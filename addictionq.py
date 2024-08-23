import streamlit as st
import streamlit_survey as ss
from utilities import aid_options, college_emails

colleges = list(college_emails.keys())


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


survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
st.write("What type of aid are you looking for?")
aid = survey.radio("Issues",
                   options=aid_options,
                   index=None,
                   label_visibility="collapsed",
                   horizontal=True,
                   )
# Addiction Questions
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
