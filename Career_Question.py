import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

def shake(url):
    st.write("You can use the new online career management platform and recruiting system, [Handshake](%s) , to find oppurtnities as a student" % url)

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
            st.write("Which School of Baruch are you apart of?")
            baruch = survey.radio("Baruch Schools",
                    options=["Baruch Undergraduate","Austin W. Marxe School of Public and International Affairs", "Weissman School of Arts & Sciences", "Zicklin School of Business"],
                    index= None,
                    label_visibility="visible",
                    horizontal=False)
            if baruch == "Baruch Undergraduate":
                url = "https://studentaffairs.baruch.cuny.edu/starr-career-development-center/"
                st.write("The Career Center at Baruch College is Called the [Starr Career Development Center](%s)" % url)
                st.write("The Center is located at 1 Bernard Baruch Way Box B2150 New York, NY 10010")
                st.write("Center Number: 646-312-4670")
                st.write("You can email them at Careerdc@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")
            elif baruch == "Austin W. Marxe School of Public and International Affairs":
                url = "http://www.baruch.cuny.edu/mspia/career-services/"
                st.write("The Career Center at Baruch's Austin W. Marxe School of Public and International Affairs is Called the [Marxe Graduate Career Services](%s)" % url)
                st.write("The Center is located at 1 Bernard Baruch Way Box D0901 New York, NY 10010")
                st.write("Center Number: 646-660-6798")
                st.write("You can email them at mspia.careerservices@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")
            elif baruch == "Weissman School of Arts & Sciences":
                url = "http://www.baruch.cuny.edu/wsas/graduatecareers/"
                st.write("The Career Center at Baruch's Weissman School of Arts & Sciences is Called the [Weissman Graduate Career Services](%s)" % url)
                st.write("The Center is located at 1 Bernard Baruch Way Box B7-180 New York, NY 10010")
                st.write("Center Number: 646-312-3887")
                st.write("You can email them at mspia.careerservices@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")
            elif baruch == "Zicklin School of Business":
                url = "https://zicklin.baruch.cuny.edu/experience-zicklin/student-experience/gcmc-graduate-career-management-center/"
                st.write("The Career Center at Baruch's Zicklin School of Business is Called the [Graduate Career Management Center](%s)" % url)
                st.write("The Center is located at 151 East 25th street Box H-820 New York, NY 10010")
                st.write("Center Number: 646-312-1330")
                st.write("You can email them at zicklin.gcmc@baruch.cuny.edu")
                shake("https://baruch.joinhandshake.com/login?ref=app-domain")

        elif college == "Borough of Manhattan Community College":
            url = "http://www.bmcc.cuny.edu/career/"
            st.write("The Career Center at Borough of Manhattan Community College is Called the [Center for Career Development](%s)" % url)
            st.write("The Center is located at 199 Chambers Street Room S-342 New York, NY 10007")
            st.write("Center Number: 212-220-8170")
            st.write("You can email them at career@bmcc.cuny.edu")
            shake("https://bmcc.joinhandshake.com/login?ref=app-domain")
        elif college == "Bronx Community College":
            url = "http://www.bcc.cuny.edu/services/career-development/"
            st.write("The Career Center at Bronx Community College is Called the [The Office of Career Development](%s)" % url)
            st.write("The Center is located at Snow Hall, First Floor 2155 University Avenue Bronx, NY 10453")
            st.write("Center Number: 718-220-7546")
            st.write("You can email them at Careerdevelopment@bcc.cuny.edu ")
            shake("https://bcccuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Brooklyn College":
            url = "https://www.brooklyn.edu/web/academics/centers/magner.php"
            st.write("The Career Center at Brooklyn College is Called the [Magner Career Center](%s)" % url)
            st.write("The Center is located at 2900 Bedford Ave. 1303 James Hall Brooklyn, NY 11210")
            st.write("Center Number: 718-951-5696")
            st.write("You can email them at careernews@brooklyn.cuny.edu ")
            shake("https://brooklyncuny.joinhandshake.com/login?ref=app-domain")
        elif college == "City College of New York":
            url = "https://www.ccny.cuny.edu/cpdi"
            st.write("The Career Center at City College of New York is Called the [Career and Professional Development Institute](%s)" % url)
            st.write("The Center is located at 138th Street at Convent Avenue NAC Building, 1st Fl, Room 116 New York, NY 10031")
            st.write("Center Number: 212-650-5327")
            st.write("You can email them at cpdi@ccny.cuny.edu ")
            shake("https://app.joinhandshake.com/login")
        elif college == "College of Staten Island":
            url = "http://www.csi.cuny.edu/career/"
            st.write("The Career Center at College of Staten Island is Called the [Center for Career and Professional Development](%s)" % url)
            st.write("The Center is located at 2800 Victory Boulevard Building 1A, Room 105 Staten Island, NY 10314")
            st.write("Center Number: 718-982 2300")
            st.write("You can email them at careers@csi.cuny.edu")
            shake("https://csicuny.joinhandshake.com/login?ref=app-domain")
        elif college == "CUNY School of Labor and Urban Studies":
            url = "https://slu.cuny.edu/academic-affairs/student-affairs/student-services/career-services/"
            st.write("The Career Center at CUNY School of Labor and Urban Studies is Called the [Career and Professional Development Center](%s)" % url)
            st.write("The Center is located at 25 W 43rd Street, 18th floor New York, NY 10036")
            st.write("Center Number: 646-313-8339")
            st.write("You can email them at careerservices@slu.cuny.edu")
            shake("https://slucuny.joinhandshake.com/login?ref=app-domain")
        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/student-services/career-services"
            st.write("The Career Center at CUNY School of Professional Studies is Called the [Office of Career Services](%s)" % url)
            st.write("The Center is located at 119 West 31st Street, 4th floor New York, NY 10001")
            st.write("Center Number: 646-664-8618")
            st.write("You can email them at career.services@sps.cuny.edu")
            shake("https://app.joinhandshake.com/login")
        elif college == "CUNY School of Public Health":
            url = "http://sph.cuny.edu/student-services/office-of-career-services/"
            st.write("The Career Center at CUNY School of Public Health is Called the [Office of Career Services](%s)" % url)
            st.write("The Center is located at 55 West 125th street, 5th floor New York, NY 10027")
            st.write("Center Number: 646-364-9644")
            st.write("You can email them at careerservices@sph.cuny.edu")
            shake("https://sphcuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Guttman Community College":
            url = "https://guttman.cuny.edu/"
            st.write("The Career Center at Guttman Community College is Called the [Center for Career Preparation & Partnerships](%s)" % url)
            st.write("The Center is located at 50 W. 40th St. New York, NY 10018")
            st.write("Center Number: 646-313-8066")
            st.write("You can email them at cpartnerships@guttman.edu")
            shake("https://guttman.joinhandshake.com/login?ref=app-domain")
        elif college == "Hostos Community College":
            url = "http://www.hostos.cuny.edu/cso/"
            st.write("The Career Center at Hostos Community College is Called the [Career Services](%s)" % url)
            st.write("The Center is located at Savoy Building, D210 Bronx, NY 10451")
            st.write("Center Number: 718-518-4468")
            st.write("You can email them at careerservices@hostos.cuny.edu")
            shake("https://hostos.joinhandshake.com/login?ref=app-domain")
        elif college == "Hunter College":
            url = "http://www.hunter.cuny.edu/studentservices/cds"
            st.write("The Career Center at Hunter College is Called the [Career Development Services](%s)" % url)
            st.write("The Center is located at 695 Park Avenue Room 805 E New York, NY 10021")
            st.write("Center Number: 212-772-4850")
            st.write("You can email them at career@hunter.cuny.edu")
            shake("https://huntercuny.joinhandshake.com/login?ref=app-domain")
        elif college == "John Jay College of Criminal Justice":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/career-services/campus-career-centers/#:~:text=John%20Jay%20College%20of%20Criminal%20Justice"
            st.write("The Career Center at John Jay College of Criminal Justice is Called the [Center for Career and Professional Development](%s)" % url)
            st.write("The Center is located at 524 West 59th StreetNew York, NY 10019")
            st.write("Center Number: 212-237-8754")
            st.write("You can email them at careers@jjay.cuny.edu")
            shake("https://jjaycuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Kingsborough Community College":
            url = "http://www.kingsborough.edu/career/"
            st.write("The Career Center at Kingsborough Community College is Called the [Center for Career Development & Experiential Learning](%s)" % url)
            st.write("The Center is located at Room C201 2001 Oriental Boulevard Brooklyn, NY 11235")
            st.write("Center Number: 718-368-5115")
            st.write("You can email them at careerdevelopment@kbcc.cuny.edu")
            shake("https://kbcc-cuny.joinhandshake.com/login?ref=app-domain")
        elif college == "LaGuardia Community College":
            url = "http://www.laguardia.cuny.edu/careerservices/"
            st.write("The Career Center at LaGuardia Community College is Called the [Center for Career & Professional Development](%s)" % url)
            st.write("The Center is located at 31-10 Thomson Avenue Room B114 Long Island City, NY 11101")
            st.write("Center Number: 718-482-5235")
            st.write("You can email them at career@lagcc.cuny.edu")
            shake("https://app.joinhandshake.com/login")
        elif college == "Lehman College":
            url = "http://www.lehman.edu/career-services/"
            st.write("The Career Center at Lehman College is Called the [Career Exploration & Development Center](%s)" % url)
            st.write("The Center is located at 250 Bedford Park Blvd. West, Shuster Hall, Room 254 Shuster Hall, Room 254 Bronx, NY 10468")
            st.write("Center Number: 718-960-8366")
            st.write("You can email them at career.services@lehman.cuny.edu")
            shake("https://lehmancuny.joinhandshake.com/login?ref=app-domain")
        elif college == "Macaulay Honors College":
            url = "https://macaulay.cuny.edu/after-macaulay/career-development/"
            st.write("The Career Center at Macaulay Honors College is Called the [Office of Career Development](%s)" % url)
            st.write("The Center is located at 35 West 67th Street New York, NY 10023")
            st.write("Center Number: 212-729-2947")
            st.write("You can email them at internships@mhc.cuny.edu")
            shake("https://mhc.joinhandshake.com/login?ref=app-domain")
        elif college == "Medgar Evers College":
            url = "https://ares.mec.cuny.edu/student-affairs/career-management-services/"
            st.write("The Career Center at Medgar Evers College is Called the [Office of Career Management Services](%s)" % url)
            st.write("The Center is located at Student Services Building1637 Bedford Avenue, Room S302 Brooklyn, NY 11225")
            st.write("Center Number: 718-270-6055")
            st.write("You can email them at CareerServices@mec.cuny.edu")
            shake("https://app.joinhandshake.com/login")
        elif college == "New York City College of Technology":
            url = "http://www.citytech.cuny.edu/pdc/"
            st.write("The Career Center at New York City College of Technology is Called the [Professional Development Center](%s)" % url)
            st.write("The Center is located at Room L-114 250 Jay Street Brooklyn, New York 11201")
            st.write("Center Number: 718-260-5050")
            st.write("You can email them at pdc@citytech.cuny.edu")
            shake("https://citytech.joinhandshake.com/login?ref=app-domain")
        elif college == "Queens College":
            url = "https://www.qc.cuny.edu/academics/cei/"
            st.write("The Career Center at Queens College is Called the [Center for Career Engagement and Internships](%s)" % url)
            st.write("The Center is located at 65-30 Kissena Boulevard Frese Hall, Room 213 Flushing, NY 11367")
            st.write("Center Number: 718-997-4465")
            st.write("You can email them at qc_career@qc.cuny.edu")
            shake("https://qc.joinhandshake.com/login?ref=app-domain")
        elif college == "Queensborough Community College":
            url = "http://www.qcc.cuny.edu/careerservices/"
            st.write("The Career Center at Queensborough Community College is Called the [Career Services](%s)" % url)
            st.write("The Center is located at Library Building, L-429222-05, 56th Avenue Bayside, NY 11364")
            st.write("Center Number: 718-631-6297")
            st.write("You can email them at careerservices@qcc.cuny.edu")
            shake("https://cunyqcc.joinhandshake.com/login?ref=app-domain")
        elif college == "York College":
            url = "http://york.cuny.edu/student-development/career-services"
            st.write("The Career Center at York College is Called the [The Office of Career Services](%s)" % url)
            st.write("The Center is located at 94-20 Guy Brewer Boulevard Room #3E03 Jamaica, NY 11451")
            st.write("Center Number: 718-262-2282")
            st.write("You can email them at career@york.cuny.edu")
            shake("https://app.joinhandshake.com/login")
    
    if check2:
        url = "https://www.cuny.edu/about/administration/offices/ocip/"
        st.write("Please follow this [link](%s) to be redirected to a plethora of CUNY Career Programs" % url)