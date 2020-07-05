from bs4 import BeautifulSoup
import requests
import codecs
from time import sleep

source = requests.get('https://www.worldometers.info/coronavirus/').text
soup =  BeautifulSoup(source, 'lxml')

list = [
    "Coronavirus Cases: ",
    "Deaths: ",
    "Recovered: "
]

while True:
    for article, i in zip(soup.find_all("div", class_="maincounter-number"), range(4)):
        if i == 3: i = 0
        name = article.span.text
        print(list[i] + name)
    print('---------------------------------')
    sleep(1) 
    