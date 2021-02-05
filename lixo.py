# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import re

# url = "https://www.cofermeta.com.br/rolamentos/rolamentos/rigidos-de-esferas/rolamento-rigido-de-esferas-6206-z-skf"
# page = urlopen(url)
# html = page.read()#.decode("utf-8")
# soup = BeautifulSoup(html, "html.parser")

# # print(soup.get_text())

# print (soup.find_all("a"))


# import re
# from requests_html import HTMLSession

# url = "https://www.fg.com.br/rolamento-rigido-de-esferas-6206-2z---skf/p"
# EMAIL_REGEX = r"""(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""

# # initiate an HTTP session
# session = HTMLSession()


# # get the HTTP Response
# r = session.get(url)

# # for JAVA-Script driven websites
# r.html.render()

# for re_match in re.finditer(EMAIL_REGEX, r.html.raw_html.decode()):
#     print(re_match.group())



from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

html_page = urlopen("https://www.cofermeta.com.br/rolamentos/rolamentos/rigidos-de-esferas/rolamento-rigido-de-esferas-6206-z-skf")
html_page = urlopen("https://www.cyhrolamentos.com.br/loja/produto/6206-2RS-250C-ENC")
soup = BeautifulSoup(html_page)

print(soup.get_text())
# import re
x = soup(text=re.compile('@'))

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXxx")
print(x)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXxx")


# import pdb; pdb.set_trace()