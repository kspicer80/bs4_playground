import requests
import pandas as pd
pd. set_option('display.max_rows', 500)
pd. set_option('display.max_columns', 500)
pd. set_option('display.width', 1000)
from bs4 import BeautifulSoup

# Goals: so, let's do a little BeautifulSoup parsing of tables; I've got a table at the url below that has a table of info I want to pull down for my best buddy ...

# Following the lead of Thiago Santos Figueira at https://medium.com/geekculture/web-scraping-tables-in-python-using-beautiful-soup-8bbc31c5803e

url = "https://blog.powerscore.com/lsat/top-100-law-school-application-deadlines-2022-edition/"
data = requests.get(url).text

soup = BeautifulSoup(data, "html.parser")

print('Classes of each table on the page:')
for table in soup.find_all('table'):
    print(table.get('class'))
    
tables = soup.find('table', class_ = 'tablepress')

df = pd.DataFrame(columns=['2021 Rank', 'Law School Name', 'Application Deadline', 'Latest Acceptable LSAT', 'Accept the GRE?', 'Notes from the University', 'Difference from last cycle'])

for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    
    if (columns != []):
        school_rank = columns[0].text.strip()
        school_name = columns[1].text.strip()
        app_deadline = columns[2].text.strip()
        latest_date = columns[3].text.strip()
        gre = columns[4].text.strip()
        notes = columns[5].text.strip()
        difference_from_last_year = columns[6].text.strip()
        
        df = df.append({'2021 Rank': school_rank, 'Law School Name': school_name, 'Application Deadline': app_deadline, 'Latest Acceptable LSAT': latest_date, 'Accept the GRE?': gre, 'Notes from the University': notes, 'Difference from last cycle': difference_from_last_year}, ignore_index=True)

#df = df.assign(Index=range(len(df))).set_index('2021 Rank')

df = df.set_index('2021 Rank')
print(df.head())
print(df.to_markdown())

# An Alternative Way to Do all This (although the website here is blocking the request)

#df_pandas = pd.read_html(url, attrs = {'class': 'tablepress'}, flavor='bs4')
#print(df_pandas.head())
