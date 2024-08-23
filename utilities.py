from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

centers_url_string = 'https://www.cuny.edu/current-students/student-affairs/student-services/counseling/#counseling'

aid_options = ["Food Insecurity", "Housing Instability", "Child Care", "Career Development",
               "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"]

college_emails = {
    "Baruch College": "counseling@baruch.cuny.edu",
    "Borough of Manhattan Community College": "counselingcenter@bmcc.cuny.edu",
    "Bronx Community College": "Personal.Counseling@bcc.cuny.edu",
    "Brooklyn College": "BCPersonalCounseling@gmail.com",
    "City College of New York": "counseling@ccny.cuny.edu",
    "College of Staten Island": "counseling@csi.cuny.edu",
    "CUNY Graduate Center": "wellness@gc.cuny.edu",
    "CUNY School of Law": "mentalwellness@law.cuny.edu",
    "Hostos Community College": "infocounseling@hostos.cuny.edu",
    "Hunter College": "PersonalCounseling@hunter.cuny.edu",
    "John Jay College of Criminal Justice": "intake@jjay.cuny.edu",
    "Kingsborough Community College": "Counseling.Center@kbcc.cuny.edu",
    "LaGuardia Community College": "WellnessCenter@lagcc.cuny.edu",
    "Lehman College": "counseling.center@lehman.cuny.edu",
    "Medgar Evers College": "jjoyner@mec.cuny.edu",
    "New York City College of Technology": "Counseling@citytech.cuny.edu",
    "Queens College": "CounselingServices@qc.cuny.edu",
    "York College": "jchoi@york.cuny.edu"
}

crisis_options = ["Yes", "No"]


def clean_address(address):
    if address:
        address = re.sub(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', '', address)  # Remove phone number
        address = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', '', address)  # Remove email
        address = address.strip()
    return address


def extract_phone_number(text):
    # Regular expression for phone numbers
    phone_pattern = re.compile(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}')
    match = phone_pattern.search(text)
    return match.group() if match else None


def get_counseling_info():
    counseling_data = {}
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(centers_url_string)
        # Get the full HTML content of the page
        content = page.content()
        # Parse the HTML content
        soup = BeautifulSoup(content, 'html.parser')
        # Find all counseling info boxes
        counseling_boxes = soup.find_all(class_='wpb_cuny_text_box')
        for box in counseling_boxes:
            title_element = box.find('h4')
            title = title_element.get_text(strip=True) if title_element else None
            title_link = title_element.find('a')['href'] if title_element and title_element.find('a') else None
            # Extract info
            address_paragraph = box.find('p')
            address = address_paragraph.get_text(strip=True) if address_paragraph else None
            email_link = address_paragraph.find('a', href=True)['href'] if address_paragraph and address_paragraph.find(
                'a', href=True) else None
            # Clean email link
            email_link = email_link.replace('mailto:', '') if email_link else None
            phone_number = extract_phone_number(address) if address else None
            # Clean address text to remove email and phone number
            clean_address_text = clean_address(address)
            if title and email_link:
                for college, email in college_emails.items():
                    # Check if the email matches the one in our pre-constructed dictionary
                    if title and email and email == email_link:
                        # Store the info in the dictionary to be returned
                        counseling_data[college] = {
                            "URL": title_link,
                            "Address": clean_address_text,
                            "Email": email_link,
                            "Number": phone_number
                        }

        browser.close()
    return counseling_data
