import requests
import pandas as pd
from bs4 import BeautifulSoup

# Following the lead of Thiago Santos Figueira at https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e

url = "https://blog.powerscore.com/lsat/top-100-law-school-application-deadlines-2022-edition/"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

print('Classes of each table on the page:')
for table in soup.find_all('table'):
    print(table.get('class'))
