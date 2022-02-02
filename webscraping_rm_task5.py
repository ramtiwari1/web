 
from webscraping_rm_task1 import *
from webscraping_rm_task4 import scrape_movie_details
import json
from pprint import pprint
task5 = scrape_top_list()
def get_movie_list_details(movies):
    movie_list=[]
    for i in movies:
        task5=i["Url"]
        a=(scrape_movie_details(task5))
        movie_list.append(a)
    a=open("task5_rm.json",'w')
    b=json.dump(movie_list,a,indent=4)
    a.close()
    return movie_list
url5=task5[0:10]   
pprint(get_movie_list_details(url5))
