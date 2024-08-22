import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

st.write("What College do you go to?")
college = survey.radio("College",
            options=["Baruch college","Borough of Manhattan CC", "Bronx Community College","Brooklyn College",
                    "The City College of New York" ,"The College of Staten Island","The Graduate Center", "Guttman Community College","Craig Newmark Graduate School of Journalism at CUNY","CUNY Graduate School of Public Health and Policy" ,"CUNY School of Labor & Urban Studies", "Hostos Community College", "Hunter College", "John Jay College of Criminal Justice"
                    ,"Kingsborough Community College","LaGuardia Community College"
                    ,"CUNY School of Law","Lehman College"
                    ,"Medgar Evers College","NY City College of Technology"
                    ,"Queens College","Queensborough Community College","School of Professional Studies","York  college" ],
            index=None,
            label_visibility="hidden",
            horizontal=True,
        )