import pymongo

client = pymongo.MongoClient('mongodb+srv://terry:1@mongo-cluster.uadhh.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.moviedb
collection = db.movie

query = collection.find().limit(100)
for item in query:
	print(item)