from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import requests
import re

class cuny_pantry:
    def __init__(self, college, campus_website, location, email, phone):
        self.college = college
        self.campus_website = campus_website
        self.location = location
        self.email = email
        self.phone = phone

bcc_pantry = cuny_pantry('Bronx Community College', '', '', '', '')
hcc_pantry = cuny_pantry('Hostos Community College', '', '', '', '')
lc_pantry = cuny_pantry('Lehman College', '', '', '', '')
bc_pantry = cuny_pantry('Brooklyn College', '', '', '', '')
kcc_pantry = cuny_pantry('Kingsborough Community College', '', '', '', '')
mec_pantry = cuny_pantry('Medgar Evers College', '', '', '', '')
nct_pantry = cuny_pantry('NYC College of Technology (City Tech)', '', '', '', '') 
bar_pantry = cuny_pantry('Baruch College', '', '', '', '') 
bmcc_pantry = cuny_pantry('Borough of Manhattan Community College', '', '', '', '')
ccny_pantry = cuny_pantry('City College of New York', '', '', '', '') 
gutt_pantry =  cuny_pantry('Guttman Community College', '', '', '', '')
hunt_pantry = cuny_pantry('Hunter College', '', '', '', '')
jj_pantry = cuny_pantry('John Jay College', '', '', '', '')
lcc_pantry = cuny_pantry('LaGuardia Community College', '', '', '', '')
qc_pantry = cuny_pantry('Queens College', '', '', '', '')
qcc_pantry = cuny_pantry('Queensborough Community College', '', '', '', '')
sj_pantry = cuny_pantry('School of Journalism', '', '', '', '')
sl_pantry = cuny_pantry('School of Law', '', '', '', '')
y_pantry =  cuny_pantry('York College', '', '', '', '')
csi_pantry = cuny_pantry('College of Staten Island', '', '', '', '')

cuny_pantries = [bcc_pantry, hcc_pantry, lc_pantry, bc_pantry, kcc_pantry, mec_pantry, nct_pantry, bar_pantry, bmcc_pantry, ccny_pantry, gutt_pantry, hunt_pantry, jj_pantry, lcc_pantry, qc_pantry, sj_pantry, sl_pantry, y_pantry, csi_pantry]

CUNY_PANTRIES_WEBSITE = 'https://www.healthycuny.org/cuny-food-pantries'

response = requests.get(CUNY_PANTRIES_WEBSITE)
if response.ok == False:
    print("CUNY Food Pantries website is down.")
cuny_pantries_html = response.text

a_tags = SoupStrainer('a')

pantries_a_tags = BeautifulSoup(cuny_pantries_html, 'lxml', parse_only=a_tags)
pantries_emails = pantries_a_tags.select('a[href^="mailto:"]')
#pantries_telephones = pantries_a_tags.select('a[href^="tel:"]')
print(pantries_emails)
#print(pantries_telephones)