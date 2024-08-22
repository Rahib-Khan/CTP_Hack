import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

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
    st.write("Baruch College selected.")
elif college == "Borough of Manhattan Community College":
    st.write("Borough of Manhattan Community College selected.")
elif college == "Bronx Community College":
    st.write("Bronx Community College selected.")
elif college == "Brooklyn College":
    st.write("Brooklyn College selected.")
elif college == "City College of New York":
    st.write("City College of New York selected.")
elif college == "College of Staten Island":
    st.write("College of Staten Island selected.")
elif college == "CUNY Graduate Center":
    st.write("CUNY Graduate Center selected.")
elif college == "CUNY School of Law":
    st.write("CUNY School of Law selected.")
elif college == "CUNY School of Professional Studies":
    st.write("CUNY School of Professional Studies selected.")
elif college == "CUNY School of Public Health":
    st.write("CUNY School of Public Health selected.")
elif college == "Guttman Community College":
    st.write("Guttman Community College selected.")
elif college == "Hostos Community College":
    st.write("Hostos Community College selected.")
elif college == "Hunter College":
    st.write("Hunter College selected.")
elif college == "John Jay College of Criminal Justice":
    st.write("John Jay College of Criminal Justice selected.")
elif college == "Kingsborough Community College":
    st.write("Kingsborough Community College selected.")
elif college == "LaGuardia Community College":
    st.write("LaGuardia Community College selected.")
elif college == "Lehman College":
    st.write("Lehman College selected.")
elif college == "Macaulay Honors College":
    st.write("Macaulay Honors College selected.")
elif college == "Medgar Evers College":
    st.write("Medgar Evers College selected.")
elif college == "New York City College of Technology":
    st.write("New York City College of Technology selected.")
elif college == "Queens College":
    st.write("Queens College selected.")
elif college == "Queensborough Community College":
    st.write("Queensborough Community College selected.")
elif college == "York College":
    st.write("York College selected.")
