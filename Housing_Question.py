#Lauren Ramroop

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

#For colleges with no direct housing aid
other_housing_resources = "https://www.nyc.gov/site/hra/help/affordable-housing.page"
def no_housing_resource():
    st.write("Sorry, the specified college doesn't provide direct housing relief. Here are some other programs")
    st.write("Please follow this [LINK](%s)" % other_housing_resources)

#Housing Instability Questionnaires
if aid == "Housing Instability":
    confirm1 = survey.checkbox("CNYC Housing Programs")
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
