
  
import requests,json
from bs4 import BeautifulSoup
from pprint import pprint
url="https://www.imdb.com/india/top-rated-indian-movies/"
req=requests.get(url)
# # pprint(req.text)
soup=BeautifulSoup(req.text,"html.parser")

def scrape_top_list():
    main_div= soup.find('div',class_='lister') 
    #return main_div
#print(scrape_top_list)
    Tbody = main_div.find('tbody',class_='lister-list')
    #return Tbody
#print(scrape_top_list)
    trs=Tbody.find_all("tr")
    #return trs
#print(scrape_top_list)
    
    Movie_Rank,Movie_Name,Movie_Rating,Movie_Realese_Date,Movie_Url=[],[],[],[],[]
    for tr in trs:
        position=tr.find("td", class_="titleColumn").get_text().strip()
        
        rank=''
        for i in position:
            if '.' not in i:
                rank=rank+i
            else:
                break
        Movie_Rank.append(rank)
        title=tr.find("td", class_="titleColumn").a.get_text()
        Movie_Name.append(title)
        rating=tr.find("td", class_="ratingColumn").strong.get_text()
        Movie_Rating.append(rating)
        date=tr.find("td", class_="titleColumn").span.get_text()
        Movie_Realese_Date.append(date)
        url1=tr.find("td", class_="titleColumn").a['href']
        link1="https://www.imdb.com"+url1
        Movie_Url.append(link1)
        
        all_movies=[]
        dict1={'Position':'','Name':'','Year':'','Rating':'','Url':''}
        for i in range(0,len(Movie_Rank)):
            dict1['Position']=int(Movie_Rank[i])
            dict1['Name']=str(Movie_Name[i])
            dict1['Year']=(Movie_Realese_Date[i])[1:5]
            dict1['Rating']=float(Movie_Rating[i])
            dict1['Url']=Movie_Url[i]
            all_movies.append(dict1.copy())
            dict1={'Position':'','Name':'','Year':'','Rating':'','Url':''}
        a=open("task1_rm.json","w")
        b=json.dump(all_movies,a,indent=4)
        a.close()
    return (all_movies)
(scrape_top_list())