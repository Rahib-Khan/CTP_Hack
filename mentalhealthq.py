import streamlit as st
import streamlit_survey as ss
from utilities import aid_options, crisis_options, college_emails, get_counseling_info

counseling_info = get_counseling_info()
colleges = list(college_emails.keys())


# Function to redirect students to mental health programs
def mental_health_survey():
    survey = ss.StreamlitSurvey("Mental Health Services Survey")
    st.write("What type of aid are you looking for?")
    aid = survey.radio("Issues",
                       options=aid_options,
                       index=None,
                       label_visibility="collapsed",
                       horizontal=True,
                       )
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


mental_health_survey()
