from bs4 import BeautifulSoup  
import requests  
import requests.exceptions  
from urllib.parse import urlsplit  
from collections import deque  
import re  


new_urls = deque(['https://www.fg.com.br/rolamento-rigido-de-esferas-6206-2z---skf/p']) 
new_urls = deque(['https://www.cofermeta.com.br/rolamentos/rolamentos/rigidos-de-esferas/rolamento-rigido-de-esferas-6206-z-skf']) 
new_urls = deque(['https://www.cyhrolamentos.com.br/loja/produto/6206-2RS-250C-ENC']) 


processed_urls = set() 


emails = set()  

while len(new_urls):  
    url = new_urls.popleft()  
    processed_urls.add(url)  
    print("Processing %s" % url)  
    try:  
        response = requests.get(url)  
    except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):  
        continue  
    
    parts = urlsplit(url)  
    base_url = "{0.scheme}://{0.netloc}".format(parts)  
    path = url[:url.rfind('/')+1] if '/' in parts.path else url     
    
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))  
    emails.update(new_emails)  
    
    
    soup = BeautifulSoup(response.text) 
    
    
    for anchor in soup.find_all("a"):  
        link = anchor.attrs["href"] if "href" in anchor.attrs else ''  
        if link.startswith('/'):  
            link = base_url + link  
        elif not link.startswith('http'):  
            link = path + link  
        if not link in new_urls and not link in processed_urls:  
            new_urls.append(link)  
            
            
    for email in emails:  
        print(email)     