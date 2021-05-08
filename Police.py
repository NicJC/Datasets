import pandas as pd 
import numpy as np
from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
from sklearn.decomposition import PCA
from bs4 import BeautifulSoup
import requests
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

url = 'https://raw.githubusercontent.com/washingtonpost/data-police-shootings/master/fatal-police-shootings-data.csv'
ps = pd.read_csv(url)
ps.head()

df = ps[['date','name','manner_of_death','race','gender','state','city']]

link = 'https://abbreviations.yourdictionary.com/articles/state-abbrev.html'

pg = requests.get(link)

soup = BeautifulSoup(pg.content, 'html.parser')

tb = []

tbl = []

exp = list(range(1,58))

for s in exp:
    if s == 51:
        s += 1       
               
    State = soup.find_all('td')[(s*3)].get_text()
    tb.append(State)
    s += 1
	
a = pd.DataFrame(tb, columns=["State"])	

for s in exp:
    if s == 51:
        s += 1       
               
    Abrev = soup.find_all('td')[(s*3)+1].get_text()
    tbl.append(Abrev)
    s += 1

b = pd.DataFrame(tbl, columns=["state"])

df1 = pd.concat([b, a], axis=1)

data = {'Race' : ['Asian','White','Hispanic','Black','Other','N/A','Not Hispanic'],
 'race' : ['A','W','H','B','O','nan','N']
 }

df2 = pd.DataFrame(data=data)

df  = df.merge(df1, left_on='state', right_on='state')

df  = df.merge(df2, left_on='race', right_on='race')

df['Year'] = pd.DatetimeIndex(df['date']).year

df.rename(columns = {'date' : 'Date','name': 'Name','manner_of_death': 'Manner of Death','race':'Race Letter','gender':'Gender','state':'State Abbreviation','city':'City','State':'State','Race':'Race','Year':'Year'}, inplace = True)

df = df[['Date','Year','Name','Manner of Death','Race','Gender','State','City']]
 
df.to_csv("C:/Users/nicjc/Datasets/Police.csv")
