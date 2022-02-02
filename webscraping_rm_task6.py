
from requests import models
from  webscraping_rm_task5 import*
import json
task6=get_movie_list_details(url5)
movie_language={}
def analyse_movies_language(movies_list):
    language1=[]
    b=""
    for i in movies_list:
        c=b.join(i["language"])
        language1.append(c)
        movie_language [c]=language1.count(c)
    file=open("task6_rm.json","w")
    json.dump(movie_language,file,indent=4)
    file.close()
    pprint(movie_language)
analyse_movies_language(task6)