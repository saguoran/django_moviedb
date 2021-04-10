import pymongo, pandas as pd, json

client = pymongo.MongoClient('mongodb+srv://terry:1@mongo-cluster.uadhh.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
db = client.moviedb
collection = db.movie

raw_data = pd.read_table('data.txt', header=None)
raw_data = raw_data[raw_data[0].str.contains('"title":')].reset_index(drop=True)
raw_data.replace(regex=True,to_replace=r'\[\[|\]\]',value='',inplace=True)
movie_list = []

def convert_json(string):
	movie_list.append(json.loads(string[0]))

raw_data.apply(convert_json,axis=1)
collection.insert_many(movie_list)