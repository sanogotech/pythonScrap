from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import csv

#https://blog.lesjeudis.com/web-scraping-avec-python

# specify the url
#urlpage = 'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

# query the website and return the html to the variable 'page'
#page = urllib.request.urlopen(urlpage)
# parse the html using beautiful soup and store in variable 'soup'
#soup = BeautifulSoup(page, 'html.parser')
# http://www.cmegroup.com/trading/products/#sortField=oi&sortAsc=false&venues=3&page=1&cleared=1&group=1



req = Request('http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')
#print(soup)

#Recherche d’éléments HTML
# find results within table
table = soup.find('table', attrs={'class': 'tableSorter'})

if table is not None:
    # Do something about x
    results = table.find_all('tr')
    print('Number of results', len(results))
    
print("End ....")