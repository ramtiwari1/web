
  
from webscraping_rm_task1 import *
from pprint import pprint
import json
scraped=scrape_top_list()
def group_by_year(movies):
    year_list=[]
    for i in movies:
        year=i["Year"]
        if year not  in year_list:
            year_list.append(year)
    dict2={i:[]for i in year_list}
    for j in movies:
        years=j["Year"]
        for x in dict2:
            if str(x) == str(years):
                dict2[x].append(j)
    a=open("task2_rm.json","w")
    b=json.dump(dict2,a,indent=4,sort_keys=True)
    a.close()
    return dict2                        
pprint(group_by_year(scraped))

    