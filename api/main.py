from flask import Flask, jsonify
from flask_cors import CORS

from pymongo import MongoClient as mongo

import os

app = Flask(__name__)

CORS(app)

mongo_url = os.getenv('MONGO_URL', 'mongodb://127.0.0.1:27017')

client = mongo(mongo_url)

db = client["vpn"]
collection = db['stats']

def getData():
    data = collection.find()
    
    return data

@app.route('/api/data', methods=['GET'])
def all():
    response = {}
    
    result = getData()
        
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
    app.run("0.0.0.0", port=8080, debug=True)