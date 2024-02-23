from flask import Flask, jsonify, request
import dbConfig
import sys
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="http://localhost:5173")

@app.route('/')
def flask_mongodb_atlas():
    return "flask react mongodb atlas app"

@app.route('/data')
def data():
    print('Hello world', file=sys.stderr)
    data = dbConfig.db.collection.find_one({"name": "John"})
    print("data is", data, file=sys.stderr)
    data["_id"] = str(data["_id"])
    return jsonify(data)

@app.route('/input', methods=['POST', 'GET'])
def input():
    input = request.get_json()['input']
    result = dbConfig.db.collection.insert_one({"name": input})
    inserted_id = str(result.inserted_id)
    response_data = {
        "_id": inserted_id,
        "name": input
    }
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(port=8000, debug=True)