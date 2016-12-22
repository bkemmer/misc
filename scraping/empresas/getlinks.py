from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import pdb; pdb.set_trace()
random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://empresasdobrasil.com/empresas"+articleUrl)
    bsObj = BeautifulSoup(html, "html.parser")
    out = []
    for div in bsObj.find("div", {"class": "container"}):
        out.append(div.findAll("a", href=re.compile("^(/empresas/).*$")))
    return out 
    #bsObj.find("div", {"class": "container"}, False).findAll("a", href=re.compile("^(/empresas/).*$"))

links = getLinks("")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
