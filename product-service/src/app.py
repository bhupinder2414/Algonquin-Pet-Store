from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Create a Flask application
app = Flask(__name__)

# Enable CORS (allowing requests from any domain)
CORS(app)

# Get the port from the environment variable or default to 3030
port = int(os.getenv('PORT', 3030))

# Define a route for "/products" that returns a JSON response
@app.route('/products', methods=['GET'])
def get_products():
    # Create a list of products as a JSON response
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99}
    ]
    return jsonify(products)

# Start the Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
