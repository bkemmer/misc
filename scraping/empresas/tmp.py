from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re
import pdb; pdb.set_trace()
# random.seed(datetime.datetime.now())

html = urlopen("http://empresasdobrasil.com/empresas")
bsObj = BeautifulSoup(html, "html.parser")
out = bsObj.body.find("div", {"class": "container"}, False).findAll("a", href=re.compile("^(/empresas/).*$"))
print(out)
