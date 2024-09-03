from flask import Flask, jsonify, request
import requests
from app import app, db
from models import Profile

@app.route('/', methods=['GET'])
def root():
    return jsonify({"message": "Use /create_profile to create a profile and search Wikipedia."})

@app.route('/profiles', methods=['GET'])
def get_profiles():
    profiles = Profile.query.all()
    return jsonify([profile.serialize() for profile in profiles])

@app.route('/create_profile', methods=['POST'])
def create_profile():
    body = request.get_json()
    print("Datos recibidos:", body)
    
    name = body.get("name")
    country = body.get("country")
    city = body.get("city")
    year = body.get("year")

    if not all([name, country, city, year]):
        return jsonify({"error": "Todos los campos deben ser llenados"}), 400
    
    try: 
        new_profile = Profile(name=name, country=country, city=city, year=year)
        db.session.add(new_profile)
        db.session.commit()

        search_query = " ".join(filter(None, [name, country, year, city]))
        wikipedia_url = "https://es.wikipedia.org/w/api.php"

        params = {
            'action': 'query',
            'format': 'json',
            'list': 'search',
            'srsearch': search_query if search_query else 'Historia 1920',
            'utf8': 1,
            'srlimit': 20
        }
        response = requests.get(wikipedia_url, params=params)
        data = response.json()
        
        return jsonify({
            "message": "Profile creado exitosamente", 
            "profile": {"id": new_profile.id},
            "wikipedia_search_results": data
        }), 201 
     
    except Exception as error:
        db.session.rollback()
        return jsonify({"error": f"{error}"}), 500


if __name__ == '__main__':
    app.run(debug=True)