from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.foneempresas.com/telefone/empresa/telefone-de-a-pioneira-goncalves-mg/23186325000106")
bsObj = BeautifulSoup(html, "html.parser")
#print(bsObj)
labelList = bsObj.findAll("span", {"class":"label"})
textList = bsObj.findAll("span", {"class":"text"})

for (l,t) in zip(labelList, textList):
	print(l.get_text(),':',t.get_text())
