from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import os
import time
import shutil


def removeQuestMarkAndAfter(link):
    link = re.sub('\?.+', '', link)
    return link


url = "https://data.worldbank.org/indicator?tab=featured"
html = urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
sections = soup.find("div", {"class": "overviewArea body"}).findAll("section", {"class": "nav-item"})
ulList = list(map(lambda x: x.findAll("ul")[-1], sections))
liList = []
for ul in ulList:
    lis = ul.findAll("li")
    liList += lis

hrefList = list(map(lambda x: x.find("a").get("href"), liList))
links = list(map(lambda x: 'https://data.worldbank.org' + removeQuestMarkAndAfter(x), hrefList))
links = list(set(links))
for index, link in enumerate(links):
    os.system('python3 scripts/getWorldBankDataset.py ' + link)
    time.sleep(3)
    if index % 20 == 0:
        status = str(round(index*100/len(links))) + ' %  completed'
        print(status)

worldBankIndicatorsFolder = '500ds-Branko/world-bank-indicator-datasets/indicators'
shutil.move('indicators', worldBankIndicatorsFolder)
shutil.rmtree('cache')
