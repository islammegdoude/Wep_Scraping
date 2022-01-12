import requests
from bs4 import BeautifulSoup
# import csv
# from itertools import zip_longest
#github_user = input('Input github user : ')
kak = []
url = 'https://github.com/islammegdoude?tab=repositories'
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
profile = soup.findAll('h3', {'class': 'wb-break-all'})
for i in range(len(profile)):
    kak.append('https://github.com/' + profile[i].find("a").attrs['href'])

print(kak)
