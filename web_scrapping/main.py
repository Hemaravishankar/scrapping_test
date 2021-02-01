from bs4 import BeautifulSoup
import requests
import re

with open('sample.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

name =  soup.find('p', class_="name").get_text(strip=True)
email = soup.p
email.string = "markdavids@recruitly.io"

print(f'Name is ---- {name}')
print(f'email id is --- {email.get_text(strip=True)}')


