from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re

class cuny_pantry:
    def __init__(self, college, url, location, email, phone):
        self.college = college
        self.url = url
        self.location = location
        self.email = email
        self.phone = phone

bcc_pantry = cuny_pantry('Bronx Community College', '', '', '', '')

CUNY_PANTRIES = 'https://www.healthycuny.org/cuny-food-pantries'

response = requests.get('https://www.healthycuny.org/cuny-food-pantries')
if response.ok == False:
    print("CUNY Food Pantries website is down.")
cuny_pantries_html = response.text

a_tags = SoupStrainer('a')


pantries_emails = BeautifulSoup(cuny_pantries_html, 'lxml', parse_only=a_tags).select('a[href^="mailto:"]')

print(pantries_emails)