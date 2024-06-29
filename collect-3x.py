import requests as req  # Make HTTP request
from datetime import datetime  # Date and time
from pymongo import MongoClient as mongo  # Database
from config.config import env  # Env config

# Get current time
timestamp = datetime.now().timestamp()

# Create mongo connection
client = mongo(env('MONGO_ATLAS'))

db = client["vpn"] # Use database
collection = db['stats'] # Use collection

# The base URL
base_url = "http://i.amirhossein.info:8080"
# Add headers to authorize in API
headers = {
    "Cookie": env("COOCIE")
}

# Get list of usages
list = req.post(f"{base_url}/panel/inbound/list", headers=headers, data={})
# Make json and get only `obj` item
inbounds_data = list.json()['obj']


# Iterate through inbounds and process clientStats
for inbound in inbounds_data:
    for user in inbound["clientStats"]:
        document = {
            'remark': user["email"],
            'download': user["down"],
            'upload': user["up"],
            'id': user["id"],
            'sequence': timestamp
        }

        # Insert
        collection.insert_one(document)
