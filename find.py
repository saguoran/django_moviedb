import pymongo
import json
from bson import json_util
import socket
from types import SimpleNamespace
import re
import copy

# {'_id': ObjectId('606c1b418d0344edcea62b2d'), 'title': 'He Who Died of Love', 'cast': ['Rosario Granados', 'Julio Villarreal', 'Hilde Krüger', 'Julián Soler', 'Luis Aldás', 'Amparo Morillo', 'Fanny Schiller', 'Pita Amor', 'Rosa Castro', 'Jorge Trevino (actor)|Jorge Trevino', 'Conchita Carracedo', 'Fernando Cortés', 'Norma Ancira', 'Alejandro Ciangherotti', 'Julio Daneri', 'Ángel Di Stefani', 'José Escanero', 'Ana María Hernández', 'Ramón G. Larrea', 'Héctor Mateos', 'Manuel Pozos', 'José Ignacio Rocha', 'Joaquín Roche'], 'directors': ['José Díaz Morales'], 'companies': ['Los Artistas Asociados'], 'year': 1945}
class Movie:
    def __init__(self, id, *args):
        self.id = id
        self.title= args[0]
        self.cast = set([i.split('|')[-1] for i in args[1]])


def parse_json(data):
    json_data:dict = json_util.loads(json_util.dumps(data))
    values = list(json_data.values())
    return Movie(str(values[0]), *values[1:])


Kevin_Bacon = "Kevin Bacon"


# sample actors
# Robert De Niro
# Chazz Palminteri 2
# José Ignacio Rocha 3
def find_actor(actor: str):
    in_tree_movies = [None]
    available_cast = set()
    distance_description = ""
    checked_cast = set(actor)
    checked_movie_ids = set()
    # distance_number = len(valid_movies)
    # valid_actors count - valid movies count = 1
    actor_str = actor.strip().lower()
    # if input is Kevin Bacon, distance = 0
    if actor_str == Kevin_Bacon.lower():
        return f"{actor} has a Bacon number of {len(in_tree_movies)}.\nf{actor}"
    client = pymongo.MongoClient(r'mongodb+srv://terry:1@mongo-cluster.uadhh.gcp.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    first_layer = client.moviedb.movie.find({"cast": re.compile(fr".*{actor_str}.*", re.IGNORECASE)}, )
    movies_layers = [[]]
    # find next movie if actor X with Kevin Bacon, distance = 1
    # guess distance is 1
    for item in first_layer:
        data = parse_json(item)
        checked_movie_ids.add(data.id)
        movies_layers[0].append(data)
        in_tree_movies[0] = data
        print(data.id, data.title, data.cast)
        if any(Kevin_Bacon in cast for cast in data.cast):
            # Kelly Bishop was in Queens Logic with Kevin Bacon
            distance_description += f"{actor} has a Bacon number of {len(in_tree_movies)}.\n"
            distance_description += f"{actor:<5} was in {data.title:<5} with\n"
            distance_description += Kevin_Bacon
            return distance_description
    # if distance 1 not found, find next movie base on cast of a movie found previous step, find distance=2,
    # guess distance > 1
    # reset movie in tree current distance, search actor relative movies start by 0 up to next number
    in_tree_movies = []
    in_tree_cast = [actor]
    distance = 0

    while True:
        next_layer_movies = []
        current_distance = len(movies_layers)
        print("current distance ", current_distance)
        # checked movies as first layer
        for movie in movies_layers[current_distance-1]:
            try:
                in_tree_movies[current_distance-1] = movie
            except IndexError:
                in_tree_movies.append(movie)
            for c in [x for x in movie.cast if x not in checked_cast]:
                try:
                    in_tree_cast[current_distance] = c
                except IndexError:
                    in_tree_cast.append(c)
                checked_cast.add(c)
                print("checked_movies",len(checked_movie_ids))
                next_layer = client.moviedb.movie.find({"cast": re.compile(fr".*{c}.*", re.IGNORECASE),"_id": {"$nin": list(checked_movie_ids)}})
                for item in next_layer:
                    data = parse_json(item)
                    try:
                        in_tree_movies[current_distance] = data
                    except IndexError:
                        in_tree_movies.append(data)
                    checked_movie_ids.add(data.id)
                    next_layer_movies.append(data)
                    print(data.id, data.title, data.cast)
                    if any(Kevin_Bacon in cast for cast in data.cast):
                        distance_description = ""
                        distance_description += f"{in_tree_cast[0]} has a Bacon number of {len(in_tree_movies)}.\n"
                        for i in range(len(in_tree_movies)):
                            distance_description += f"{in_tree_cast[i]:<5} was in {in_tree_movies[i].title:<5} with\n"
                        distance_description += Kevin_Bacon
                        return distance_description
        current_layer_movies = next_layer_movies
        distance += 1

