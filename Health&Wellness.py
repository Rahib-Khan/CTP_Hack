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
if aid == "Health And Wellness":
    st.write("Which Health Service would you like to have information about?")
    health = survey.radio("Health Services", 
            options = ["Campus Health Services", "Health Insurance", "Community Resources","Immunization Info",
                       "Influenza (Flu)", "Infectious Disease Notification Protocol","Student Affairs","Lactation Services"],
                       index= None,
                        label_visibility="collapsed",
                        horizontal=True)
    if health == "Campus Health Services":
        st.write("What College do you go to?")
        college = survey.radio("College",
                    options = [
            "Baruch College",
            "Borough of Manhattan Community College",
            "Bronx Community College",
            "Brooklyn College",
            "City College of New York",
            "College of Staten Island",
            "CUNY School of Labor and Urban Studies",
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
            url = "http://www.baruch.cuny.edu/studentaffairs/healthServices.htm"
            st.write("The Health Center at Baruch College is Called the [Baruch College Health Services](%s)" % url)
            st.write("The Center is located at 138 E. 26th Street, 1st Fl. New York, NY 10010")
            st.write("Center Number: 646-312-2040")
            st.write("You can email them at StudentHealthCareCenter@baruch.cuny.edu")
            

        elif college == "Borough of Manhattan Community College":
            url = "https://www.bmcc.cuny.edu/student-affairs/health-services/"
            st.write("The Health Center at Borough of Manhattan Community College is Called the [BMCC Health Services](%s)" % url)
            st.write("The Center is located at 199 Chambers Street Room N-303 New York, NY 10007")
            st.write("Center Number: 212-220-8255")
            st.write("You can email them at healthservices@bmcc.cuny.edu")
            
        elif college == "Bronx Community College":
           url = "https://www.bmcc.cuny.edu/student-affairs/health-services/"
            st.write("The Health Center at Borough of Manhattan Community College is Called the [BMCC Health Services](%s)" % url)
            st.write("The Center is located at 199 Chambers Street Room N-303 New York, NY 10007")
            st.write("Center Number: 212-220-8255")
            st.write("You can email them at healthservices@bmcc.cuny.edu")
        elif college == "Brooklyn College":
            url = "https://www.brooklyn.cuny.edu/web/about/offices/studentaffairs/health-wellness/healthclinic.php"
            st.write("The Career Center at Brooklyn College is Called the [Magner Career Center](%s)" % url)
            st.write("The Center is located at 2900 Bedford Ave. 1303 James Hall Brooklyn, NY 11210")
            st.write("Center Number: 718-951-5696")
            st.write("You can email them at careernews@brooklyn.cuny.edu ")

        elif college == "City College of New York":
            url = "https://www.ccny.cuny.edu/health-wellness"
            st.write("The Career Center at City College of New York is Called the [Career and Professional Development Institute](%s)" % url)
            st.write("The Center is located at 138th Street at Convent Avenue NAC Building, 1st Fl, Room 116 New York, NY 10031")
            st.write("Center Number: 212-650-5327")
            st.write("You can email them at cpdi@ccny.cuny.edu ")

        elif college == "College of Staten Island":
            url = "http://www.csi.cuny.edu/studentaffairs/healthservices/"
            st.write("The Career Center at College of Staten Island is Called the [Center for Career and Professional Development](%s)" % url)
            st.write("The Center is located at 2800 Victory Boulevard Building 1A, Room 105 Staten Island, NY 10314")
            st.write("Center Number: 718-982 2300")
            st.write("You can email them at careers@csi.cuny.edu")

        elif college == "CUNY School of Labor and Urban Studies":
            url = "https://slu.cuny.edu/academics/academics-2/counseling-wellness/"
            st.write("The Career Center at CUNY School of Labor and Urban Studies is Called the [Career and Professional Development Center](%s)" % url)
            st.write("The Center is located at 25 W 43rd Street, 18th floor New York, NY 10036")
            st.write("Center Number: 646-313-8339")
            st.write("You can email them at careerservices@slu.cuny.edu")

        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/student-services/career-services"
            st.write("The Career Center at CUNY School of Professional Studies is Called the [Office of Career Services](%s)" % url)
            st.write("The Center is located at 119 West 31st Street, 4th floor New York, NY 10001")
            st.write("Center Number: 646-664-8618")
            st.write("You can email them at career.services@sps.cuny.edu")

        elif college == "CUNY School of Public Health":
            url = "https://sph.cuny.edu/students/student-services/student-wellness/counseling-and-wellness-services/"
            st.write("The Career Center at CUNY School of Public Health is Called the [Office of Career Services](%s)" % url)
            st.write("The Center is located at 55 West 125th street, 5th floor New York, NY 10027")
            st.write("Center Number: 646-364-9644")
            st.write("You can email them at careerservices@sph.cuny.edu")

        elif college == "Guttman Community College":
            url = "https://guttman.cuny.edu/students/wellness/"
            st.write("The Career Center at Guttman Community College is Called the [Center for Career Preparation & Partnerships](%s)" % url)
            st.write("The Center is located at 50 W. 40th St. New York, NY 10018")
            st.write("Center Number: 646-313-8066")
            st.write("You can email them at cpartnerships@guttman.edu")

        elif college == "Hostos Community College":
            url = "http://www.hostos.cuny.edu/sdem/health_wellness.html/"
            st.write("The Career Center at Hostos Community College is Called the [Career Services](%s)" % url)
            st.write("The Center is located at Savoy Building, D210 Bronx, NY 10451")
            st.write("Center Number: 718-518-4468")
            st.write("You can email them at careerservices@hostos.cuny.edu")
   
        elif college == "Hunter College":
            url = "https://hunter.cuny.edu/students/counseling-and-wellness-services/immunization-records/"
            st.write("The Career Center at Hunter College is Called the [Career Development Services](%s)" % url)
            st.write("The Center is located at 695 Park Avenue Room 805 E New York, NY 10021")
            st.write("Center Number: 212-772-4850")
            st.write("You can email them at career@hunter.cuny.edu")

        elif college == "John Jay College of Criminal Justice":
            url = "https://www.jjay.cuny.edu/wellness-health-services"
            st.write("The Career Center at John Jay College of Criminal Justice is Called the [Center for Career and Professional Development](%s)" % url)
            st.write("The Center is located at 524 West 59th StreetNew York, NY 10019")
            st.write("Center Number: 212-237-8754")
            st.write("You can email them at careers@jjay.cuny.edu")

        elif college == "Kingsborough Community College":
            url = "http://www.kbcc.cuny.edu/healthservices/index.html"
            st.write("The Career Center at Kingsborough Community College is Called the [Center for Career Development & Experiential Learning](%s)" % url)
            st.write("The Center is located at Room C201 2001 Oriental Boulevard Brooklyn, NY 11235")
            st.write("Center Number: 718-368-5115")
            st.write("You can email them at careerdevelopment@kbcc.cuny.edu")

        elif college == "LaGuardia Community College":
            url = "https://www.laguardia.edu/healthservices/"
            st.write("The Career Center at LaGuardia Community College is Called the [Center for Career & Professional Development](%s)" % url)
            st.write("The Center is located at 31-10 Thomson Avenue Room B114 Long Island City, NY 11101")
            st.write("Center Number: 718-482-5235")
            st.write("You can email them at career@lagcc.cuny.edu")

        elif college == "Lehman College":
            url = "http://www.lehman.cuny.edu/student-health-center/clinical-services-fees.php"
            st.write("The Career Center at Lehman College is Called the [Career Exploration & Development Center](%s)" % url)
            st.write("The Center is located at 250 Bedford Park Blvd. West, Shuster Hall, Room 254 Shuster Hall, Room 254 Bronx, NY 10468")
            st.write("Center Number: 718-960-8366")
            st.write("You can email them at career.services@lehman.cuny.edu")

        elif college == "Macaulay Honors College":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#healthservices:~:text=Mental%20Health%20%26%20Wellness%20Center"
            st.write("The Career Center at Macaulay Honors College is Called the [Office of Career Development](%s)" % url)
            st.write("The Center is located at 35 West 67th Street New York, NY 10023")
            st.write("Center Number: 212-729-2947")
            st.write("You can email them at internships@mhc.cuny.edu")
 
        elif college == "Medgar Evers College":
            url = "https://www.mec.cuny.edu/student-success/health-services/"
            st.write("The Career Center at Medgar Evers College is Called the [Office of Career Management Services](%s)" % url)
            st.write("The Center is located at Student Services Building1637 Bedford Avenue, Room S302 Brooklyn, NY 11225")
            st.write("Center Number: 718-270-6055")
            st.write("You can email them at CareerServices@mec.cuny.edu")

        elif college == "New York City College of Technology":
            url = "https://www.citytech.cuny.edu/wellness-center/"
            st.write("The Career Center at New York City College of Technology is Called the [Professional Development Center](%s)" % url)
            st.write("The Center is located at Room L-114 250 Jay Street Brooklyn, New York 11201")
            st.write("Center Number: 718-260-5050")
            st.write("You can email them at pdc@citytech.cuny.edu")

        elif college == "Queens College":
            url = "https://www.qc.cuny.edu/health/"
            st.write("The Career Center at Queens College is Called the [Center for Career Engagement and Internships](%s)" % url)
            st.write("The Center is located at 65-30 Kissena Boulevard Frese Hall, Room 213 Flushing, NY 11367")
            st.write("Center Number: 718-997-4465")
            st.write("You can email them at qc_career@qc.cuny.edu")

        elif college == "Queensborough Community College":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#healthservices:~:text=Queensborough%20Community%20College%20Health%20Services"
            st.write("The Career Center at Queensborough Community College is Called the [Career Services](%s)" % url)
            st.write("The Center is located at Library Building, L-429222-05, 56th Avenue Bayside, NY 11364")
            st.write("Center Number: 718-631-6297")
            st.write("You can email them at careerservices@qcc.cuny.edu")

        elif college == "York College":
            url = "https://www.york.cuny.edu/health"
            st.write("The Career Center at York College is Called the [The Office of Career Services](%s)" % url)
            st.write("The Center is located at 94-20 Guy Brewer Boulevard Room #3E03 Jamaica, NY 11451")
            st.write("Center Number: 718-262-2282")
            st.write("You can email them at career@york.cuny.edu")


    if health == "Health Insurance":
    
    if health == "Community Resources":
    
    if health == "Immunization Info":

    if health == "Influenza (Flu)":

    if health == "Infectious Disease Notification Protocol":

    if health == "Lactation Services"
