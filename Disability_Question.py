import streamlit as st
import streamlit_survey as ss
import First

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

st.write("What Type of Aid Are you looking for?")
aid = survey.radio("Issues",
        options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
        index= None,
        label_visibility="collapsed",
        horizontal=True,
    )


#Housing Instability Questionnaires
if aid == "Disability Services":
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
            johnjay_disability_url = https://www.jjay.cuny.edu/student-life/wellness-center/accessibility-services
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

