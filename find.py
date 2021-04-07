import pymongo, json
from bson import json_util

class node:
    __slots__ = ('movie', 'actor')

def parse_json(data):
    return json.loads(json_util.dumps(data))

def find_actor(actor):
	# query = collection.find().limit(1000)
	# query = collection.find( { "cast": "Carl Washington" }, )
	query = collection.find( { "cast": actor}, )
	#query = collection.find( {}, {"title": 1, "cast": 1, '_id': 0})
	for item in query:
		print(item)
		data = parse_json(item)
		#data = json.dumps(item)
		print(data)
		return data

client = pymongo.MongoClient('mongodb+srv://terry:1@mongo-cluster.uadhh.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.moviedb
collection = db.movie