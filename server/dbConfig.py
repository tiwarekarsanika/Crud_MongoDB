from flask import Flask
from flask_pymongo import pymongo
# import app

CONNECTION_STRING = "mongodb+srv://tiwarekarsanika:bG8REetmLSXu29MG@cluster0.4dephlt.mongodb.net/?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('some-project')
collection1 = pymongo.collection.Collection(db, 'some-project')