#Worked on by Jasminder Garcha
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re

CUNY_PANTRIES_WEBSITE = 'https://www.healthycuny.org/cuny-food-pantries'

response = requests.get(CUNY_PANTRIES_WEBSITE)
if response.ok == False:
    print("CUNY Food Pantries website is down.")

cuny_pantries_html = response.text

hrefs = SoupStrainer('a', href=True)
h1s = SoupStrainer('p')

hrefs_html = BeautifulSoup(cuny_pantries_html, 'lxml', parse_only=hrefs)
h1s_html = BeautifulSoup(cuny_pantries_html, 'lxml', parse_only=h1s)

websites_html = hrefs_html.find_all(href=re.compile('https://'))
telephones_html = hrefs_html.find_all(href=re.compile('tel:'))
emails_html = hrefs_html.find_all(href=re.compile('mailto:'))

websites, telephones, emails, locations = [], [], [], []

for website in websites_html:
    websites.append(website.get('href'))

for telephone in telephones_html:
    telephones.append(telephone.get_text())

for email in emails_html:
    emails.append(email.get_text())

print(websites)
print(telephones)
print(emails)