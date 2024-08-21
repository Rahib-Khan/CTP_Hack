import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
pages = survey.pages(2, on_submit=lambda: st.success("Your responses have been recorded. Thank you!"))
with pages:
    if pages.current == 0:
        st.write("What College do you go to?")
        college = survey.radio(
            "College",
            options=["Baruch college","Borough of Manhattan CC", "Bronx Community College","Brooklyn College",
                    "The City College of New York" ,"The College of Staten Island","The Graduate Center", "Guttman Community College","Craig Newmark Graduate School of Journalism at CUNY","CUNY Graduate School of Public Health and Policy" ,"CUNY School of Labor & Urban Studies", "Hostos Community College", "Hunter College", "John Jay College of Criminal Justice"
                    ,"Kingsborough Community College","LaGuardia Community College"
                    ,"CUNY School of Law","Lehman College"
                    ,"Medgar Evers College","NY City College of Technology"
                    ,"Queens College","Queensborough Community College","School of Professional Studies","York  college" ],
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
        st.write("What Type of Aid Are you looking for?")
        aid = survey.radio(
            "Issues",
            options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
            index=0,
            label_visibility="collapsed",
            horizontal=True,
        )
        if college == "Queens College":
            st.write("How often do you use Streamlit?")
            survey.select_slider(
                "st_frequency",
                options=["Every Day", "Every week", "Every Month", "Once a year", "Rarely"],
                label_visibility="collapsed",
            )
        elif college == "No":
            st.write("Have you used other dashboarding tools?")
            used_other = survey.radio(
                "used_other",
                options=["NA", "Yes", "No"],
                index=0,
                label_visibility="collapsed",
                horizontal=True,
            )
            if used_other == "Yes":
                st.write("Which tools?")
                survey.multiselect(
                    "other_tools",
                    options=["Dash", "Voila", "Panel", "Bokeh", "Plotly", "Other"],
                    label_visibility="collapsed",
                )
    elif pages.current == 1:
        st.write("How satisfied are you with this survey?")
        survey.select_slider(
            "Overall Satisfaction",
            options=["Very Unsatisfied", "Unsatisfied", "Neutral", "Satisfied", "Very Satisfied"],
            label_visibility="collapsed",
        )