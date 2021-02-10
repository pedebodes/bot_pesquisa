from bs4 import BeautifulSoup  
import requests  
import requests.exceptions  
from fake_useragent import UserAgent
from urllib.parse import urlsplit  
from collections import deque  
import re  
from tabelas import engine, UrlBase,session
from urllib.parse import urlparse
import random


# new_urls = deque(['https://www.fg.com.br/rolamento-rigido-de-esferas-6206-2z---skf/p']) 
# new_urls = deque(['https://www.cofermeta.com.br/rolamentos/rolamentos/rigidos-de-esferas/rolamento-rigido-de-esferas-6206-z-skf']) 
# new_urls = deque(['https://www.cyhrolamentos.com.br/loja/produto/6206-2RS-250C-ENC']) 
# new_urls = deque(['https://www.oliveirarolamentos.com.br/rolamento-rigido-de-esferas-6206-2rs-30x62x16mm.html']) 

VARRER_TODO_SITE =  False
# VARRER_TODO_SITE =  True


processed_urls = set() 


emails = set()  

result = session.query(UrlBase)\
    .distinct()\
    .all()
    # .filter(UrlBase.dominio == 'www.cofermeta.com.br')\


        
def getEmail(part1, part2):
    try:
        return list(
            dict.fromkeys(
                re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", part1, part2)
                )
            )
    except:
        return None

def getCnpj(part1):
    try:
        return re.search("\d{2}.\d{3}.\d{3}/\d{4}-\d{2}", part1).group()
    except:
        return None
      
    pass
def getTelefoneFixo(part1):
    try:
      return re.search('\(\d{2}\)\s\d{4}\-\d{4}', part1).group()
    except:
        return None
    
def getCelular(part1):
    try:
        return re.search('\(\d{2}\)\s\d{5}\-\d{4}', part1).group()
    except:
        return None
      
def getCep(part1):
    try:
        return re.search(r"CEP: \d{5}.\d{3}", part1).group()
    except:
        return None
      


for row in result:
    # print ("Dominio: ",row.dominio, " <<>>> Url: ",row.url)
    new_urls = deque([row.url])
    while len(new_urls):  
        url = new_urls.popleft()  
        processed_urls.add(url)  
        ua = UserAgent()
        # url = "https://rolamentoscbf.com.br/" # verificar porque não pega dados de tel email cnpj nada, verificar regex ou coisa do tipo , se possivel outra forma de coletar esses dados
        print("Processando %s" % url)  

        try:  
            
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36', "Upgrade-Insecure-Requests": "1","DNT": "1","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Accept-Encoding": "gzip, deflate"}
            response = requests.get(url,headers=headers, allow_redirects = True )
            # response = requests.get(url, {"User-Agent": ua.random}, timeout=5, allow_redirects = True )  
        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):  
            continue  

        parts = urlsplit(url)
        
        
        base_url = "{0.scheme}://{0.netloc}".format(parts)  
        path = url[:url.rfind('/')+1] if '/' in parts.path else url     
        
        new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))  
        emails.update(new_emails)  
        

        email = getEmail(response.text, re.I)
        if email is not None and len(email) > 0:
            session.query(UrlBase).filter(UrlBase.id == row.id).update({"email": str(email)})
        
        cnpj = getCnpj(response.text)
        if cnpj is not None:
            session.query(UrlBase).filter(UrlBase.id == row.id).update({"cnpj": cnpj})

        cep = getCep(response.text)
        if cep is not None:
            session.query(UrlBase).filter(UrlBase.id == row.id).update({"cep": cep.split()[1]})

        fixo =getTelefoneFixo(response.text)  
        if fixo is not None:
            session.query(UrlBase).filter(UrlBase.id == row.id).update({"telefone_fixo": fixo})
            
        celular =getCelular(response.text) 
        if celular is not None:
            session.query(UrlBase).filter(UrlBase.id == row.id).update({"telefone_celular": celular })
        
        
        session.commit()


        

        
        soup = BeautifulSoup(response.text) 
        
        
        for anchor in soup.find_all("a"):  
            link = anchor.attrs["href"] if "href" in anchor.attrs else ''  
            if link.startswith('/'):  
                link = base_url + link  
            elif not link.startswith('http'):  
                link = path + link  
                # import pdb; pdb.set_trace()
            if not link in new_urls and not link in processed_urls and VARRER_TODO_SITE:  
                print(link)
                aux = urlparse(link)
                if row.dominio == aux.netloc :
                    # import pdb; pdb.set_trace()
                    new_urls.append(link)  
                
                
                
        # for email in emails:  
        #     session.query(UrlBase).filter(UrlBase.id == row.id).update({"email": email})
        #     session.commit()
        #     print(email)     
            
        # if not VARRER_TODO_SITE :
        
        #     sys.exit()
        
        
