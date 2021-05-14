from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import csv

#https://blog.lesjeudis.com/web-scraping-avec-python



req = Request('http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/', headers={'User-Agent': 'Mozilla/5.0'},method='GET')
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
#print(soup)

#Recherche d’éléments HTML
# find results within table
table = soup.find('table', attrs={'class': 'tableSorter2'})

if table is not None:
    # Do something about x
    results = table.find_all('tr')
    print('Number of results', len(results))
    
print("End ....")