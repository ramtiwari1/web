from requests import models
from  webscraping_rm_task5 import*
import json
task7=get_movie_list_details(url5)
movie_director={}
def analyse_movies_directors(movies_list):
    director_movie=[]
    b=""
    for i in movies_list:
        c=b.join(i["director"])
        director_movie.append(c)
        movie_director [c]=director_movie.count(c)
    file=open("task7_rm.json","w")
    json.dump(movie_director,file,indent=4)
    file.close()
    pprint(movie_director)
analyse_movies_directors(task7)