from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

from bs4 import BeautifulSoup
import re
import pdb; pdb.set_trace()
pages = set()
def getLinks(pageUrl):
    global pages
    try:
        html = urlopen("http://empresasdobrasil.com"+pageUrl)
    except HTTPError as e:
        print(e)
    except URLError as e:
        print("The server could not be found!")
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.body.find("div", {"class": "container"}, False).findAll("a", href=re.compile("^(/empresas/).*$")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print("----------------\n"+newPage)
                pages.add(newPage)
                getLinks(newPage)
getLinks("/empresas")
