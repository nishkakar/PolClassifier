from bs4 import BeautifulSoup
import requests

# takes in a url and returns a dict of [word, occurrences]
def scraper(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    text = ''
    for par in soup.find_all('p'):
        text = text + ''.join(par.findAll(text=True))
    words = text.split()
    data = {}
    for word in words:
        test = str(word)
        if test in data:
            data[test] + 1
        else:
            data[test] = 1
    print data

# scraper('http://www.cnn.com/interactive/us/map-same-sex-marriage/')
scraper('http://www.cnn.com/2015/07/03/travel/solar-plane-flight/index.html')
