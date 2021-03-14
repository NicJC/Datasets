  
import pandas as pd
import requests
from io import StringIO
import os
import numpy as np
from bs4 import BeautifulSoup


# Get data

url='https://raw.githubusercontent.com/owid/owid-datasets/master/datasets/Births%20outside%20of%20marriage/Births%20outside%20of%20marriage.csv'
data=pd.read_csv(url)


data.columns = ['Country','Year','birth%']

data['Count'] =  data.groupby('Country')['Country'].transform('count')

df = data[['Country', 'Year','birth%','Count']]

pd.options.display.float_format = '{:,.1f}'.format

df.to_csv("C:/Users/nicjc/Datasets/Birth rate.csv")
