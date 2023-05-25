import requests as req  # Make HTTP request
from datetime import datetime  # Date and time
from pymongo import MongoClient as mongo  # Database
from config.config import env  # Env config

# Get current time
current_time = datetime.now().strftime("%H:%M")

# Create mongo connection
client = mongo(env("MONGO_ATLAS"))

db = client["vpn"]  # Use database
collection = db['stats']  # Use collection

# The base URL
base_url = "http://95.216.138.218:2003"
# Add headers to authorize in API
headers = {
    "Cookie": env("COOCIE")
}

# Get list of usages
list = req.post(f"{base_url}/xui/inbound/list", headers=headers, data={})
# Make json and get only `obj` item
data = list.json()["obj"]

# Lopp in records and insert in mongo
for user in data:
    # Create doc
    document = {
        'remark': user["remark"],
        'download': user["down"],
        'upload': user["up"],
        'id': user["id"],
        'sequence': current_time
    }

    # Insert
    collection.insert_one(document)
