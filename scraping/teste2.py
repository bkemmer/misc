from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://empresasdobrasil.com/empresa/marcos-ferreira-dias-advogados-associados-04998661000109")
bsObj = BeautifulSoup(html, "html.parser")
#print(bsObj)
labelList = bsObj.findAll("div", {"class":"col-md-8"})
print(labelList)

#textList = bsObj.findAll("span", {"class":"text"})

#for (l,t) in zip(labelList, textList):
#	print(l.get_text(),':',t.get_text())
