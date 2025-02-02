from flask import Flask, jsonify
from flask_cors import CORS

from pymongo import MongoClient as mongo

import os

app = Flask(__name__)

CORS(app)

mongo_url = os.getenv('MONGO_URL', 'mongodb://127.0.0.1:27017')

client = mongo(mongo_url)

def getData(collection):
    data = collection.find()
    
    return data

@app.route('/api/data/day', methods=['GET'])
def every_day():
    response = {}
    
    db = client["vpn"]
    collection = db['stats']
    
    result = getData(collection)
        
    items = []
    
    for one in result:
        who = {
            '_id': str(one['_id']),
            'remark': one['remark'],
            'download': one['download'],
            'upload': one['upload'],
            'id': one['id'],
            'sequence': one['sequence']
        }

        items.append(who)        
        
    response['data'] = items
    
    return jsonify(response), 200

@app.route('/api/data/minute', methods=['GET'])
def every_minute():
    response = {}
    
    db = client["vpn-one"]
    collection = db['stats']
    
    result = getData(collection)
        
    items = []
    
    for one in result:
        who = {
            '_id': str(one['_id']),
            'remark': one['remark'],
            'download': one['download'],
            'upload': one['upload'],
            'id': one['id'],
            'sequence': one['sequence']
        }

        items.append(who)        
        
    response['data'] = items
    
    return jsonify(response), 200

if __name__ == "__main__":
    app.run("0.0.0.0", port=7676, debug=True)