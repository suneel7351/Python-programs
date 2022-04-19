import pymongo


client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

db = client["pythondb"]

dblist = client.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

col = db["student"]

collist = db.list_collection_names()
if "student" in collist:
    print("The collection exists.")
