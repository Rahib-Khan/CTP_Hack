import streamlit as st
import streamlit_survey as ss

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")
# Function to redirect students to other childcare programs
other_resources= "https://www.cuny.edu/academics/current-initiatives/office-of-early-childhood-initiatives/childhood/#1677039908238-a0b79be9-e9c2"
def no(other_resources):
    st.write("Sorry. Unfortunatley it looks like your College doesn't provide a direct Child Care service that fits your needs. However, there are other programs that may be able to help you.")
    st.write("Please follow this [LINK](%s)" % other_resources)

#How to start every path for each question
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
    "York College", 
    "Other"
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
        if confirm == "Yes":
            Center_url= "https://studentaffairs.baruch.cuny.edu/early-learning-center/"
            Location_url = "https://www.google.com/maps/place/1+Bernard+Baruch+Way,+New+York,+NY+10010/@40.740181,-73.9841493,18.42z/data=!4m5!3m4!1s0x89c259a752b00719:0xf5c500d480255408!8m2!3d40.74016!4d-73.9833505?shorturl=1"
            st.write("The Child Care Center at Baruch College is Called the [Early Learning Center](%s)" % Center_url)
            st.write("Located at [Box G-1063, 1 Bernard Baruch Way, New York, NY 10010](%s)" % Location_url)
            st.write("Center Numbers: 212-387-1420 or 212-387-1421 | C: 646-261-2451")
            st.write("The Center Director is Lorraine Mondesir")

        elif confirm == "No":
            no(other_resources)

    elif college == "Borough of Manhattan Community College":
        st.write("Is your child between the ages of 3 Months and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.bmcc.cuny.edu/student-affairs/ecc/"
            Location_url = "https://goo.gl/maps/tUPqPnPtAGsjohhB8"
            st.write("The Child Care Center at Borough of Manhattan Community College is Called the [Borough of Manhattan Community College Early Childhood Center Inc](%s)" % Center_url)
            st.write("Located at [Room N375, 199 Chambers Street, New York, NY 10007](%s)" % Location_url)
            st.write("Center Numbers: 212-220-8250 or 212-220-8251")
            st.write("The Center Director is Cecilia Scott-Croff")
            st.write("Hours: Mon to Thu 7:45AM - 9PM | Fri 7:45AM - 6PM | Sat 7:45AM - 6PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "Bronx Community College":
        st.write("Is your child between the ages of 6 weeks and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.bcc.cuny.edu/campus-resources/early-childhood-center/"
            Location_url = "https://goo.gl/maps/gSGmYBosNAqwvkof9"
            st.write("The Child Care Center at Bronx Community College is Called the [Child Development Center](%s)" % Center_url)
            st.write("Located at [2155 University Avenue Bronx, NY 10453](%s)" % Location_url)
            st.write("Center Number: 718-289-5461")
            st.write("The Center Director is Jitinder Walia")
            st.write("Hours: Pre-School: Mon to Thu 7:30AM to 8PM | Fri 7:30AM-5:30PM) (Infant/Toddlers: Mon to Thu 8AM-4PM) (School Age: Mon to Thu 3PM-8PM")

        elif confirm == "No":
            no(other_resources)
             
    elif college == "Brooklyn College":
        st.write("Is your child between the ages of 4 Months and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.brooklyn.edu/dosa/student-support-services/csds/"
            Location_url = "https://goo.gl/maps/HJiEHpifaEZhvk7b7"
            st.write("The Child Care Center at Brooklyn College is Called the [The Early Childhood Center Programs](%s)" % Center_url)
            st.write("Located at [1604 James Hall, Bedford Avenue & Avenue H, Brooklyn, NY 11210](%s)" % Location_url)
            st.write("Center Number: 718-951-5431")
            st.write("The Center Director is Kaity Kapetan")
            st.write("Hours: Mon to Fri 8:30AM-4:30PM")

        elif confirm == "No":
            no(other_resources)
             
    elif college == "City College of New York":
        st.write("Is your child between the ages of 4 Months and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.ccny.cuny.edu/cdc"
            Location_url = "https://goo.gl/maps/nwtXcwpfDy87TLAG7"
            st.write("The Child Care Center at City College of New York is Called the [Campus Child Development Center](%s)" % Center_url)
            st.write("Located at [Schiff House, 119 Convent Avenue, New York, NY 10031](%s)" % Location_url)
            st.write("Center Numbers: 212-650-7679")
            st.write("The Center Director is Chanda Huston")
            st.write("Hours: Mon to Fri 7:30AM to 5:30PM")

        elif confirm == "No":
            no(other_resources)
             
    elif college == "College of Staten Island":
        st.write("Is your child between the ages of 6 Months and 9 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.csi.cuny.edu/campus-life/student-services/childrens-center"
            Location_url = "https://goo.gl/maps/3F2v6rcntjk5mvTJ9"
            st.write("The Child Care Center at College of Staten Island is Called the [The Children's Center](%s)" % Center_url)
            st.write("Located at [2R-104, 2800 Victory Boulevard, Staten Island, NY 10314](%s)" % Location_url)
            st.write("Center Numbers: 718-982-3190")
            st.write("The Center Director is Margaret Rooney")
            st.write("Hours: Mon to Fri 7AM - 6:30PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "CUNY Graduate Center":
        st.write("Is your child between the ages of 2 Years and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.gc.cuny.edu/Prospective-Current-Students/Student-Life/Resources/Child-Development-and-Learning-Center"
            Location_url = "https://goo.gl/maps/ypTJ2CiG1UUX2koQ9"
            st.write("The Child Care Center at CUNY Graduate Center is Called the [The Child Development and Learning Center](%s)" % Center_url)
            st.write("Located at [Suite 3201, 365 Fifth Avenue, New York, NY 10016](%s)" % Location_url)
            st.write("Center Numbers: 212-817-7033")
            st.write("The Center Director is Molly Polin")
            st.write("Hours:  Mon to Thu 9AM to 5PM | Fri 9AM to 4PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "CUNY School of Law":
        st.write("Is your child between the ages of 6 Months and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.laguardia.edu/eclc/"
            Location_url = "https://goo.gl/maps/Tjm6vpu27PFm84X86"
            st.write("The Child Care Center for CUNY School of Law is shared with LaGuardia Community College and is Called the [Early Childhood Learning Center Programs](%s)" % Center_url)
            st.write("Located at [Room MB09, 31-10 Thomson Avenue, Long Island City, NY 11101](%s)" % Location_url)
            st.write("Center Numbers: 718-482-5295")
            st.write("The Center Director is Sonya Evariste")
            st.write("Hours: Mon to Fri 7:50AM to 5PM | Sat 8AM to 3PM (During Spring & Fall only)")

        elif confirm == "No":
            no(other_resources)

    elif college == "Hostos Community College":
        st.write("Is your child between the ages of 6 Weeks and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.hostos.cuny.edu/Administrative-Offices/SDEM/Children-s-Center"
            Location_url = "https://goo.gl/maps/jtGvpVyegw7R7hix5"
            st.write("The Child Care Center for Hostos Community College is Called the [Children's Center](%s)" % Center_url)
            st.write("Located at [475 Grand Concourse, Bronx, NY 10451](%s)" % Location_url)
            st.write("Center Numbers: 718-518-4176")
            st.write("The Center Director is Catherine Garcia-Bou")
            st.write("Hours: Mon to Fri 7:45AM to 5PM")

        elif confirm == "No":
            no(other_resources)
        
    elif college == "Hunter College":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "http://www.hunter.cuny.edu/studentservices/clc"
            Location_url = "https://goo.gl/maps/Czxt3nUmrkzNc3xd7"
            st.write("The Child Care Center for Hunter College is Called the [The Children's Learning Center](%s)" % Center_url)
            st.write("Located at [Room 207N, 695 Park Avenue, New York, NY 10065](%s)" % Location_url)
            st.write("Center Numbers: 212-772-4066")
            st.write("The Center Director is Rittela F Letellier")
            st.write("Hours: Mon to Thu 8AM to 7PM | Fri 8AM to 3PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "John Jay College of Criminal Justice":
        st.write("Is your child between the ages of 6 Months and 5 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "http://www.jjay.cuny.edu/childrens-center"
            Location_url = "https://goo.gl/maps/aGRu9i3p2o2LXF9L6"
            st.write("The Child Care Center for John Jay College of Criminal Justice is Called the [Children's Center](%s)" % Center_url)
            st.write("Located at [860 11th Avenue, New York, NY 10019](%s)" % Location_url)
            st.write("Center Numbers: 212-393-6438")
            st.write("The Center Director is Linda Soleyn")
            st.write("Hours: Mon to Thu 7:30AM to 6PM | Fri-7:30AM to 3:30PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "Kingsborough Community College":
        st.write("Is your child between the ages of 2 Years & 10 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.kbcc.cuny.edu/childcenter/Homepage.html"
            Location_url = "https://goo.gl/maps/bt3mb7yHX73LE8hg8"
            st.write("The Child Care Center for Kingsborough Community College is Called the [Child Development Center](%s)" % Center_url)
            st.write("Located at [Room V105, 2001 Oriental Blvd. Brooklyn, NY 11235](%s)" % Location_url)
            st.write("Center Numbers: 718-368-5439")
            st.write("The Center Director is Latasha Collins")
            st.write("Hours: Mon to Thu 7:30AM to 5:30PM | Fri 7:30AM-4:30PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "LaGuardia Community College":
        st.write("Is your child between the ages of 6 Months and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.laguardia.edu/eclc/"
            Location_url = "https://goo.gl/maps/Tjm6vpu27PFm84X86"
            st.write("The Child Care Center for LaGuardia Community College is Called the [Early Childhood Learning Center Programs](%s)" % Center_url)
            st.write("Located at [Room MB09, 31-10 Thomson Avenue, Long Island City, NY 11101](%s)" % Location_url)
            st.write("Center Numbers: 718-482-5295")
            st.write("The Center Director is Sonya Evariste")
            st.write("Hours: Mon to Fri 7:50AM to 5PM | Sat 8AM to 3PM (During Spring & Fall only)")

        elif confirm == "No":
            no(other_resources)

    elif college == "Lehman College":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "http://www.lehman.edu/child-care-center/"
            Location_url = "https://goo.gl/maps/4D4VScMSyuTpQ5rR9"
            st.write("The Child Care Center for Lehman College is Called the [Child Care Center](%s)" % Center_url)
            st.write("Located at [2870 Goulden Avenue, Bronx, NY 10468](%s)" % Location_url)
            st.write("Center Numbers: 718-960-7436")
            st.write("The Center Director is Jaci Maurer")
            st.write("Hours: Mon to Thu 7:30AM to 5:30PM | Fri 7:30AM to 5PM | For Preschool & School Age programs Mon to Thu 3PM to 9:30PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "Medgar Evers College":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Location_url = "https://goo.gl/maps/DPL54MTpNKBrXMjdA"
            st.write("The Child Care Center for Medgar Evers College is Called the Child Care Center")
            st.write("Located at [Room C103, 1150 Carroll Street, Brooklyn, NY 11225](%s)" % Location_url)
            st.write("Center Numbers: 718-270-6018")
            st.write("The Center Director is Juanita Crafton")
            st.write("Hours: Mon to Thu 7:45AM to 10PM | Fri 7:45AM to 3PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "New York City College of Technology":
        st.write("Is your child between the ages of 2 Years and 12 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "http://www.citytech.cuny.edu/occ/"
            Location_url = "https://goo.gl/maps/woyzZxdHkoYQGST3A"
            st.write("The Child Care Center for New York City College of Technology is Called the [Child Care Center](%s)" % Center_url)
            st.write("Located at [Room G-309 and Room NG14, 300 Jay Street, Brooklyn, NY 11201](%s)" % Location_url)
            st.write("Center Numbers: 718-260-5192")
            st.write("The Center Director is Elizabeth Leone")
            st.write("Hours: Mon to Fri 7:30AM to 9:30PM | Sat 8AM to 4:30PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "Queens College":
        st.write("Is your child between the ages of 30 Months and 10 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Location_url = "https://goo.gl/maps/EH5gWApauWWfSW5j7"
            st.write("The Child Care Center for Queens College is Called the Child Development Center")
            st.write("Located at [Room 245, Kiely Hall, 65-30 Kissena Blvd, Flushing, NY 11367](%s)" % Location_url)
            st.write("Center Numbers: 718-997-5885")
            st.write("The Center Director is Eric Urevich")
            st.write("Hours: Mon to Thu 9AM-5PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "York College":
        st.write("Is your child between the ages of 6 Months and 10 Years?")
        confirm = survey.radio(
                "Confirm",
                options=["Yes", "No"],
                index= None,
                label_visibility="collapsed",
                horizontal=True,
            )
        if confirm == "Yes":
            Center_url= "https://www.york.cuny.edu/student-development/child-and-family-center"
            Location_url = "https://goo.gl/maps/S78GDgCWmeMSdBVcA"
            st.write("The Child Care Center for York College is Called the [York College Child and Family Center, Inc.](%s)" % Center_url)
            st.write("Located at [94-12 160th street, Jamaica, New York 11451](%s)" % Location_url)
            st.write("Center Numbers:/n 718-262-2930")
            st.write("The Center Director is Charlene Dertinger")
            st.write("Hours: Mon to Thu 8AM to 6PM | Fri 8AM to 4PM")

        elif confirm == "No":
            no(other_resources)

    elif college == "Other":
        no(other_resources)
        
