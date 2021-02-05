# import pandas as pd
# import numpy as np
import urllib
from fake_useragent import UserAgent
import requests
import re
# from urllib.request import Request, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from tabelas import engine, UrlBase


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

# informar termo de pesquisa , numero de resultados por pagina
def google_results(busca, n_results):
    busca = urllib.parse.quote_plus(busca)
    n_results = n_results
    ua = UserAgent()
    google_url = "https://www.google.com/search?q=" + busca + "&num=" + str(n_results)
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result]
    
    
    links=[i.group(1) for i in results if i != None]
    for x in results:
        if x != None:
            session.add(UrlBase(dominio = urlparse(x.group(1)).netloc,url = x.group(1)))
            
    session.commit()
    
    return (links)


x = google_results('6206', 30)
