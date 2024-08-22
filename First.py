import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")


st.write("What Type of Aid Are you looking for?")
aid = survey.radio("Issues",
    options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
    index=None,
    label_visibility="collapsed",
    horizontal=True,
)