
  
from webscraping_rm_task2 import *
from pprint import pprint
import json
decadee=group_by_year(scraped)
def group_by_decade(movies):
    decad_list=[]
    dict3={}
    for i in movies:
        mod = int(i)%10
        decode = int(i)-mod
        if decode not in decad_list:
            decad_list.append(decode)
        decad_list.sort()
        for i in decad_list:
            dict3[i]=[]
        for i in dict3:
            decode_movie10=i+9
            for x in movies:
                if int(x)<=int(decode_movie10) and int(x)>=int(i):
                    for y in movies[x]:
                        dict3[i].append(y)
    a=open("task3_rm.json","w")
    b=json.dump(dict3,a,indent=4,sort_keys=True)
    a.close()
                    
    return dict3
pprint(group_by_decade(decadee))