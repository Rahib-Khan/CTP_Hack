import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

def shake():
    url = "https://app.joinhandshake.com/login"
    st.write("You can use the new online career management platform and recruiting system, [Handshake](%s) , to find oppurtnities for students" % url)

st.write("What Type of Aid Are you looking for?")
aid = survey.radio("Issues",
        options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
        index= None,
        label_visibility="collapsed",
        horizontal=True,
    )
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
            st.write("Which School of Baruch are you apart of?")
            baruch = survey.radio("Baruch Schools",
                    options=["Baruch Undergraduate","Austin W. Marxe School of Public and International Affairs", "Weissman School of Arts & Sciences", "Zicklin School of Business"],
                    index= None,
                    label_visibility="Visible",
                    horizontal=False)
            

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
    
    if check2:
        url = "https://www.cuny.edu/about/administration/offices/ocip/"
        st.write("Okay")
        st.write("Please follow this [link](%s) to be redirected to a plethora of CUNY Career Programs" % url)