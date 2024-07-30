from flask import jsonify
from app import app
from app.spiders import fetch_reviews

@app.route('/fetch_reviews', methods=['GET'])
def fetch_reviews_route():
    fetch_reviews()
    return jsonify({'message': 'Reviews fetched and stored successfully!'})
