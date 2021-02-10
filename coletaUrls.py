import urllib
# from fake_useragent import UserAgent
import requests
import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from tabelas import session, UrlBase,UrlIgnorar
import json
import pathlib

# informar termo de pesquisa , numero de resultados por pagina
def google_results(busca, n_results,ignorar):
    busca = urllib.parse.quote_plus(busca)
    n_results = n_results
    # ua = UserAgent()
    google_url = "https://www.google.com/search?q=" + busca + "&num=" + str(n_results)
    # print (google_url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
    response = requests.get(google_url,headers=headers, allow_redirects = True )
    # response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result = soup.find_all('div', attrs = {'class': 'ZINbbc'})
    results=[re.search('\/url\?q\=(.*)\&sa',str(i.find('a', href = True)['href'])) for i in result]
    
    
    links=[i.group(1) for i in results if i != None]
    for x in results:
        if x != None:
            
            ignorar = session.query(UrlIgnorar).filter(UrlIgnorar.dominio.ilike(urlparse(x.group(1)).netloc.split('.')[1])).all()
                        
            if len(ignorar) == 0:
                
                ext = pathlib.Path(x.group(1)).suffix
                
                ignorarExtensoes = ['.xls','.xlsx', '.pdf', '.rar', '.exe']

                result = list(filter(lambda x: str(ext).lower() in x, ignorarExtensoes))  
                if len(result) > 0:
                    session.add(UrlBase(dominio = urlparse(x.group(1)).netloc,url =urlparse(x.group(1)).scheme+"://"+urlparse(x.group(1)).netloc))
                else:
                    session.add(UrlBase(dominio = urlparse(x.group(1)).netloc,url = x.group(1)))
            
    session.commit()
    
    
    
    
        
    return (links)



# Consulta URl para ignorar
ignorar = session.query(UrlIgnorar).all()

x = google_results('rolamentos', 3000,ignorar)
# print(x)