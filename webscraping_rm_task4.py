
from webscraping_rm_task1 import scrape_top_list
from bs4 import BeautifulSoup
from pprint import pprint
import json,requests
task4=scrape_top_list()
#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
def scrape_movie_details(movies):
    details_movie={}
    url=requests.get(movies)
    soup=BeautifulSoup(url.text,"html.parser")
    title4=soup.find(class_="TitleBlock__Container-sc-1nlhx7j-0 hglRHk")
    ul4=soup.find_all("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-all ipc-metadata-list--base")
    li4=soup.find("div",class_="ipc-metadata-list-item__content-container").text
    poster4=soup.find("a",class_="ipc-lockup-overlay ipc-focusable")['href']
    time4=title4.find_all("li",class_="ipc-inline-list__item")
    a=0
    for i in time4:
        if a==2:
             details_movie["runtime"]=i.text
        a+=1
    for j in ul4:
        b=[]
        if "Language" in j.text:
            c=j.find_all("li")
            for i in c:
                if "Language" in i.text:
                    d=i.find("div")
                    e=d.find_all("a")
                    for k in e:
                        b.append(k.get_text())
                    details_movie["language"]=b
                if "Country" in i.text:
                    f=i.find("a")
                    details_movie["country"]=f.get_text()
        details_movie["name"]=soup.find("h1").get_text()
        details_movie["director"]=[li4]
        details_movie["poster"]="https://www.imdb.com"+poster4
        #details_movie["bio"]=soup.find("span",class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text
        details_movie["genre"]=soup.find("span",class_="ipc-chip__text").text
    c=open("task4_rm.json","w")
    g=json.dump(details_movie,c,indent=4)
    c.close()
    return details_movie
num=int(input("Enter A Movie Rank(1 To 250) To Get Details:"))
url1=task4[num-1]["Url"]
pprint(scrape_movie_details(url1))


