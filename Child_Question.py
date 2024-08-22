import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")


st.write("What Type of Aid Are you looking for?")
aid = survey.radio("Issues",
    options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
    index= None,
    label_visibility="collapsed",
    horizontal=True,
)

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
    "York College"
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
    elif college == "Borough of Manhattan Community College":
        st.write("Is your child between the ages of 3 Months and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        
    elif college == "Bronx Community College":
        st.write("Is your child between the ages of 6 weeks and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Brooklyn College":
        st.write("Is your child between the ages of 4 Months and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "City College of New York":
        st.write("Is your child between the ages of 4 Months and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "College of Staten Island":
        st.write("Is your child between the ages of 6 Months and 9 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "CUNY Graduate Center":
        st.write("Is your child between the ages of 2 Years and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "CUNY School of Law":
        st.write("Is your child between the ages of 6 Months and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Hostos Community College":
        st.write("Is your child between the ages of 6 Weeks and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Hunter College":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "John Jay College of Criminal Justice":
        st.write("Is your child between the ages of 6 Months and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Kingsborough Community College":
        st.write("Is your child between the ages of 2 Years & 10 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "LaGuardia Community College":
        st.write("Is your child between the ages of 6 Months and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Lehman College":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Medgar Evers College":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "New York City College of Technology":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "Queens College":
        st.write("Is your child between the ages of 30 Months and 10 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
    elif college == "York College":
        st.write("Is your child between the ages of 6 Months and 10 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
