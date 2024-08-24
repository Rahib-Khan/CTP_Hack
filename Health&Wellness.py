#Author: Rahib Khandaker
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
                       "Influenza (Flu)", "Infectious Disease Notification Protocol","Lactation Services"],
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
            st.write("The Health Services at Baruch College is Called the [Baruch College Health Services](%s)" % url)
            st.write("The Services are located at 138 E. 26th Street, 1st Fl. New York, NY 10010")
            st.write("Services Number: 646-312-2040")
            st.write("You can email them at StudentHealthCareCenter@baruch.cuny.edu")
            

        elif college == "Borough of Manhattan Community College":
            url = "https://www.bmcc.cuny.edu/student-affairs/health-services/"
            st.write("The Health Services at Borough of Manhattan Community College is Called the [BMCC Health Services](%s)" % url)
            st.write("The Services are located at 199 Chambers Street Room N-303 New York, NY 10007")
            st.write("Services Number: 212-220-8255")
            st.write("You can email them at healthservices@bmcc.cuny.edu")
            
        elif college == "Bronx Community College":
           url = "https://www.bmcc.cuny.edu/student-affairs/health-services/"
           st.write("The Health Services at Bronx Community College is Called the [BCC Office of Health Services](%s)" % url)
           st.write("The Services is located at West 181st St. & University Avenue, Loew Hall, Room 101 Bronx, NY 10453")
           st.write("Services Number: 718-289-5858")
           st.write("You can email them at healthservices@bcc.cuny.edu")
        elif college == "Brooklyn College":
            url = "https://www.brooklyn.cuny.edu/web/about/offices/studentaffairs/health-wellness/healthclinic.php"
            st.write("The Health Services at Brooklyn College is Called the [The Brooklyn College Health Clinic](%s)" % url)
            st.write("The Services is located at 2900 Bedford Avenue, 114 Roosevelt Hall Brooklyn, NY 11210")
            st.write("Services Number: 718-951-5580")
            st.write("You can email them at bchealthclinic@brooklyn.cuny.edu ")

        elif college == "City College of New York":
            url = "https://www.ccny.cuny.edu/health-wellness"
            st.write("The Health Services at City College of New York is Called the [The City College Student Health Services](%s)" % url)
            st.write("The Services is located at Marshak Science Building, Room J-15 138th Street & Convent Avenue New York, NY 10031")
            st.write("Services Number: 212-650-5327")
            st.write("You can email them at shs@ccny.cuny.edu ")

        elif college == "College of Staten Island":
            url = "http://www.csi.cuny.edu/studentaffairs/healthservices/"
            st.write("The Health Services at College of Staten Island is Called the [CSI Health and Wellness Services](%s)" % url)
            st.write("The Services is located at 2800 Victory Blvd., Room 1C-112 Staten Island, NY 10314")
            st.write("Services Number: 718-982 2300")
            st.write("You can email them at healthcenter@csi.cuny.edu")

        elif college == "CUNY School of Labor and Urban Studies":
            url = "https://slu.cuny.edu/academics/academics-2/counseling-wellness/"
            st.write("The Career Services at CUNY School of Labor and Urban Studies is Called the [Student Counseling and Wellness](%s)" % url)
            st.write("The Services is located at 25 West 43rd Street, 19th Floor New York, NY 10036")
            st.write("Services Number: 212-827-0200")
            st.write("You can email the wellness counsler, Lindsay Kazi, at lindsay.kazi@slu.cuny.edu")

        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/student-services/health-services"
            st.write("The Health Services at [CUNY School of Professional Studies](%s)" % url)
            st.write("The provided location is at 119 West 31st Street New York, NY 10001")
            st.write("Services Number: 212-652-CUNY ")
            st.write("You can email them at studentservices@sps.cuny.edu")

        elif college == "CUNY School of Public Health":
            url = "https://sph.cuny.edu/students/student-services/student-wellness/counseling-and-wellness-services/"
            st.write("The Health Services at CUNY School of Public Health is Called the [Counseling and Wellness Services](%s)" % url)
            st.write("The Services is located at 55 West 125th street, 5th floor New York, NY 10027")
            st.write("Services Number: 646-364-9644")

        elif college == "Guttman Community College":
            url = "https://guttman.cuny.edu/students/counseling-and-wellness-center/"
            st.write("The Health Services at Guttman Community College is Called the [Wellness Office](%s)" % url)
            st.write("The Services is located at 50 West 40th St, Room 506 New York, NY 10018")
            st.write("Services Number: 646-313-8000")
            st.write("You can email them at Counseling.wellness@guttman.cuny.edu")

        elif college == "Hostos Community College":
            url = "http://www.hostos.cuny.edu/sdem/health_wellness.html/"
            st.write("The Health Services at Hostos Community College is Called the [Hostos Community College Health Services](%s)" % url)
            st.write("The Services is located at Health Services 475 Grand Concourse A-334C Bronx, NY 10451")
            st.write("Services Number: 718-518-6542 or 718-518-6567")
   
        elif college == "Hunter College":
            url = "https://hunter.cuny.edu/students/health-wellness/"
            st.write("The Health Services at Hunter College is Called the [Hunter College Health & Support](%s)" % url)
            st.write("The Services is located at 695 Park Avenue Room 307, North New York, NY 10065")
            st.write("Services Number: 212-772-4800 212-772-4000")

        elif college == "John Jay College of Criminal Justice":
            url = "https://www.jjay.cuny.edu/wellness-health-services"
            st.write("The Health Services at John Jay College of Criminal Justice is Called the [John Jay College Health Services](%s)" % url)
            st.write("The Services is located at 524 West 59th StreetNew York, NY 10019")
            st.write("Services Number: 212-237-8754")
            st.write("You can email them at careers@jjay.cuny.edu")

        elif college == "Kingsborough Community College":
            url = "http://www.kbcc.cuny.edu/healthservices/index.html"
            st.write("The Health Services at Kingsborough Community College is Called the [Kingsborough Community College Health Center](%s)" % url)
            st.write("The Serives is located at Room A108 2001 Oriental Blvd. Brooklyn, NY 11235")
            st.write("Services Number: 718- 368-5684")
            st.write("You can email them at Health.Center@kbcc.cuny.edu")

        elif college == "LaGuardia Community College":
            url = "https://www.laguardia.edu/healthservices/"
            st.write("The Health Serives at LaGuardia Community College is Called the [LaGuardia Community College Health Services](%s)" % url)
            st.write("The Services is located at 31-10 Thomson Avenue Room MB-40 Long Island City, NY 11101")
            st.write("Services Number: 718-482-5408")
            st.write("You can email them at Health-Center@lagcc.cuny.edu")

        elif college == "Lehman College":
            url = "https://www.lehman.edu/student-health-center/"
            st.write("The Health Services at Lehman College is Called the [Lehman College The Student Health Center](%s)" % url)
            st.write("The Services is located at Old Gym, Room B008 250 Bedford Park Blvd. West Bronx, NY 10468-1589")
            st.write("Services Number: 718-960-8900")
            st.write("You can email them at med.requirements@lehman.cuny.edu")

        elif college == "Macaulay Honors College":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#healthservices:~:text=Mental%20Health%20%26%20Wellness%20Center"
            st.write("The Health Services at Macaulay Honors College is Called the [Mental Health & Wellness Center](%s)" % url)
            st.write("The Services is located at 35 W. 67th Street, New York, NY 10023")
            st.write("Services Number: 212-729-2914")
            st.write("You can email them atwellness@mhc.cuny.edu")
 
        elif college == "Medgar Evers College":
            url = "https://www.mec.cuny.edu/student-success/health-services/"
            st.write("The Career Services at Medgar Evers College is Called the [Medgar Evers College Health Services](%s)" % url)
            st.write("The Services is located at 1637 Bedford Avenue, Room S217 Brooklyn, NY 11225")
            st.write("Services Number: 718-270-6075 or 718-270-4900")
            st.write("You can email them at healthservices@mec.cuny.edu")

        elif college == "New York City College of Technology":
            url = "https://www.citytech.cuny.edu/wellness-center/"
            st.write("The Health Service at New York City College of Technology is Called the [New York City College of Technology Health Services](%s)" % url)
            st.write("The Service is located at 300 Jay Street General Bldg, Room 414 Brooklyn, NY 11201")
            st.write("Service Number: 718-260-5385 or 718-260-5910")
            st.write("You can email them at wellnesscenter@citytech.cuny.edu")

        elif college == "Queens College":
            url = "https://www.qc.cuny.edu/health/"
            st.write("The Health Services at Queens College is Called the [Queens College Health Services](%s)" % url)
            st.write("The Services is located at 65-30 Kissena Blvd. Frese Hall, 3rd Floor Flushing, NY 11367")
            st.write("Services Number: 718-997-2760")
            st.write("You can email them at healthquestions@qc.cuny.edu")

        elif college == "Queensborough Community College":
            url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#healthservices:~:text=Queensborough%20Community%20College%20Health%20Services"
            st.write("The Health Services at Queensborough Community College is Called the [Queensborough Community College Health Services](%s)" % url)
            st.write("The Services is located at 222-05 56th Avenue Medical Arts Building, Room MC-02 Bayside, NY 11364")
            st.write("Services Number: 718-631-6375")
            st.write("You can email them at HealthServices@qcc.cuny.edu")

        elif college == "York College":
            url = "https://www.york.cuny.edu/health"
            st.write("The Health Services at York College is Called the [York College Health Services](%s)" % url)
            st.write("The Services is located at 94-20 Guy Brewer Boulevard Room #3E03 Jamaica, NY 11451")
            st.write("Services Number: 718-262-2282")
            st.write("You can email them at StudHealthSvcCtr@york.cuny.edu")


    if health == "Health Insurance":
        url = ("https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#insurance")
        url2 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#gotinsurance"
        st.write("You can follow this link to find any information on obtaining [Health Insurance](%s)" % url)
        st.write("[If you already have insurance](%s)" % url2)
    
    if health == "Community Resources":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#comresources"
        url2 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#1691701649205-c3369359-1725"
        url3 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#1683737540708-e92f159c-f358"
        url4 = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#1619819868109-17cc6e25-4129"
        st.write("The [Community Resources](%s) are plentiful including information on")
        st.write("[Abortion Access](%s)" % url2)
        st.write("[STI Testing](%s)" % url3)   
        st.write("[Healthy Eating](%s)" % url4)
    if health == "Immunization Info":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#immunization"
        st.write("New York State Public Health Law 2165 requires all students entering a post-secondary institution to provide their health services center with immunity to Measles, Mumps and Rubella. This law applies to students born on or after January 1, 1957, who are registered for 6 or more credits at a CUNY campus. Proof of immunity must be documented by a health care practitioner or other acceptable evidence in the following way")
        st.write("Any other information can be found [here](%s)" % url)
    if health == "Influenza (Flu)":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#influenza"
        st.write("Information surronding [THE FLU](%s)" % url)
    if health == "Infectious Disease Notification Protocol":
        url = "https://www.cuny.edu/current-students/student-affairs/student-services/health-services/#idn-protocol"
        st.write("Please follow the Directions displayed at this [link](%s)" % url)
    if health == "Lactation Services":
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
            url = "https://hr.baruch.cuny.edu/lactation-room/"
            st.write("[Lactation Room Information Overview](%s) for Baruch College" % url)
            st.write("The lactation room is located in room #112 on the first floor of the Information and Technology Building.")        
        elif college == "Borough of Manhattan Community College":
            url = "https://www.bmcc.cuny.edu/student-affairs/womens-resource-center/lactation/"
            st.write("[Lactation Room Info](%s) for Borough of Manhattan Community College" % url)
        elif college == "Bronx Community College":
            st.write("The Lactation Room for Bronx Community College is located at Loew Hall Room 105 and it is open to students, faculty, and staff")
        elif college == "Brooklyn College":
            st.write("A Lactation room is available for nursing mothers (faculty, staff and students) in the Early Childhood Center in 1604 James Hall and in the John Whyte Room, 303 Student Center.")
            st.write("Open Mon-Thu 8:30am-10:30pm & Fri 8:30am-5:00pm.")
        elif college == "City College of New York":
            st.write("City College of NY Lactation Room accommodations are available at Student Health Services, Marshak Science Building, 4th Floor, Room 418-S (Temporary location during renovation) during office hours Monday-Friday 9am-5pm")
        elif college == "College of Staten Island":
            url = "https://csitoday.com/2017/04/lactation-room/"
            st.write("Here is some information on the [Lactation Room](%s) at CSI"% url)
            st.write("Located in the Center for the Arts (Building 1P), Room 1P-008 has been designated as a lactation room for College of Staten Island faculty, staff, and students (as available). The room is located on the lower level, and is accessible from the west elevator in the Atrium. Those seeking to use the lactation room should present their current CSI ID to the Office of the Vice President for Finance and Administration, Building 1A, Room 309. Keys for the room will be issued through that Office.")
        elif college == "CUNY Graduate Center":
            st.write("A dedicated space has been established at The Graduate Center for mothers to express breast milk for a nursing child. Room 7408, also called the Mothers' Room, is available to all nursing women students and employees who present a current Graduate Center ID. Those wishing to use the Mothers’ Room should fill out a one-time key request form in the Student Affairs office, Room 7301. Nursing mothers may also use the Child Care Center (until 5 p.m.) for the same purpose, ring the bell for Room 3201")
        elif college == "CUNY School of Law":
            st.write("The lactation room, located in room 2-101, is available to students, staff, or faculty who wish to use the room. Please direct inquiries to the Office of Student Affairs, room 5-110, (718) 340-4207 or email studentaffairsoffice@mail.law.cuny.edu.")
        elif college == "CUNY School of Professional Studies":
            url = "https://sps.cuny.edu/about/policies/facilities-policies/mother%E2%80%99s-room-policy"
            st.write("Here is Info on the [Mother Rooms]")
            st.write("All students, staff, faculty, and visitors can use the lactation room on the 10th floor opposite the elevator during hours of operation")
        elif college == "CUNY School of Public Health":
            url = "https://sph.cuny.edu/life-at-sph/lactation-support-room/"
            st.write("Here is information on the [Lactation Support Room](%s)" % url)
            st.write("All students, faculty, staff and visitors may use the Lactation Support Room in Room 819 where you will find a comfortable chair, a counter, and a refrigerator for storing your milk, snacks and beverages.")
        elif college == "Guttman Community College":
            st.write("Guttman has a room dedicated to lactation and will be made available based on availability, on a first-come, first-served basis. If you have any questions or would like to make a reservation for the lactation room, please email hr@guttman.cuny.edu.")
        elif college == "Hostos Community College":
            st.write("Hostos has established the following spaces as available lactation rooms:")
            st.write("Students: Health Services Office, “A Building” Room A-334C: Monday-Thursday 9am-5pm")
            st.write("To gain access, students should call the Health Services Office at 718-518-6542")
            st.write("Or send an email to CJoseph@hostos.cuny.edu. A response will be given within a “reasonable” amount of time not to exceed five business days.")
        elif college == "Hunter College":
            st.write("A lactation room is available to Hunter students, faculty, and staff at Brookdale: Room E117 (East Building) is the first room to your right when entering the Rotunda Foyer. For access, guests must first submit an online request form to have their Hunter OneCard authorized for keyless entry. Please specify that your request is for the Brookdale Campus and allow up to 2 business days for your card to be authorized. For questions, contact the OneCard office at 212-650-3191 or onecard@hunter.cuny.edu.")
        elif college == "John Jay College of Criminal Justice":
            st.write("The Lactation Room is the last door on your right, adjacent to the All-Gender Locker Room. The lactation space locks from the inside, there is a table, chair, access to an electrical outlet and sink. Unfortunately, it does not have a refrigerator. Secure, refrigerated storage is available for students and staff in the Women’s Center for Gender Justice located in room L.67.")
        elif college == "Kingsborough Community College":
            st.write("The Health Center at KBCC has space for lactation open to everyone- students, staff, and visitors.")
            st.write("Open 9-5 Mon Thurs Fri 9am-5pm and Tues- Wed 9am-8pm")
        elif college == "LaGuardia Community College":
            st.write("Students can request/reserve the lactation room in the Wellness Center C building Room 349. Form is on-line. Staff ad faculty must go to HR for sign up sheet on-line to reserve time. Lactation room is in Lower Lobby M building Room MB60 basement. An id is required.")
        elif college == "Lehman College":
            form = "http://goo.gl/forms/8vpLQcyJQA"
            url = "https://www.lehman.edu/student-health-center/wellness-education-promotion/breastfeeding-support-services/"
            st.write("Lehman College has this website for [breastfeeding information].")
            st.write("The lactation room is available by request to all students enrolled at the college as well as faculty and staff. The lactation room is located in Carman Hall, room 187.")
            st.write("To request access, complete the [lactation request form](%s)." % form)
        elif college == "Medgar Evers College":
            url = "https://www.mec.cuny.edu/student-success/health-services/lactation-room/"
            st.write("Here is website on the [Lactation Room](%s)" % url)
            st.write("On campus there are two lactation rooms available to both working and student mothers to use. One is in the Student Building (S-Building) Office of Health Services Room 217 and the other is located in The Center for Women's Development in the Carroll Street Building (C-Building) Room C-M2.")
        elif college == "New York City College of Technology":
            st.write("Lactation room is available to students, staff, faculty, and visitors at the Student Wellness Center M, T, W, Th 9am-5:30pm. Located in the Academic Bldg. ALL110")
        elif college == "Queens College":
            st.write("The Lactation room at Queens College is in Kiely 134E. It is open to students, faculty, and staff. Health Services request a form filled out to get the key.  Once the key is given, they can access the room and refrigerator during evening hours.")
        elif college == "Queensborough Community College":
            st.write("Lactation rooms are available in Health Services Mon-Thursday 9am-5pm. Student Activities also have a room for nursing mothers.")
        elif college == "York College":
            url = "https://www.york.cuny.edu/womens-center/lactation-services"
            form = "https://reservations.york.cuny.edu/lactation"
            st.write("Here is the website info on the [Lactation Room](%s)" % url)
            st.write("The room is located in the Academic Core Building Room 1H11.  If there room is locked you may go to Public Safety (AC-1M01) and ask them to unlock it for you.")
            st.write("You can reserve the room with this [form](%s)" % form)
