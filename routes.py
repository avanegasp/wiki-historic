from flask import Flask, jsonify, request
import requests
from app import app, db
from models import Profile

@app.route('/', methods=['GET'])
def root():
    wikipedia_url = "https://es.wikipedia.org/w/api.php"

    params = {
        'action': 'query',
        'format': 'json',
        'list': 'search',
        'srsearch': 'Historia 1920',
        'utf8': 1,
        'srlimit': 10
    }

    response = requests.get(wikipedia_url, params=params)
    data = response.json()
    print(data)
    return jsonify(data)

@app.route('/profile', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([profile.serialize() for profile in profiles])

@app.route('/create_profile', methods=['POST'])
def create_profile():
    body = request.get_json()
    
    name = body.get("name", None)
    country = body.get("country", None)
    city = body.get("city", None)
    year = body.get("year", None)

    if name is None or country is None or city is None or year is None:
        return jsonify({"error": "Todos los campos deben ser llenados"}), 400
    
    if Profile.query.filter_by(name = name).first() is not None:
        return jsonify({"error":"Name ya está siendo utilizado"}), 400
    
    try: 
        new_profile = Profile(name = name, country = country, city = city, year = year)
        db.session.add(new_profile)
        db.session.commit()
        return jsonify({"message":"Profile creado exitosamente", "profile":{"id":new_profile.id}}), 201
    
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": f"{error}"}),500


if __name__ == '__main__':
    app.run(debug=True)