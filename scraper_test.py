from bs4 import BeautifulSoup
import requests 
import re 

response = requests.get('https://www.cuny.edu/academics/current-initiatives/office-of-early-childhood-initiatives/childhood/')
html_doc = response.text

soup = BeautifulSoup(html_doc, 'lxml')
schools = soup.h3

print(schools)


