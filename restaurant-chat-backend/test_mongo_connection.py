from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from urllib.parse import quote_plus  # This import can be used if you need to encode special characters in your URI

# Replace <db_password> and <your_database_name> with your actual password and database name
username = "nakli491"
password = "3LeiJshlpGep7mxL"
cluster = "cluster0.go8cq.mongodb.net"
database_name = "Cluster0"  # Replace with your database name

# Encode the password in case it has special characters
encoded_password = quote_plus(password)

# Construct the URI
uri = f"mongodb+srv://{username}:{encoded_password}@{cluster}/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
