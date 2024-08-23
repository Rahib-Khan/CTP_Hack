import streamlit as st
import streamlit_survey as ss
from utilities import aid_options, college_emails, crisis_options, get_counseling_info

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

st.title("Student Aid Questionaire")

counseling_info = get_counseling_info()
colleges = list(college_emails.keys())

def shake(url):
    st.write("You can use the new online career management platform and recruiting system, [Handshake](%s) , to find oppurtnities as a student" % url)

other_resources= "https://www.cuny.edu/academics/current-initiatives/office-of-early-childhood-initiatives/childhood/#1677039908238-a0b79be9-e9c2"
def no():
    st.write("Sorry. Unfortunatley it looks like your College doesn't provide a direct Child Care service that fits your needs. However, there are other programs that may be able to help you.")
    st.write("Please follow this [LINK](%s)" % other_resources)

other_housing_resources = "https://www.nyc.gov/site/hra/help/affordable-housing.page"
def no_housing_resource():
    st.write("Sorry, the specified college doesn't provide direct housing relief. Here are some other programs")
    st.write("Please follow this [LINK](%s)" % other_housing_resources)

def prompt_colleges():
    st.write("What College do you go to?")
    college = survey.radio("College",
                           options=colleges,
                           index=None,
                           label_visibility="collapsed",
                           horizontal=True,
                           )
    return college


def show_alcohol_program():
    college = prompt_colleges()
    alcohol_urls = {
        "Baruch College": "https://echeckup.sdsu.edu/usa/alc/coll/baruch",
        "Borough of Manhattan Community College": "https://echeckup.sdsu.edu/usa/alc/coll/bmcc",
        "Bronx Community College": "https://echeckup.sdsu.edu/usa/alc/coll/bcccuny",
        "Brooklyn College": "https://echeckup.sdsu.edu/usa/alc/coll/brooklyn",
        "City College of New York": "https://echeckup.sdsu.edu/usa/alc/coll/ccny",
        "College of Staten Island": "https://echeckup.sdsu.edu/usa/alc/coll/csicuny",
        "CUNY Graduate Center": "https://echeckup.sdsu.edu/usa/alc/coll/gccuny",
        "CUNY School of Law": "https://echeckup.sdsu.edu/usa/alc/coll/lawcuny",
        "Hostos Community College": "https://echeckup.sdsu.edu/usa/alc/coll/hostos",
        "Hunter College": "https://echeckup.sdsu.edu/usa/alc/coll/hunter",
        "John Jay College of Criminal Justice": "https://echeckup.sdsu.edu/usa/alc/coll/jjay",
        "Kingsborough Community College": "https://echeckup.sdsu.edu/usa/alc/coll/kbcc",
        "LaGuardia Community College": "https://echeckup.sdsu.edu/usa/alc/coll/laguardia",
        "Lehman College": "https://echeckup.sdsu.edu/usa/alc/coll/lehman",
        "Medgar Evers College": "https://echeckup.sdsu.edu/usa/alc/coll/mec",
        "New York City College of Technology": "https://echeckup.sdsu.edu/usa/alc/coll/citytech",
        "Queens College": "https://echeckup.sdsu.edu/usa/alc/coll/qccuny",
        "York College": "https://echeckup.sdsu.edu/usa/alc/coll/yorkcuny"
    }
    if college in alcohol_urls:
        st.write(f"Please visit: [{college}'s alcohol program]({alcohol_urls[college]})")
        st.markdown(f'''
        Program Description:<br>
        The Alcohol eCHECKUP TO GO program provides a comprehensive, personalized 
        assessment to help you understand and manage your alcohol consumption. This program offers:<br>
        - Personalized Feedback: Gain insights into your drinking patterns and identify potential risk factors.<br>
        - Self-Assessment: Evaluate your current alcohol use and its impact on your health and well-being.<br>
        - Goal Setting: Discover strategies and resources to support your goals related to alcohol reduction or abstinence.<br>
        - Local Resources: Access valuable support services and resources available at {college} and within the broader community.
        ''', unsafe_allow_html=True)
    else:
        st.write("No alcohol program URL available for your selected college.")


def show_cannabis_program():
    college = prompt_colleges()
    cannabis_urls = {
        "Baruch College": "https://echeckup.sdsu.edu/usa/mj/coll/baruch",
        "Borough of Manhattan Community College": "https://echeckup.sdsu.edu/usa/mj/coll/bmcc",
        "Bronx Community College": "https://echeckup.sdsu.edu/usa/mj/coll/bcccuny",
        "Brooklyn College": "https://echeckup.sdsu.edu/usa/mj/coll/brooklyn",
        "City College of New York": "https://echeckup.sdsu.edu/usa/mj/coll/ccny",
        "College of Staten Island": "https://echeckup.sdsu.edu/usa/mj/coll/csicuny",
        "CUNY Graduate Center": "https://echeckup.sdsu.edu/usa/mj/coll/gccuny",
        "CUNY School of Law": "https://echeckup.sdsu.edu/usa/mj/coll/lawcuny",
        "Hostos Community College": "https://echeckup.sdsu.edu/usa/mj/coll/hostos",
        "Hunter College": "https://echeckup.sdsu.edu/usa/mj/coll/hunter",
        "John Jay College of Criminal Justice": "https://echeckup.sdsu.edu/usa/mj/coll/jjay",
        "Kingsborough Community College": "https://echeckup.sdsu.edu/usa/mj/coll/kbcc",
        "LaGuardia Community College": "https://echeckup.sdsu.edu/usa/mj/coll/laguardia",
        "Lehman College": "https://echeckup.sdsu.edu/usa/mj/coll/lehman",
        "Medgar Evers College": "https://echeckup.sdsu.edu/usa/mj/coll/mec",
        "New York City College of Technology": "https://echeckup.sdsu.edu/usa/mj/coll/citytech",
        "Queens College": "https://echeckup.sdsu.edu/usa/mj/coll/qccuny",
        "York College": "https://echeckup.sdsu.edu/usa/mj/coll/yorkcuny"
    }
    if college in cannabis_urls:
        st.write(f"Please visit: [{college}'s cannabis program]({cannabis_urls[college]})")
        st.markdown(f'''
        Program Description:<br>
        The Cannabis eCHECKUP TO GO program provides a comprehensive, personalized 
        assessment to help you understand and manage your cannabis use. This program includes:<br>
        - Personalized Feedback: Gain insights into your cannabis use patterns and identify potential risk factors.<br>
        - Self-Assessment: Evaluate your current cannabis habits and their impact on your health and well-being.<br>
        - Goal Setting: Discover strategies and resources to support your goals related to cannabis use reduction or cessation.<br>
        - Local Resources: Access valuable support services and resources available at {college} and within the broader community.
        ''', unsafe_allow_html=True)
    else:
        st.write("No cannabis program URL available for your selected college.")


def show_nicotine_program():
    college = prompt_colleges()
    nicotine_urls = {
        "Baruch College": "https://echeckup.sdsu.edu/usa/nicotine/coll/baruch",
        "Borough of Manhattan Community College": "https://echeckup.sdsu.edu/usa/nicotine/coll/bmcc",
        "Bronx Community College": "https://echeckup.sdsu.edu/usa/nicotine/coll/bcccuny",
        "Brooklyn College": "https://echeckup.sdsu.edu/usa/nicotine/coll/brooklyn",
        "City College of New York": "https://echeckup.sdsu.edu/usa/nicotine/coll/ccny",
        "College of Staten Island": "https://echeckup.sdsu.edu/usa/nicotine/coll/csicuny",
        "CUNY Graduate Center": "https://echeckup.sdsu.edu/usa/nicotine/coll/gccuny",
        "CUNY School of Law": "https://echeckup.sdsu.edu/usa/nicotine/coll/lawcuny",
        "Hostos Community College": "https://echeckup.sdsu.edu/usa/nicotine/coll/hostos",
        "Hunter College": "https://echeckup.sdsu.edu/usa/nicotine/coll/hunter",
        "John Jay College of Criminal Justice": "https://echeckup.sdsu.edu/usa/nicotine/coll/jjay",
        "Kingsborough Community College": "https://echeckup.sdsu.edu/usa/nicotine/coll/kbcc",
        "LaGuardia Community College": "https://echeckup.sdsu.edu/usa/nicotine/coll/laguardia",
        "Lehman College": "https://echeckup.sdsu.edu/usa/nicotine/coll/lehman",
        "Medgar Evers College": "https://echeckup.sdsu.edu/usa/nicotine/coll/mec",
        "New York City College of Technology": "https://echeckup.sdsu.edu/usa/nicotine/coll/citytech",
        "Queens College": "https://echeckup.sdsu.edu/usa/nicotine/coll/qccuny",
        "York College": "https://echeckup.sdsu.edu/usa/nicotine/coll/yorkcuny"
    }
    if college in nicotine_urls:
        st.write(f"Please visit: [{college}'s nicotine program]({nicotine_urls[college]})")
        st.markdown(f'''
        Program Description:<br>
        The Nicotine eCHECKUP TO GO program offers a comprehensive, personalized 
        assessment to help you understand and manage your nicotine use. This program provides:<br>
        - Personalized Feedback: Gain insights into your nicotine use patterns and identify potential risk factors.<br>
        - Self-Assessment: Evaluate your current nicotine habits and their impact on your health and well-being.<br>
        - Goal Setting: Discover strategies and resources to support your goals related to nicotine use reduction or cessation.<br>
        - Local Resources: Access valuable support services and resources available at {college} and within the broader community.
        ''', unsafe_allow_html=True)
    else:
        st.write("No nicotine program URL available for your selected college.")
def mental_health_survey():
    if aid == "Mental Health":
        st.write("Are you seeking immediate crisis intervention?")
        crisis_status = survey.radio("Crisis Intervention",
                                     options=crisis_options,
                                     index=None,
                                     label_visibility="collapsed",
                                     horizontal=True
                                     )
        if crisis_status == 'Yes':
            st.write("Please seek immediate help by reaching out to CUNY's crisis text line and texting 'CUNY' to "
                     "741741.")
        elif crisis_status == 'No':
            st.write("What CUNY college are you currently attending?")
            college = survey.radio("College",
                                   options=colleges,
                                   index=None,
                                   label_visibility="collapsed",
                                   horizontal=True,
                                   )
            if college:
                st.write(f"Listed below is {college}'s counseling center which provides information about recieving "
                         f"essential mental health services including therapy, group support, self-help resources, "
                         f"and more!")
                center_url = counseling_info[college]['URL']
                address = counseling_info[college]['Address']
                contact_number = counseling_info[college]['Number']
                contact_email = counseling_info[college]['Email']
                st.write(f"[{college}'s Counseling Center Website](%s)" % center_url)
                st.write(f"Located at: {address}")
                st.write(f"Center Contact Number: {contact_number}")
                st.write(f"Center Contact Email: {contact_email}")
                print(colleges)

st.write("What Type of Aid Are you looking for?")
aid = survey.radio("Issues",
        options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
        index= None,
        label_visibility="collapsed",
        horizontal=True,
    )

if aid == "Addiction Services":
    st.write('Which program are you seeking?')
    program = survey.radio("service",
                           options=["Alcohol Program", "Cannabis Program", "Nicotine Program"],
                           index=None,
                           label_visibility="collapsed",
                           horizontal=True,
                           )
    if program == 'Alcohol Program':
        show_alcohol_program()
    elif program == 'Cannabis Program':
        show_cannabis_program()
    elif program == 'Nicotine Program':
        show_nicotine_program()
#Child Care Questionaire
if aid == "Child Care":
        st.write("What College do you go to?")
        college = survey.radio("College",
                options = [
        "Baruch College",
        "Borough of Manhattan Community College",
        "Bronx Community College",
        "Brooklyn College",
        "City College of New York",
        "College of Staten Island",
        "CUNY Graduate Center",
        "CUNY School of Law",
        "Hostos Community College",
        "Hunter College",
        "John Jay College of Criminal Justice",
        "Kingsborough Community College",
        "LaGuardia Community College",
        "Lehman College",
        "Medgar Evers College",
        "New York City College of Technology",
        "Queens College",
        "York College", 
        "Other"
    ]
    ,
                index=None,
                label_visibility="hidden",
                horizontal=True,
            )

        if college == "Baruch College":
            st.write("Is your child between the ages of 4 Months and 5 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://studentaffairs.baruch.cuny.edu/early-learning-center/"
                Location_url = "https://www.google.com/maps/place/1+Bernard+Baruch+Way,+New+York,+NY+10010/@40.740181,-73.9841493,18.42z/data=!4m5!3m4!1s0x89c259a752b00719:0xf5c500d480255408!8m2!3d40.74016!4d-73.9833505?shorturl=1"
                st.write("The Child Care Center at Baruch College is Called the [Early Learning Center](%s)" % Center_url)
                st.write("Located at [Box G-1063, 1 Bernard Baruch Way, New York, NY 10010](%s)" % Location_url)
                st.write("Center Numbers: 212-387-1420 or 212-387-1421 | C: 646-261-2451")
                st.write("The Center Director is Lorraine Mondesir")

            elif confirm == "No":
                no()

        elif college == "Borough of Manhattan Community College":
            st.write("Is your child between the ages of 3 Months and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.bmcc.cuny.edu/student-affairs/ecc/"
                Location_url = "https://goo.gl/maps/tUPqPnPtAGsjohhB8"
                st.write("The Child Care Center at Borough of Manhattan Community College is Called the [Borough of Manhattan Community College Early Childhood Center Inc](%s)" % Center_url)
                st.write("Located at [Room N375, 199 Chambers Street, New York, NY 10007](%s)" % Location_url)
                st.write("Center Numbers: 212-220-8250 or 212-220-8251")
                st.write("The Center Director is Cecilia Scott-Croff")
                st.write("Hours: Mon to Thu 7:45AM - 9PM | Fri 7:45AM - 6PM | Sat 7:45AM - 6PM")

            elif confirm == "No":
                no()

        elif college == "Bronx Community College":
            st.write("Is your child between the ages of 6 weeks and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.bcc.cuny.edu/campus-resources/early-childhood-center/"
                Location_url = "https://goo.gl/maps/gSGmYBosNAqwvkof9"
                st.write("The Child Care Center at Bronx Community College is Called the [Child Development Center](%s)" % Center_url)
                st.write("Located at [2155 University Avenue Bronx, NY 10453](%s)" % Location_url)
                st.write("Center Number: 718-289-5461")
                st.write("The Center Director is Jitinder Walia")
                st.write("Hours: Pre-School: Mon to Thu 7:30AM to 8PM | Fri 7:30AM-5:30PM) (Infant/Toddlers: Mon to Thu 8AM-4PM) (School Age: Mon to Thu 3PM-8PM")

            elif confirm == "No":
                no()
                
        elif college == "Brooklyn College":
            st.write("Is your child between the ages of 4 Months and 5 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.brooklyn.edu/dosa/student-support-services/csds/"
                Location_url = "https://goo.gl/maps/HJiEHpifaEZhvk7b7"
                st.write("The Child Care Center at Brooklyn College is Called the [The Early Childhood Center Programs](%s)" % Center_url)
                st.write("Located at [1604 James Hall, Bedford Avenue & Avenue H, Brooklyn, NY 11210](%s)" % Location_url)
                st.write("Center Number: 718-951-5431")
                st.write("The Center Director is Kaity Kapetan")
                st.write("Hours: Mon to Fri 8:30AM-4:30PM")

            elif confirm == "No":
                no()
                
        elif college == "City College of New York":
            st.write("Is your child between the ages of 4 Months and 5 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.ccny.cuny.edu/cdc"
                Location_url = "https://goo.gl/maps/nwtXcwpfDy87TLAG7"
                st.write("The Child Care Center at City College of New York is Called the [Campus Child Development Center](%s)" % Center_url)
                st.write("Located at [Schiff House, 119 Convent Avenue, New York, NY 10031](%s)" % Location_url)
                st.write("Center Numbers: 212-650-7679")
                st.write("The Center Director is Chanda Huston")
                st.write("Hours: Mon to Fri 7:30AM to 5:30PM")

            elif confirm == "No":
                no()
                
        elif college == "College of Staten Island":
            st.write("Is your child between the ages of 6 Months and 9 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.csi.cuny.edu/campus-life/student-services/childrens-center"
                Location_url = "https://goo.gl/maps/3F2v6rcntjk5mvTJ9"
                st.write("The Child Care Center at College of Staten Island is Called the [The Children's Center](%s)" % Center_url)
                st.write("Located at [2R-104, 2800 Victory Boulevard, Staten Island, NY 10314](%s)" % Location_url)
                st.write("Center Numbers: 718-982-3190")
                st.write("The Center Director is Margaret Rooney")
                st.write("Hours: Mon to Fri 7AM - 6:30PM")

            elif confirm == "No":
                no()

        elif college == "CUNY Graduate Center":
            st.write("Is your child between the ages of 2 Years and 5 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.gc.cuny.edu/Prospective-Current-Students/Student-Life/Resources/Child-Development-and-Learning-Center"
                Location_url = "https://goo.gl/maps/ypTJ2CiG1UUX2koQ9"
                st.write("The Child Care Center at CUNY Graduate Center is Called the [The Child Development and Learning Center](%s)" % Center_url)
                st.write("Located at [Suite 3201, 365 Fifth Avenue, New York, NY 10016](%s)" % Location_url)
                st.write("Center Numbers: 212-817-7033")
                st.write("The Center Director is Molly Polin")
                st.write("Hours:  Mon to Thu 9AM to 5PM | Fri 9AM to 4PM")

            elif confirm == "No":
                no()

        elif college == "CUNY School of Law":
            st.write("Is your child between the ages of 6 Months and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.laguardia.edu/eclc/"
                Location_url = "https://goo.gl/maps/Tjm6vpu27PFm84X86"
                st.write("The Child Care Center for CUNY School of Law is shared with LaGuardia Community College and is Called the [Early Childhood Learning Center Programs](%s)" % Center_url)
                st.write("Located at [Room MB09, 31-10 Thomson Avenue, Long Island City, NY 11101](%s)" % Location_url)
                st.write("Center Numbers: 718-482-5295")
                st.write("The Center Director is Sonya Evariste")
                st.write("Hours: Mon to Fri 7:50AM to 5PM | Sat 8AM to 3PM (During Spring & Fall only)")

            elif confirm == "No":
                no()

        elif college == "Hostos Community College":
            st.write("Is your child between the ages of 6 Weeks and 5 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.hostos.cuny.edu/Administrative-Offices/SDEM/Children-s-Center"
                Location_url = "https://goo.gl/maps/jtGvpVyegw7R7hix5"
                st.write("The Child Care Center for Hostos Community College is Called the [Children's Center](%s)" % Center_url)
                st.write("Located at [475 Grand Concourse, Bronx, NY 10451](%s)" % Location_url)
                st.write("Center Numbers: 718-518-4176")
                st.write("The Center Director is Catherine Garcia-Bou")
                st.write("Hours: Mon to Fri 7:45AM to 5PM")

            elif confirm == "No":
                no()
            
        elif college == "Hunter College":
            st.write("Is your child between the ages of 2 Years and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "http://www.hunter.cuny.edu/studentservices/clc"
                Location_url = "https://goo.gl/maps/Czxt3nUmrkzNc3xd7"
                st.write("The Child Care Center for Hunter College is Called the [The Children's Learning Center](%s)" % Center_url)
                st.write("Located at [Room 207N, 695 Park Avenue, New York, NY 10065](%s)" % Location_url)
                st.write("Center Numbers: 212-772-4066")
                st.write("The Center Director is Rittela F Letellier")
                st.write("Hours: Mon to Thu 8AM to 7PM | Fri 8AM to 3PM")

            elif confirm == "No":
                no()

        elif college == "John Jay College of Criminal Justice":
            st.write("Is your child between the ages of 6 Months and 5 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "http://www.jjay.cuny.edu/childrens-center"
                Location_url = "https://goo.gl/maps/aGRu9i3p2o2LXF9L6"
                st.write("The Child Care Center for John Jay College of Criminal Justice is Called the [Children's Center](%s)" % Center_url)
                st.write("Located at [860 11th Avenue, New York, NY 10019](%s)" % Location_url)
                st.write("Center Numbers: 212-393-6438")
                st.write("The Center Director is Linda Soleyn")
                st.write("Hours: Mon to Thu 7:30AM to 6PM | Fri-7:30AM to 3:30PM")

            elif confirm == "No":
                no()

        elif college == "Kingsborough Community College":
            st.write("Is your child between the ages of 2 Years & 10 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.kbcc.cuny.edu/childcenter/Homepage.html"
                Location_url = "https://goo.gl/maps/bt3mb7yHX73LE8hg8"
                st.write("The Child Care Center for Kingsborough Community College is Called the [Child Development Center](%s)" % Center_url)
                st.write("Located at [Room V105, 2001 Oriental Blvd. Brooklyn, NY 11235](%s)" % Location_url)
                st.write("Center Numbers: 718-368-5439")
                st.write("The Center Director is Latasha Collins")
                st.write("Hours: Mon to Thu 7:30AM to 5:30PM | Fri 7:30AM-4:30PM")

            elif confirm == "No":
                no()

        elif college == "LaGuardia Community College":
            st.write("Is your child between the ages of 6 Months and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.laguardia.edu/eclc/"
                Location_url = "https://goo.gl/maps/Tjm6vpu27PFm84X86"
                st.write("The Child Care Center for LaGuardia Community College is Called the [Early Childhood Learning Center Programs](%s)" % Center_url)
                st.write("Located at [Room MB09, 31-10 Thomson Avenue, Long Island City, NY 11101](%s)" % Location_url)
                st.write("Center Numbers: 718-482-5295")
                st.write("The Center Director is Sonya Evariste")
                st.write("Hours: Mon to Fri 7:50AM to 5PM | Sat 8AM to 3PM (During Spring & Fall only)")

            elif confirm == "No":
                no()

        elif college == "Lehman College":
            st.write("Is your child between the ages of 2 Years and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "http://www.lehman.edu/child-care-center/"
                Location_url = "https://goo.gl/maps/4D4VScMSyuTpQ5rR9"
                st.write("The Child Care Center for Lehman College is Called the [Child Care Center](%s)" % Center_url)
                st.write("Located at [2870 Goulden Avenue, Bronx, NY 10468](%s)" % Location_url)
                st.write("Center Numbers: 718-960-7436")
                st.write("The Center Director is Jaci Maurer")
                st.write("Hours: Mon to Thu 7:30AM to 5:30PM | Fri 7:30AM to 5PM | For Preschool & School Age programs Mon to Thu 3PM to 9:30PM")

            elif confirm == "No":
                no()

        elif college == "Medgar Evers College":
            st.write("Is your child between the ages of 2 Years and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Location_url = "https://goo.gl/maps/DPL54MTpNKBrXMjdA"
                st.write("The Child Care Center for Medgar Evers College is Called the Child Care Center")
                st.write("Located at [Room C103, 1150 Carroll Street, Brooklyn, NY 11225](%s)" % Location_url)
                st.write("Center Numbers: 718-270-6018")
                st.write("The Center Director is Juanita Crafton")
                st.write("Hours: Mon to Thu 7:45AM to 10PM | Fri 7:45AM to 3PM")

            elif confirm == "No":
                no()

        elif college == "New York City College of Technology":
            st.write("Is your child between the ages of 2 Years and 12 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "http://www.citytech.cuny.edu/occ/"
                Location_url = "https://goo.gl/maps/woyzZxdHkoYQGST3A"
                st.write("The Child Care Center for New York City College of Technology is Called the [Child Care Center](%s)" % Center_url)
                st.write("Located at [Room G-309 and Room NG14, 300 Jay Street, Brooklyn, NY 11201](%s)" % Location_url)
                st.write("Center Numbers: 718-260-5192")
                st.write("The Center Director is Elizabeth Leone")
                st.write("Hours: Mon to Fri 7:30AM to 9:30PM | Sat 8AM to 4:30PM")

            elif confirm == "No":
                no()

        elif college == "Queens College":
            st.write("Is your child between the ages of 30 Months and 10 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url = "https://www.qc.cuny.edu/chdc/"
                Location_url = "https://goo.gl/maps/EH5gWApauWWfSW5j7"
                st.write("The Child Care Center for Queens College is Called the [Child Development Center](%s)" % Center_url)
                st.write("Located at [Room 245, Kiely Hall, 65-30 Kissena Blvd, Flushing, NY 11367](%s)" % Location_url)
                st.write("Center Numbers: 718-997-5885")
                st.write("The Center Director is Eric Urevich")
                st.write("Hours: Mon to Thu 9AM-5PM")

            elif confirm == "No":
                no()

        elif college == "York College":
            st.write("Is your child between the ages of 6 Months and 10 Years?")
            confirm = survey.radio(
                    "Confirm",
                    options=["Yes", "No"],
                    index= None,
                    label_visibility="collapsed",
                    horizontal=True,
                )
            if confirm == "Yes":
                Center_url= "https://www.york.cuny.edu/student-development/child-and-family-center"
                Location_url = "https://goo.gl/maps/S78GDgCWmeMSdBVcA"
                st.write("The Child Care Center for York College is Called the [York College Child and Family Center, Inc.](%s)" % Center_url)
                st.write("Located at [94-12 160th street, Jamaica, New York 11451](%s)" % Location_url)
                st.write("Center Numbers:/n 718-262-2930")
                st.write("The Center Director is Charlene Dertinger")
                st.write("Hours: Mon to Thu 8AM to 6PM | Fri 8AM to 4PM")

            elif confirm == "No":
                no()

        elif college == "Other":
            no()
#Career Development Questionaire
if aid == "Career Development":
    st.write("Would you like to be connected to your Campus Career Center or have information on CUNY Programs?")
    check1 = survey.checkbox("Campus Career Center")
    check2 = survey.checkbox("CUNY Program")

    if check1:
        st.write("What College do you go to?")
        college = survey.radio("College",
                    options = [
            "Baruch College",
            "Borough of Manhattan Community College",
            "Bronx Community College",
            "Brooklyn College",
            "City College of New York",
            "College of Staten Island",
            "CUNY School of Labor and Urban Studies",
            "CUNY School of Professional Studies",
            "CUNY School of Public Health",
            "Guttman Community College",
            "Hostos Community College",
            "Hunter College",
            "John Jay College of Criminal Justice",
            "Kingsborough Community College",
            "LaGuardia Community College",
            "Lehman College",
            "Macaulay Honors College",
            "Medgar Evers College",
            "New York City College of Technology",
            "Queens College",
            "Queensborough Community College",
            "York College"
        ]
        ,
                    index=None,
                    label_visibility="hidden",
                    horizontal=True,
                )

        if college == "Baruch College":
            st.write("Which School of Baruch are you apart of?")
            baruch = survey.radio("Baruch Schools",
                    options=["Baruch Undergraduate","Austin W. Marxe School of Public and International Affairs", "Weissman School of Arts & Sciences", "Zicklin School of Business"],
                    index= None,
                    label_visibility="visible",
                    horizontal=False)
            if baruch == "Baruch Undergraduate":
                url = "https://studentaffairs.baruch.cuny.edu/starr-career-development-center/"
                st.write("The Career Center at Baruch College is Called the [Starr Career Development Center](%s)" % url)
                st.write("The Center is located at 1 Bernard Baruch Way Box B2150 New York, NY 10010")
                st.write("Center Number: 646-312-4670")
                st.write("You can email them at Careerdc@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")
            elif baruch == "Austin W. Marxe School of Public and International Affairs":
                url = "http://www.baruch.cuny.edu/mspia/career-services/"
                st.write("The Career Center at Baruch's Austin W. Marxe School of Public and International Affairs is Called the [Marxe Graduate Career Services](%s)" % url)
                st.write("The Center is located at 1 Bernard Baruch Way Box D0901 New York, NY 10010")
                st.write("Center Number: 646-660-6798")
                st.write("You can email them at mspia.careerservices@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")
            elif baruch == "Weissman School of Arts & Sciences":
                url = "http://www.baruch.cuny.edu/wsas/graduatecareers/"
                st.write("The Career Center at Baruch's Weissman School of Arts & Sciences is Called the [Weissman Graduate Career Services](%s)" % url)
                st.write("The Center is located at 1 Bernard Baruch Way Box B7-180 New York, NY 10010")
                st.write("Center Number: 646-312-3887")
                st.write("You can email them at mspia.careerservices@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")
            elif baruch == "Zicklin School of Business":
                url = "https://zicklin.baruch.cuny.edu/experience-zicklin/student-experience/gcmc-graduate-career-management-center/"
                st.write("The Career Center at Baruch's Zicklin School of Business is Called the [Graduate Career Management Center](%s)" % url)
                st.write("The Center is located at 151 East 25th street Box H-820 New York, NY 10010")
                st.write("Center Number: 646-312-1330")
                st.write("You can email them at zicklin.gcmc@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")

        elif college == "Borough of Manhattan Community College":
            url = "http://www.bmcc.cuny.edu/career/"
            st.write("The Career Center at Borough of Manhattan Community College is Called the [Center for Career Development](%s)" % url)
            st.write("The Center is located at 199 Chambers Street Room S-342 New York, NY 10007")
            st.write("Center Number: 212-220-8170")
            st.write("You can email them at career@bmcc.cuny.edu")
            shake("https://bmcc.joinhandshake.com/login?ref=app-domain")
        elif college == "Bronx Community College":
            url = "http://www.bcc.cuny.edu/services/career-development/"
            st.write("The Career Center at Bronx Community College is Called the [The Office of Career Development](%s)" % url)
            st.write("The Center is located at Snow Hall, First Floor 2155 University Avenue Bronx, NY 10453")
            st.write("Center Number: 718-220-7546")
            st.write("You can email them at Careerdevelopment@bcc.cuny.edu ")
            shake("https://bcccuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Brooklyn College":
            url = "https://www.brooklyn.edu/web/academics/centers/magner.php"
            st.write("The Career Center at Brooklyn College is Called the [Magner Career Center](%s)" % url)
            st.write("The Center is located at 2900 Bedford Ave. 1303 James Hall Brooklyn, NY 11210")
            st.write("Center Number: 718-951-5696")
            st.write("You can email them at careernews@brooklyn.cuny.edu ")
            shake("https://brooklyncuny.joinhandshake.com/login?ref=app-domain")
        elif college == "City College of New York":
            url = "https://www.ccny.cuny.edu/cpdi"
            st.write("The Career Center at City College of New York is Called the [Career and Professional Development Institute](%s)" % url)
            st.write("The Center is located at 138th Street at Convent Avenue NAC Building, 1st Fl, Room 116 New York, NY 10031")
            st.write("Center Number: 212-650-5327")
            st.write("You can email them at cpdi@ccny.cuny.edu ")
            shake("https://app.joinhandshake.com/login")
        elif college == "College of Staten Island":
            url = "http://www.csi.cuny.edu/career/"
            st.write("The Career Center at College of Staten Island is Called the [Center for Career and Professional Development](%s)" % url)
            st.write("The Center is located at 2800 Victory Boulevard Building 1A, Room 105 Staten Island, NY 10314")
            st.write("Center Number: 718-982 2300")
            st.write("You can email them at careers@csi.cuny.edu")
            shake("https://csicuny.joinhandshake.com/login?ref=app-domain")
        elif college == "CUNY School of Labor and Urban Studies":
            url = "https://slu.cuny.edu/academic-affairs/student-affairs/student-services/career-services/"
            st.write("The Career Center at CUNY School of Labor and Urban Studies is Called the [Career and Professional Development Center](%s)" % url)
            st.write("The Center is located at 25 W 43rd Street, 18th floor New York, NY 10036")
            st.write("Center Number: 646-313-8339")
            st.write("You can email them at careerservices@slu.cuny.edu")
            shake("https://slucuny.joinhandshake.com/login?ref=app-domain")
        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/student-services/career-services"
            st.write("The Career Center at CUNY School of Professional Studies is Called the [Office of Career Services](%s)" % url)
            st.write("The Center is located at 119 West 31st Street, 4th floor New York, NY 10001")
            st.write("Center Number: 646-664-8618")
            st.write("You can email them at career.services@sps.cuny.edu")
            shake("https://app.joinhandshake.com/login")
        elif college == "CUNY School of Public Health":
            url = "http://sph.cuny.edu/student-services/office-of-career-services/"
            st.write("The Career Center at CUNY School of Public Health is Called the [Office of Career Services](%s)" % url)
            st.write("The Center is located at 55 West 125th street, 5th floor New York, NY 10027")
            st.write("Center Number: 646-364-9644")
            st.write("You can email them at careerservices@sph.cuny.edu")
            shake("https://sphcuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Guttman Community College":
            url = "https://guttman.cuny.edu/"
            st.write("The Career Center at Guttman Community College is Called the [Center for Career Preparation & Partnerships](%s)" % url)
            st.write("The Center is located at 50 W. 40th St. New York, NY 10018")
            st.write("Center Number: 646-313-8066")
            st.write("You can email them at cpartnerships@guttman.edu")
            shake("https://guttman.joinhandshake.com/login?ref=app-domain")
        elif college == "Hostos Community College":
            url = "http://www.hostos.cuny.edu/cso/"
            st.write("The Career Center at Hostos Community College is Called the [Career Services](%s)" % url)
            st.write("The Center is located at Savoy Building, D210 Bronx, NY 10451")
            st.write("Center Number: 718-518-4468")
            st.write("You can email them at careerservices@hostos.cuny.edu")
            shake("https://hostos.joinhandshake.com/login?ref=app-domain")
        elif college == "Hunter College":
            url = "http://www.hunter.cuny.edu/studentservices/cds"
            st.write("The Career Center at Hunter College is Called the [Career Development Services](%s)" % url)
            st.write("The Center is located at 695 Park Avenue Room 805 E New York, NY 10021")
            st.write("Center Number: 212-772-4850")
            st.write("You can email them at career@hunter.cuny.edu")
            shake("https://huntercuny.joinhandshake.com/login?ref=app-domain")
        elif college == "John Jay College of Criminal Justice":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/career-services/campus-career-centers/#:~:text=John%20Jay%20College%20of%20Criminal%20Justice"
            st.write("The Career Center at John Jay College of Criminal Justice is Called the [Center for Career and Professional Development](%s)" % url)
            st.write("The Center is located at 524 West 59th StreetNew York, NY 10019")
            st.write("Center Number: 212-237-8754")
            st.write("You can email them at careers@jjay.cuny.edu")
            shake("https://jjaycuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Kingsborough Community College":
            url = "http://www.kingsborough.edu/career/"
            st.write("The Career Center at Kingsborough Community College is Called the [Center for Career Development & Experiential Learning](%s)" % url)
            st.write("The Center is located at Room C201 2001 Oriental Boulevard Brooklyn, NY 11235")
            st.write("Center Number: 718-368-5115")
            st.write("You can email them at careerdevelopment@kbcc.cuny.edu")
            shake("https://kbcc-cuny.joinhandshake.com/login?ref=app-domain")
        elif college == "LaGuardia Community College":
            url = "http://www.laguardia.cuny.edu/careerservices/"
            st.write("The Career Center at LaGuardia Community College is Called the [Center for Career & Professional Development](%s)" % url)
            st.write("The Center is located at 31-10 Thomson Avenue Room B114 Long Island City, NY 11101")
            st.write("Center Number: 718-482-5235")
            st.write("You can email them at career@lagcc.cuny.edu")
            shake("https://app.joinhandshake.com/login")
        elif college == "Lehman College":
            url = "http://www.lehman.edu/career-services/"
            st.write("The Career Center at Lehman College is Called the [Career Exploration & Development Center](%s)" % url)
            st.write("The Center is located at 250 Bedford Park Blvd. West, Shuster Hall, Room 254 Shuster Hall, Room 254 Bronx, NY 10468")
            st.write("Center Number: 718-960-8366")
            st.write("You can email them at career.services@lehman.cuny.edu")
            shake("https://lehmancuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Macaulay Honors College":
            url = "https://macaulay.cuny.edu/after-macaulay/career-development/"
            st.write("The Career Center at Macaulay Honors College is Called the [Office of Career Development](%s)" % url)
            st.write("The Center is located at 35 West 67th Street New York, NY 10023")
            st.write("Center Number: 212-729-2947")
            st.write("You can email them at internships@mhc.cuny.edu")
            shake("https://mhc.joinhandshake.com/login?ref=app-domain")
        elif college == "Medgar Evers College":
            url = "https://ares.mec.cuny.edu/student-affairs/career-management-services/"
            st.write("The Career Center at Medgar Evers College is Called the [Office of Career Management Services](%s)" % url)
            st.write("The Center is located at Student Services Building1637 Bedford Avenue, Room S302 Brooklyn, NY 11225")
            st.write("Center Number: 718-270-6055")
            st.write("You can email them at CareerServices@mec.cuny.edu")
            shake("https://app.joinhandshake.com/login")
        elif college == "New York City College of Technology":
            url = "http://www.citytech.cuny.edu/pdc/"
            st.write("The Career Center at New York City College of Technology is Called the [Professional Development Center](%s)" % url)
            st.write("The Center is located at Room L-114 250 Jay Street Brooklyn, New York 11201")
            st.write("Center Number: 718-260-5050")
            st.write("You can email them at pdc@citytech.cuny.edu")
            shake("https://citytech.joinhandshake.com/login?ref=app-domain")
        elif college == "Queens College":
            url = "https://www.qc.cuny.edu/academics/cei/"
            st.write("The Career Center at Queens College is Called the [Center for Career Engagement and Internships](%s)" % url)
            st.write("The Center is located at 65-30 Kissena Boulevard Frese Hall, Room 213 Flushing, NY 11367")
            st.write("Center Number: 718-997-4465")
            st.write("You can email them at qc_career@qc.cuny.edu")
            shake("https://qc.joinhandshake.com/login?ref=app-domain")
        elif college == "Queensborough Community College":
            url = "http://www.qcc.cuny.edu/careerservices/"
            st.write("The Career Center at Queensborough Community College is Called the [Career Services](%s)" % url)
            st.write("The Center is located at Library Building, L-429222-05, 56th Avenue Bayside, NY 11364")
            st.write("Center Number: 718-631-6297")
            st.write("You can email them at careerservices@qcc.cuny.edu")
            shake("https://cunyqcc.joinhandshake.com/login?ref=app-domain")
        elif college == "York College":
            url = "http://york.cuny.edu/student-development/career-services"
            st.write("The Career Center at York College is Called the [The Office of Career Services](%s)" % url)
            st.write("The Center is located at 94-20 Guy Brewer Boulevard Room #3E03 Jamaica, NY 11451")
            st.write("Center Number: 718-262-2282")
            st.write("You can email them at career@york.cuny.edu")
            shake("https://app.joinhandshake.com/login")
    
    if check2:
        url = "https://www.cuny.edu/about/administration/offices/ocip/"
        st.write("Please follow this [link](%s) to be redirected to a plethora of CUNY Career Programs" % url)

#Housing Instability Questionnaires
if aid == "Housing Instability":
    confirm1 = survey.checkbox("NYC Housing Programs")
    confirm2 = survey.checkbox("CUNY Programs")
    
    if confirm1:
        nyc_housing_url = "https://www.healthycuny.org/resources-housing-homelessness"
        st.write("Check out this URL(%s)" % nyc_housing_url)
    
    if confirm2:
        st.write("What College do you go to?")
        college = survey.radio("College",
                    options = [
            "Baruch College",
            "Borough of Manhattan Community College",
            "Bronx Community College",
            "Brooklyn College",
            "City College of New York",
            "College of Staten Island",
            "CUNY Graduate Center",
            "CUNY School of Law",
            "Hostos Community College",
            "Hunter College",
            "John Jay College of Criminal Justice",
            "Kingsborough Community College",
            "LaGuardia Community College",
            "Lehman College",
            "Medgar Evers College",
            "New York City College of Technology",
            "Queens College",
            "York College", 
            "Other"
                    ]
        ,
                    index=None,
                    label_visibility="hidden",
                    horizontal=True,
                )
        if college == "Baruch College":
            baruch_housing_url = "https://studentaffairs.baruch.cuny.edu/residence-life/"
            baruch_offcampus_url = "https://studentaffairs.baruch.cuny.edu/residence-life/off-campus-housing/"
            st.write("Baruch on-campus housing](%s)" % baruch_housing_url)
            st.write("Baruch off-campus housing](%s)" % baruch_offcampus_url)

        elif college == "Borough of Manhattan Community College":
            bmcc_shelter_url = "https://www.bmcc.cuny.edu/student-affairs/arc/housing-options/nyc-area-shelters/"
            st.write("BMCC does not have any dorms or housing. Check out these resources](%s)" % bmcc_shelter_url)
            no_housing_resource()
        
        elif college == "Bronx Community College":
            bronx_ehs_url = "https://www.studenthousing.org/and/bronxcc/"
            bronx_shelter_url = "https://www.bcc.cuny.edu/campus-resources/access-resource-center/housing-options/"
            st.write("Check out Educational Housing Services (EHS)](%s)" % bronx_ehs_url)
            st.write("Check out these additional resources](%s)" % bronx_shelter_url)
        
        elif college == "Brooklyn College":
            brooklyn_ehs_url =  "https://www.studenthousing.org/and/brooklyncollege/"
            brooklyn_shelter_url = "https://www.brooklyn.edu/student-life/living-in-brooklyn/"
            st.write("Check out some Educational Housing Services(EHS)](%s)" % brooklyn_ehs_url)
            st.write("Brooklyn College doesn't have any doorms. Check out this resource instead](%s)" % brooklyn_shelter_url)

        elif college == "City College of New York":
            ccny_housing_url =" https://www.ccny.cuny.edu/housing?srsltid=AfmBOopOfMSgvvxkqjrV3OL5cXuzTapZULRARmzgar673YivFD8sWHhK"
            ccny_offcampus_url = "https://www.ccny.cuny.edu/studentaffairs/campus-resources?srsltid=AfmBOoqasS4_TkDJtmvHs-G0xd6bD-5gInVHWU_uyZUccqzxOfPlliel"
            st.write("Check out some housing on CCNY](%s)" % ccny_housing_url)
            st.write("Check out some off-campus housing resources](%s)" % ccny_offcampus_url )
        
        elif college == "College of Staten Island":
            staten_housing_url = "https://www.csi.cuny.edu/admissions/new-student-guide/undergraduate-guide/student-housing-information"
            staten_housing_assist = "https://www.csi.cuny.edu/admissions/paying-college/financial-aid/student-financial-aid-and-campus-housing-csi#:~:text=Students%20can%20use%20funds%20from,be%20used%20to%20pay%20tuition"
            st.write("Check out on-campus housing](%s)" % staten_housing_url)
            st.write("Check out some housing assistance at CSI](%s)" % staten_housing_assist)

        elif college == "CUNY Graduate Center":
            gc_housing_url = "https://www.gc.cuny.edu/student-life/living-and-learning-nyc/housing"
            gc_grant_url = "https://www.gc.cuny.edu/fellowships-and-financial-aid"
            st.write("Check out housing at CUNY GC](%s)" % gc_housing_url)
            st.write("Check out the student emergency grant at CUNY GC](%s)" % gc_grant_url)
        
        elif college == "CUNY School of Law":
            law_housing_url = "https://law.catalog.cuny.edu/section-x-student-services/housing"
            st.write("This is the housing financial aid CUNY School of Law offers](%s)" % law_housing_url)
            no_housing_resource()

        elif college == "Hostos Community College":
            hostos_housing_url = "https://hostos.catalog.cuny.edu/student-support-services/single-stop"
            st.write("Here are some housing assitance and more aid at Hostos Community College](%s)" % hostos_housing_url)
        
        elif college == "Hunter College":
            hunter_assistance_url = "https://hunter.cuny.edu/students/health-wellness/emergency-support-resources/"
            st.write("While Hunter doesn't explicitly have housing assistance, here are their emergency support resources](%s)" % hunter_assistance_url)
            no_housing_resource()
        
        elif college == "John Jay College of Criminal Justice":
            no_housing_resource()
        
        elif college == "Kingsborough Community College":
            kbcc_aid_url = "https://www.kbcc.cuny.edu/arc/index.html"
            kbcc_grant_url = "https://www.kbcc.cuny.edu/admission/EmergencyFund.html"
            st.write("Here is some financial assistance offered at Kingsborough Community College](%s)" % kbcc_aid_url)
            st.write("Here is the Student Emergency Funds offered by Kingsborough Community College](%s)" % kbcc_grant_url)
        
        elif college == "LaGuardia Community College":
            laguardia_housing_url = "https://www.laguardia.edu/cares/#:~:text=Apply%20using%20the%20Petrie%20Emergency%20Assistance%20Application%20form.&text=LaGuardia%20Foundation%20Emergency%20Assistance%20provides,internet%20access%2C%20and%20medical%20expenses."
            st.write("Check out LaGuardia CARES, which includes housing assistance](%s)" % laguardia_housing_url)
        
        elif college == "Lehman College":
            lehman_housing_url = "https://www.lehman.edu/student-affairs/student-housing/housing-resources.php"
            st.write("While Lehman College doesn't offer on-campus housing, here are some resources they provide](%s)" % lehman_housing_url)
            no_housing_resource()

        elif college == "Medgar Evers College":
            medgar_assistance_url = "https://www.mec.cuny.edu/student-success/transition-academy/"
            st.write("Medgar Evers College provides the transition academy, designed to help students experiencing homelessness and more](%s)" % medgar_assistance_url)
        
        elif college == "New York City College of Technology":
            citytech_housing_url = "https://www.citytech.cuny.edu/ssc/Emergency-resource-services.aspx"
            st.write("Here are some Emergency Resource Services, including housing aid](%s)" % citytech_housing_url)

        elif college == "Queens College":
            qc_housing_url = "https://www.qc.cuny.edu/faid/fed-nys-grants/"
            st.write("Queens College offers a variety of aid, including housing. Check out their grants](%s)" %qc_housing_url)
        
        elif college == "York College":
            york_petrie_fund_url = "https://www.york.cuny.edu/student-development/emergency-funding/petrie-fund-application"
            york_ehs_url = "https://www.studenthousing.org/and/york/"
            york_housing_connect_url = "https://www.york.cuny.edu/learning-center/services"
            st.write("Check out this housing emergency fund by York:](%s)" % york_petrie_fund_url)
            st.write("Check out the Educational Housing Services for Yoro](%s)" % york_ehs_url)
            st.write("Check out what the York College Learning Center offers](%s)" % york_housing_connect_url)

#Disability Questionnaire
if aid == "Disability Services":
    st.write("What type of enviorment are you looking for?")
    confirm1 = survey.checkbox("NYC Disability Resources")
    confirm2 = survey.checkbox("CUNY Disability Programs")

    if confirm1:
        other_disability_aid = "https://otda.ny.gov/"
        st.write("Check out this URL(%s)" % other_disability_aid)
    
    if confirm2:
        st.write("What College do you go to?")
        college = survey.radio("College",
                    options = [
            "Baruch College",
            "Borough of Manhattan Community College",
            "Bronx Community College",
            "Brooklyn College",
            "City College of New York",
            "College of Staten Island",
            "CUNY Graduate Center",
            "CUNY School of Law",
            "Hostos Community College",
            "Hunter College",
            "John Jay College of Criminal Justice",
            "Kingsborough Community College",
            "LaGuardia Community College",
            "Lehman College",
            "Medgar Evers College",
            "New York City College of Technology",
            "Queens College",
            "York College", 
            "Other"
                    ]
        ,
                    index=None,
                    label_visibility="hidden",
                    horizontal=True,
                )
        if college == "Baruch College":
            baruch_disability_url = "https://studentaffairs.baruch.cuny.edu/student-disability-services/"
            st.write("Baruch disabilitiy aid](%s)" % baruch_disability_url)

        elif college == "Borough of Manhattan Community College":
            bmcc_disability_url = "https://www.bmcc.cuny.edu/student-affairs/accessibility/"
            st.write("BMCC Office of Accessiblity link](%s)" % bmcc_disability_url)
        
        elif college == "Bronx Community College":
            bronx_disability_url = "https://www.bcc.cuny.edu/campus-resources/disability-services/"
            st.write("Check out Bronx Community College's Disability Services](%s)" % bronx_disability_url)
        
        elif college == "Brooklyn College":
            brooklyn_disability_url =  "https://www.brooklyn.edu/dosa/student-support-services/csds/"
            st.write("Check out Brooklyn College's Center for Student Disability Services](%s)" % brooklyn_disability_url)

        elif college == "City College of New York":
            ccny_disability_url = "https://www.ccny.cuny.edu/accessability?srsltid=AfmBOooPYesZYBgUkwyq-LGX1GN7aIw4GjjyZ6XX1ScEB08S1W1_cDVx"
            st.write("Check out the AAC/SDS ad City College of New York(%s)" % ccny_disability_url )
        
        elif college == "College of Staten Island":
            staten_disability_url = "https://www.csi.cuny.edu/campus-life/office-accessibility-services"
            st.write("Check out the Office of Accessibility Services at CSI](%s)" % staten_disability_url)

        elif college == "CUNY Graduate Center":
            gc_disability_url = "https://www.gc.cuny.edu/student-disability-services"
            st.write("Check out the student disability services at CUNY GC](%s)" % gc_disability_url)
        
        elif college == "CUNY School of Law":
            law_disability_url = "https://www.law.cuny.edu/students/disability-services-reasonable-accommodations/"
            st.write("Check out the Disability Services offered at CUNY School of Law](%s)" % law_disability_url)

        elif college == "Hostos Community College":
            hostos_disability_url = "https://www.hostos.cuny.edu/Administrative-Offices/Accessibility-Resource-Center-(ARC)"
            st.write("Check out the Accessibility Resource Center at Hostos Community College](%s)" % hostos_disability_url)
        
        elif college == "Hunter College":
            hunter_disability_url = "https://hunter.cuny.edu/students/health-wellness/accessibility/"
            st.write("Check out the Office of Accessibility at Hunter College](%s)" % hunter_disability_url)
        
        elif college == "John Jay College of Criminal Justice":
            johnjay_disability_url = "https://www.jjay.cuny.edu/student-life/wellness-center/accessibility-services"
            st.write("Check out the Accessibility Services at John Jay](%s)" % johnjay_disability_url)
        
        elif college == "Kingsborough Community College":
            kbcc_disability_url = "https://www.kbcc.cuny.edu/access-ability/homepage.html"
            st.write("Here are the Disability Services offered at Kingsborough Community College](%s)" % kbcc_disability_url)
        
        elif college == "LaGuardia Community College":
            laguardia_disability_url = "https://www.laguardia.edu/students/office-of-accessibility/"
            st.write("Check out the Office of Accessibility at LaGuardia Community College](%s)" % laguardia_disability_url)
        
        elif college == "Lehman College":
            lehman_disability_url = "https://www.lehman.edu/student-disability-services/"
            st.write("Here are the Student Disability Services offered at Lehman College](%s)" % lehman_disability_url)

        elif college == "Medgar Evers College":
            medgar_disability_url = "https://www.mec.cuny.edu/student-success/office-of-accessibility-and-accommodations-services/"
            st.write("Here is the Office of Accessibility and Accomodations Services at Medgar evers College](%s)" % medgar_disability_url)

        elif college == "New York City College of Technology":
            citytech_disability_url = "https://www.citytech.cuny.edu/accessibility/"
            st.write("Here is the Center for Student Accessibility at City Tech](%s)" % citytech_disability_url)

        elif college == "Queens College":
            qc_disability_url = "https://www.qc.cuny.edu/sp/"
            st.write("Here are the Special Services offered at QC](%s)" %qc_disability_url)
        
        elif college == "York College":
            york_disability_url = "https://www.york.cuny.edu/csd"
            st.write("Here is the Center for Students with Disabilities at York College(%s)" % york_disability_url)

mental_health_survey()

#Health and Wellness
if aid == "Health And Wellness":
    st.write("Which Health Service would you like to have information about?")
    health = survey.radio("Health Services", 
            options = ["Campus Health Services", "Health Insurance", "Community Resources","Immunization Info",
                       "Influenza (Flu)", "Infectious Disease Notification Protocol","Lactation Services"],
                       index= None,
                        label_visibility="collapsed",
                        horizontal=True)
    if health == "Campus Health Services":
        st.write("What College do you go to?")
        college = survey.radio("College",
                    options = [
            "Baruch College",
            "Borough of Manhattan Community College",
            "Bronx Community College",
            "Brooklyn College",
            "City College of New York",
            "College of Staten Island",
            "CUNY School of Labor and Urban Studies",
            "CUNY School of Professional Studies",
            "CUNY School of Public Health",
            "Guttman Community College",
            "Hostos Community College",
            "Hunter College",
            "John Jay College of Criminal Justice",
            "Kingsborough Community College",
            "LaGuardia Community College",
            "Lehman College",
            "Macaulay Honors College",
            "Medgar Evers College",
            "New York City College of Technology",
            "Queens College",
            "Queensborough Community College",
            "York College"
        ]
        ,
                    index=None,
                    label_visibility="hidden",
                    horizontal=True,
                )
        if college == "Baruch College":
            url = "http://www.baruch.cuny.edu/studentaffairs/healthServices.htm"
            st.write("The Health Services at Baruch College is Called the [Baruch College Health Services](%s)" % url)
            st.write("The Services are located at 138 E. 26th Street, 1st Fl. New York, NY 10010")
            st.write("Services Number: 646-312-2040")
            st.write("You can email them at StudentHealthCareCenter@baruch.cuny.edu")
            

        elif college == "Borough of Manhattan Community College":
            url = "https://www.bmcc.cuny.edu/student-affairs/health-services/"
            st.write("The Health Services at Borough of Manhattan Community College is Called the [BMCC Health Services](%s)" % url)
            st.write("The Services are located at 199 Chambers Street Room N-303 New York, NY 10007")
            st.write("Services Number: 212-220-8255")
            st.write("You can email them at healthservices@bmcc.cuny.edu")
            
        elif college == "Bronx Community College":
           url = "https://www.bmcc.cuny.edu/student-affairs/health-services/"
           st.write("The Health Services at Bronx Community College is Called the [BCC Office of Health Services](%s)" % url)
           st.write("The Services is located at West 181st St. & University Avenue, Loew Hall, Room 101 Bronx, NY 10453")
           st.write("Services Number: 718-289-5858")
           st.write("You can email them at healthservices@bcc.cuny.edu")
        elif college == "Brooklyn College":
            url = "https://www.brooklyn.cuny.edu/web/about/offices/studentaffairs/health-wellness/healthclinic.php"
            st.write("The Health Services at Brooklyn College is Called the [The Brooklyn College Health Clinic](%s)" % url)
            st.write("The Services is located at 2900 Bedford Avenue, 114 Roosevelt Hall Brooklyn, NY 11210")
            st.write("Services Number: 718-951-5580")
            st.write("You can email them at bchealthclinic@brooklyn.cuny.edu ")

        elif college == "City College of New York":
            url = "https://www.ccny.cuny.edu/health-wellness"
            st.write("The Health Services at City College of New York is Called the [The City College Student Health Services](%s)" % url)
            st.write("The Services is located at Marshak Science Building, Room J-15 138th Street & Convent Avenue New York, NY 10031")
            st.write("Services Number: 212-650-5327")
            st.write("You can email them at shs@ccny.cuny.edu ")

        elif college == "College of Staten Island":
            url = "http://www.csi.cuny.edu/studentaffairs/healthservices/"
            st.write("The Health Services at College of Staten Island is Called the [CSI Health and Wellness Services](%s)" % url)
            st.write("The Services is located at 2800 Victory Blvd., Room 1C-112 Staten Island, NY 10314")
            st.write("Services Number: 718-982 2300")
            st.write("You can email them at healthcenter@csi.cuny.edu")

        elif college == "CUNY School of Labor and Urban Studies":
            url = "https://slu.cuny.edu/academics/academics-2/counseling-wellness/"
            st.write("The Career Services at CUNY School of Labor and Urban Studies is Called the [Student Counseling and Wellness](%s)" % url)
            st.write("The Services is located at 25 West 43rd Street, 19th Floor New York, NY 10036")
            st.write("Services Number: 212-827-0200")
            st.write("You can email the wellness counsler, Lindsay Kazi, at lindsay.kazi@slu.cuny.edu")

        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/student-services/health-services"
            st.write("The Health Services at [CUNY School of Professional Studies](%s)" % url)
            st.write("The provided location is at 119 West 31st Street New York, NY 10001")
            st.write("Services Number: 212-652-CUNY ")
            st.write("You can email them at studentservices@sps.cuny.edu")

        elif college == "CUNY School of Public Health":
            url = "https://sph.cuny.edu/students/student-services/student-wellness/counseling-and-wellness-services/"
            st.write("The Health Services at CUNY School of Public Health is Called the [Counseling and Wellness Services](%s)" % url)
            st.write("The Services is located at 55 West 125th street, 5th floor New York, NY 10027")
            st.write("Services Number: 646-364-9644")

        elif college == "Guttman Community College":
            url = "https://guttman.cuny.edu/students/counseling-and-wellness-center/"
            st.write("The Health Services at Guttman Community College is Called the [Wellness Office](%s)" % url)
            st.write("The Services is located at 50 West 40th St, Room 506 New York, NY 10018")
            st.write("Services Number: 646-313-8000")
            st.write("You can email them at Counseling.wellness@guttman.cuny.edu")

        elif college == "Hostos Community College":
            url = "http://www.hostos.cuny.edu/sdem/health_wellness.html/"
            st.write("The Health Services at Hostos Community College is Called the [Hostos Community College Health Services](%s)" % url)
            st.write("The Services is located at Health Services 475 Grand Concourse A-334C Bronx, NY 10451")
            st.write("Services Number: 718-518-6542 or 718-518-6567")
   
        elif college == "Hunter College":
            url = "https://hunter.cuny.edu/students/health-wellness/"
            st.write("The Health Services at Hunter College is Called the [Hunter College Health & Support](%s)" % url)
            st.write("The Services is located at 695 Park Avenue Room 307, North New York, NY 10065")
            st.write("Services Number: 212-772-4800 212-772-4000")

        elif college == "John Jay College of Criminal Justice":
            url = "https://www.jjay.cuny.edu/wellness-health-services"
            st.write("The Health Services at John Jay College of Criminal Justice is Called the [John Jay College Health Services](%s)" % url)
            st.write("The Services is located at 524 West 59th StreetNew York, NY 10019")
            st.write("Services Number: 212-237-8754")
            st.write("You can email them at careers@jjay.cuny.edu")

        elif college == "Kingsborough Community College":
            url = "http://www.kbcc.cuny.edu/healthservices/index.html"
            st.write("The Health Services at Kingsborough Community College is Called the [Kingsborough Community College Health Center](%s)" % url)
            st.write("The Serives is located at Room A108 2001 Oriental Blvd. Brooklyn, NY 11235")
            st.write("Services Number: 718- 368-5684")
            st.write("You can email them at Health.Center@kbcc.cuny.edu")

        elif college == "LaGuardia Community College":
            url = "https://www.laguardia.edu/healthservices/"
            st.write("The Health Serives at LaGuardia Community College is Called the [LaGuardia Community College Health Services](%s)" % url)
            st.write("The Services is located at 31-10 Thomson Avenue Room MB-40 Long Island City, NY 11101")
            st.write("Services Number: 718-482-5408")
            st.write("You can email them at Health-Center@lagcc.cuny.edu")

        elif college == "Lehman College":
            url = "https://www.lehman.edu/student-health-center/"
            st.write("The Health Services at Lehman College is Called the [Lehman College The Student Health Center](%s)" % url)
            st.write("The Services is located at Old Gym, Room B008 250 Bedford Park Blvd. West Bronx, NY 10468-1589")
            st.write("Services Number: 718-960-8900")
            st.write("You can email them at med.requirements@lehman.cuny.edu")

        elif college == "Macaulay Honors College":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#healthservices:~:text=Mental%20Health%20%26%20Wellness%20Center"
            st.write("The Health Services at Macaulay Honors College is Called the [Mental Health & Wellness Center](%s)" % url)
            st.write("The Services is located at 35 W. 67th Street, New York, NY 10023")
            st.write("Services Number: 212-729-2914")
            st.write("You can email them atwellness@mhc.cuny.edu")
 
        elif college == "Medgar Evers College":
            url = "https://www.mec.cuny.edu/student-success/health-services/"
            st.write("The Career Services at Medgar Evers College is Called the [Medgar Evers College Health Services](%s)" % url)
            st.write("The Services is located at 1637 Bedford Avenue, Room S217 Brooklyn, NY 11225")
            st.write("Services Number: 718-270-6075 or 718-270-4900")
            st.write("You can email them at healthservices@mec.cuny.edu")

        elif college == "New York City College of Technology":
            url = "https://www.citytech.cuny.edu/wellness-center/"
            st.write("The Health Service at New York City College of Technology is Called the [New York City College of Technology Health Services](%s)" % url)
            st.write("The Service is located at 300 Jay Street General Bldg, Room 414 Brooklyn, NY 11201")
            st.write("Service Number: 718-260-5385 or 718-260-5910")
            st.write("You can email them at wellnesscenter@citytech.cuny.edu")

        elif college == "Queens College":
            url = "https://www.qc.cuny.edu/health/"
            st.write("The Health Services at Queens College is Called the [Queens College Health Services](%s)" % url)
            st.write("The Services is located at 65-30 Kissena Blvd. Frese Hall, 3rd Floor Flushing, NY 11367")
            st.write("Services Number: 718-997-2760")
            st.write("You can email them at healthquestions@qc.cuny.edu")

        elif college == "Queensborough Community College":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#healthservices:~:text=Queensborough%20Community%20College%20Health%20Services"
            st.write("The Health Services at Queensborough Community College is Called the [Queensborough Community College Health Services](%s)" % url)
            st.write("The Services is located at 222-05 56th Avenue Medical Arts Building, Room MC-02 Bayside, NY 11364")
            st.write("Services Number: 718-631-6375")
            st.write("You can email them at HealthServices@qcc.cuny.edu")

        elif college == "York College":
            url = "https://www.york.cuny.edu/health"
            st.write("The Health Services at York College is Called the [York College Health Services](%s)" % url)
            st.write("The Services is located at 94-20 Guy Brewer Boulevard Room #3E03 Jamaica, NY 11451")
            st.write("Services Number: 718-262-2282")
            st.write("You can email them at StudHealthSvcCtr@york.cuny.edu")


    if health == "Health Insurance":
        url = ("https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#insurance")
        url2 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#gotinsurance"
        st.write("You can follow this link to find any information on obtaining [Health Insurance](%s)" % url)
        st.write("[If you already have insurance](%s)" % url2)
    
    if health == "Community Resources":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#comresources"
        url2 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#1691701649205-c3369359-1725"
        url3 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#1683737540708-e92f159c-f358"
        url4 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#1619819868109-17cc6e25-4129"
        st.write("The [Community Resources](%s) are plentiful including information on")
        st.write("[Abortion Access](%s)" % url2)
        st.write("[STI Testing](%s)" % url3)   
        st.write("[Healthy Eating](%s)" % url4)
    if health == "Immunization Info":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#immunization"
        st.write("New York State Public Health Law 2165 requires all students entering a post-secondary institution to provide their health services center with immunity to Measles, Mumps and Rubella. This law applies to students born on or after January 1, 1957, who are registered for 6 or more credits at a CUNY campus. Proof of immunity must be documented by a health care practitioner or other acceptable evidence in the following way")
        st.write("Any other information can be found [here](%s)" % url)
    if health == "Influenza (Flu)":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#influenza"
        st.write("Information surronding [THE FLU](%s)" % url)
    if health == "Infectious Disease Notification Protocol":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#idn-protocol"
        st.write("Please follow the Directions displayed at this [link](%s)" % url)
    if health == "Lactation Services":
        st.write("What College do you go to?")
        college = survey.radio("College",
                    options = [
            "Baruch College",
            "Borough of Manhattan Community College",
            "Bronx Community College",
            "Brooklyn College",
            "City College of New York",
            "College of Staten Island",
            "CUNY Graduate Center",
            "CUNY School of Law",
            "CUNY School of Professional Studies",
            "CUNY School of Public Health",
            "Guttman Community College",
            "Hostos Community College",
            "Hunter College",
            "John Jay College of Criminal Justice",
            "Kingsborough Community College",
            "LaGuardia Community College",
            "Lehman College",
            "Medgar Evers College",
            "New York City College of Technology",
            "Queens College",
            "Queensborough Community College",
            "York College"
        ]
        ,
                    index=None,
                    label_visibility="hidden",
                    horizontal=True,
                )

        if college == "Baruch College":
            url = "https://hr.baruch.cuny.edu/lactation-room/"
            st.write("[Lactation Room Information Overview](%s) for Baruch College" % url)
            st.write("The lactation room is located in room #112 on the first floor of the Information and Technology Building.")        
        elif college == "Borough of Manhattan Community College":
            url = "https://www.bmcc.cuny.edu/student-affairs/womens-resource-center/lactation/"
            st.write("[Lactation Room Info](%s) for Borough of Manhattan Community College" % url)
        elif college == "Bronx Community College":
            st.write("The Lactation Room for Bronx Community College is located at Loew Hall Room 105 and it is open to students, faculty, and staff")
        elif college == "Brooklyn College":
            st.write("A Lactation room is available for nursing mothers (faculty, staff and students) in the Early Childhood Center in 1604 James Hall and in the John Whyte Room, 303 Student Center.")
            st.write("Open Mon-Thu 8:30am-10:30pm & Fri 8:30am-5:00pm.")
        elif college == "City College of New York":
            st.write("City College of NY Lactation Room accommodations are available at Student Health Services, Marshak Science Building, 4th Floor, Room 418-S (Temporary location during renovation) during office hours Monday-Friday 9am-5pm")
        elif college == "College of Staten Island":
            url = "https://csitoday.com/2017/04/lactation-room/"
            st.write("Here is some information on the [Lactation Room](%s) at CSI"% url)
            st.write("Located in the Center for the Arts (Building 1P), Room 1P-008 has been designated as a lactation room for College of Staten Island faculty, staff, and students (as available). The room is located on the lower level, and is accessible from the west elevator in the Atrium. Those seeking to use the lactation room should present their current CSI ID to the Office of the Vice President for Finance and Administration, Building 1A, Room 309. Keys for the room will be issued through that Office.")
        elif college == "CUNY Graduate Center":
            st.write("A dedicated space has been established at The Graduate Center for mothers to express breast milk for a nursing child. Room 7408, also called the Mothers' Room, is available to all nursing women students and employees who present a current Graduate Center ID. Those wishing to use the Mothers’ Room should fill out a one-time key request form in the Student Affairs office, Room 7301. Nursing mothers may also use the Child Care Center (until 5 p.m.) for the same purpose, ring the bell for Room 3201")
        elif college == "CUNY School of Law":
            st.write("The lactation room, located in room 2-101, is available to students, staff, or faculty who wish to use the room. Please direct inquiries to the Office of Student Affairs, room 5-110, (718) 340-4207 or email studentaffairsoffice@mail.law.cuny.edu.")
        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/about/policies/facilities-policies/mother%E2%80%99s-room-policy"
            st.write("Here is Info on the [Mother Rooms]")
            st.write("All students, staff, faculty, and visitors can use the lactation room on the 10th floor opposite the elevator during hours of operation")
        elif college == "CUNY School of Public Health":
            url = "https://sph.cuny.edu/life-at-sph/lactation-support-room/"
            st.write("Here is information on the [Lactation Support Room](%s)" % url)
            st.write("All students, faculty, staff and visitors may use the Lactation Support Room in Room 819 where you will find a comfortable chair, a counter, and a refrigerator for storing your milk, snacks and beverages.")
        elif college == "Guttman Community College":
            st.write("Guttman has a room dedicated to lactation and will be made available based on availability, on a first-come, first-served basis. If you have any questions or would like to make a reservation for the lactation room, please email hr@guttman.cuny.edu.")
        elif college == "Hostos Community College":
            st.write("Hostos has established the following spaces as available lactation rooms:")
            st.write("Students: Health Services Office, “A Building” Room A-334C: Monday-Thursday 9am-5pm")
            st.write("To gain access, students should call the Health Services Office at 718-518-6542")
            st.write("Or send an email to CJoseph@hostos.cuny.edu. A response will be given within a “reasonable” amount of time not to exceed five business days.")
        elif college == "Hunter College":
            st.write("A lactation room is available to Hunter students, faculty, and staff at Brookdale: Room E117 (East Building) is the first room to your right when entering the Rotunda Foyer. For access, guests must first submit an online request form to have their Hunter OneCard authorized for keyless entry. Please specify that your request is for the Brookdale Campus and allow up to 2 business days for your card to be authorized. For questions, contact the OneCard office at 212-650-3191 or onecard@hunter.cuny.edu.")
        elif college == "John Jay College of Criminal Justice":
            st.write("The Lactation Room is the last door on your right, adjacent to the All-Gender Locker Room. The lactation space locks from the inside, there is a table, chair, access to an electrical outlet and sink. Unfortunately, it does not have a refrigerator. Secure, refrigerated storage is available for students and staff in the Women’s Center for Gender Justice located in room L.67.")
        elif college == "Kingsborough Community College":
            st.write("The Health Center at KBCC has space for lactation open to everyone- students, staff, and visitors.")
            st.write("Open 9-5 Mon Thurs Fri 9am-5pm and Tues- Wed 9am-8pm")
        elif college == "LaGuardia Community College":
            st.write("Students can request/reserve the lactation room in the Wellness Center C building Room 349. Form is on-line. Staff ad faculty must go to HR for sign up sheet on-line to reserve time. Lactation room is in Lower Lobby M building Room MB60 basement. An id is required.")
        elif college == "Lehman College":
            form = "http://goo.gl/forms/8vpLQcyJQA"
            url = "https://www.lehman.edu/student-health-center/wellness-education-promotion/breastfeeding-support-services/"
            st.write("Lehman College has this website for [breastfeeding information].")
            st.write("The lactation room is available by request to all students enrolled at the college as well as faculty and staff. The lactation room is located in Carman Hall, room 187.")
            st.write("To request access, complete the [lactation request form](%s)." % form)
        elif college == "Medgar Evers College":
            url = "https://www.mec.cuny.edu/student-success/health-services/lactation-room/"
            st.write("Here is website on the [Lactation Room](%s)" % url)
            st.write("On campus there are two lactation rooms available to both working and student mothers to use. One is in the Student Building (S-Building) Office of Health Services Room 217 and the other is located in The Center for Women's Development in the Carroll Street Building (C-Building) Room C-M2.")
        elif college == "New York City College of Technology":
            st.write("Lactation room is available to students, staff, faculty, and visitors at the Student Wellness Center M, T, W, Th 9am-5:30pm. Located in the Academic Bldg. ALL110")
        elif college == "Queens College":
            st.write("The Lactation room at Queens College is in Kiely 134E. It is open to students, faculty, and staff. Health Services request a form filled out to get the key.  Once the key is given, they can access the room and refrigerator during evening hours.")
        elif college == "Queensborough Community College":
            st.write("Lactation rooms are available in Health Services Mon-Thursday 9am-5pm. Student Activities also have a room for nursing mothers.")
        elif college == "York College":
            url = "https://www.york.cuny.edu/womens-center/lactation-services"
            form = "https://reservations.york.cuny.edu/lactation"
            st.write("Here is the website info on the [Lactation Room](%s)" % url)
            st.write("The room is located in the Academic Core Building Room 1H11.  If there room is locked you may go to Public Safety (AC-1M01) and ask them to unlock it for you.")
            st.write("You can reserve the room with this [form](%s)" % form)

#Food Insecurity