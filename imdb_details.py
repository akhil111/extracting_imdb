
import sys
import csv
import requests 

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from pandas import Series,DataFrame



length=int(sys.argv[1])
movie_list=[]
rating_list=[]
stars_list=[]
director_list=[]

with open('akhil.csv','w') as csvfile:
    for i in range(1,length):
        driver = webdriver.Firefox()
        driver.get('http://www.imdb.com/title/tt000000{}/'.format(i))
        
        page=requests.get('http://www.imdb.com/title/tt000000{}/'.format(i))
        soup=BeautifulSoup(page.content,'html.parser')
        movie=soup.find('h1',class_="").text
        rating=soup.find('span',itemprop="ratingValue").text
        director=soup.find('span',class_="itemprop",itemprop="name").text
        stars=soup.find('span',class_="small",itemprop="ratingCount").text

        print(movie)
        movie_list.append(movie)
        print(rating)
        rating_list.append(rating)
        print(stars)
        stars_list.append(stars)
        print(director)
        director_list.append(director)

  
#        akhil=csv.writer(csvfile)
#        akhil.writerow(imdb_list)
        driver.quit()
    


movie_ratings = pd.DataFrame({'movie': movie_list,
                              'rating': rating_list,
                              'stars':stars_list,
                              'director': director_list,
                              },index=[np.arange(length-1)])
        

print(movie_ratings)
print(movie_ratings.sort_index(by='rating'))












