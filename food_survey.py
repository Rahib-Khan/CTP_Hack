import streamlit as st
import streamlit_survey as ss

class cuny_pantry:
    def __init__(self, college, website, location, email, phone, appointment):
        self.college = college
        self.website = website
        self.location = location
        self.email = email
        self.phone = phone
        self.appointment = appointment

bcc_pantry = cuny_pantry('Bronx Community College', 
                         'https://www.bcc.cuny.edu/campus-resources/access-resource-center/food-pantry/', 
                         'Access Resource Center office: Loew Hall 125', 
                         'bcc.ARC@bcc.cuny.edu', 
                         '718-289-5179', 
                         '')

hcc_pantry = cuny_pantry('Hostos Community College', 
                         'https://www.hostos.cuny.edu/Programs/One-Stop-Resource-Center', 
                         'Hostos One Stop Center, Savoy Building (1st floor intake) D-101', 
                         'mcruz@hostos.cuny.edu', 
                         '718-518-4141', 
                         '')

lc_pantry = cuny_pantry('Lehman College', 
                        'https://www.lehman.edu/student-leadership/lehman-food-bank.php', 
                        'Student Life Building 120', 
                        'food.bank@lehman.cuny.edu', 
                        '718-960-8535', 
                        '')

bc_pantry = cuny_pantry('Brooklyn College', 
                        'https://www.brooklyn.cuny.edu/web/about/offices/studentaffairs/student-support-services/food-pantry.php', 
                        'Student Center, Room 524', 
                        'civicengagement@brooklyn.cuny.edu', 
                        '', 
                        '')

kcc_pantry = cuny_pantry('Kingsborough Community College', 
                         'https://www.kbcc.cuny.edu/studres/cunyedge.html', 
                         'CUNY EDGE, T4-216 (Food for Thought)', 
                         '718-368-4660', 
                         '', 
                         '')

mec_pantry = cuny_pantry('Medgar Evers College', 
                         'https://ares.mec.cuny.edu/student-affairs/transition-academy/', 
                         'Transition Academy, 1150 Carroll Street (Room C-307)', 
                         'transitionacademy@mec.cuny.edu', 
                         '718-270-6988', 
                         '')

nct_pantry = cuny_pantry('NYC College of Technology (City Tech)', 
                         'https://www.citytech.cuny.edu/student-life/food-pantry.aspx', 
                         'Yellowjacket N.E.S.T. (Nutrition for Education and Student Achievement) Food Pantry at City Tech, 300 Jay Street, Student Life, G-516.', 
                         '', 
                         '', 
                         'https://calendly.com/geramirez-1/pantryhttps://calendly.com/geramirez-1/pantry')

bar_pantry = cuny_pantry('Baruch College', 
                         'https://studentaffairs.baruch.cuny.edu/dean-of-students/bearcat-food-pantry/', 
                         'deanofstudents@baruch.cuny.edu', 
                         '', 
                         '646-312-4570', 
                         'https://baruch.az1.qualtrics.com/jfe/form/SV_0fwrpgDtATh3qC2')
 
bmcc_pantry = cuny_pantry('Borough of Manhattan Community College', 
                          'https://www.bmcc.cuny.edu/student-affairs/arc/panther-pantry/', 
                          'Advocacy and Resource Center, Panther Pantry, Room S-230', 
                          'arc@bmcc.cuny.edu', 
                          '212-220-8195', 
                          '')

ccny_pantry = cuny_pantry('City College of New York', 
                          'https://www.ccny.cuny.edu/bennysfoodpantry', 
                          'NAC Ground Floor', 
                          'bennysfoodpantry@ccny.cuny.edu', 
                          '', 
                          'https://calendly.com/bennysfoodpantry/benny-s-food-pantry-appointment-system?month=2023-03 or stop by Mon-Fri 10am-6pm.') 

gutt_pantry =  cuny_pantry('Guttman Community College', 
                           'https://guttman.cuny.edu/students/connect-center/food-resources/', 
                           'The Connect Center, Room LL020/021', 
                           'connectcenter@guttman.cuny.edu', 
                           '646-313-8857',
                           '')

hc_pantry = cuny_pantry('Hunter College', 
                        'https://ww2.hunter.cuny.edu/students/student-life/emergency-support-and-resources/', 
                        'Main Campus 68th Street, West Building Room B103\n Brookdale Campus, Main Floor Lobby', 
                        'rt2049@hunter.cuny.edu', 
                        '', 
                        '')

jj_pantry = cuny_pantry('John Jay College', 
                        'https://www.jjay.cuny.edu/john-jay-food-bank', 
                        'Wellness Center/Single Stop Rm L.68.13', 
                        'JJCFoodBank@jjay.cuny.edu', 
                        '212-237-8052', 
                        '')

lcc_pantry = cuny_pantry('LaGuardia Community College', 
                         'https://www.laguardia.edu/cares/', 
                         'LaGuardia Cares, Room C-107', 
                         'Laguardiacare@lagcc.cuny.edu', 
                         '718-482-5135', 
                         '')

qc_pantry = cuny_pantry('Queens College', 
                        'https://qcknightstable.org/', 
                        'Student Union, Lower Level, 29', 
                        'team@qcknightstable.org', 
                        '718-570-0393', 
                        '')

qcc_pantry = cuny_pantry('Queensborough Community College', 
                         'http://www.qcc.cuny.edu/foodPantry/index.html', 
                         'Student Union, SU 115', 
                         'etai@qcc.cuny.edu', 
                         '', 
                         '')

sj_pantry = cuny_pantry('School of Journalism', 
                        '', 
                        'Student Affairs', 
                        'anthony.laviscount@journalism.cuny.edu', 
                        '', 
                        '')

sl_pantry = cuny_pantry('School of Law', 
                        '', 
                        'Student Affairs', 
                        'amanda.beltran@law.cuny.edu', 
                        '718-340-4204', 
                        '')

y_pantry =  cuny_pantry('York College', 
                        'https://www.york.cuny.edu/news/the-food-pantry-is-open--ready-to-serve-you', 
                        'Room 3M02 –The Men’s Center', 
                        'foodpantry@york.cuny.edu', 
                        '718-262-2008', 
                        '')

csi_pantry = cuny_pantry('College of Staten Island', 
                         'http://csitoday.com/2016/02/csi-food-pantry/', 
                         'Office of Student Life in the Campus Center, 1C-201', 
                         'studentlife@csi.cuny.edu', 
                         '718-982-3088', 
                         '')

survey = ss.StreamlitSurvey("Survey Example - Advanced Usage")

st.write("What Type of Aid Are you looking for?")
aid = survey.radio("Issues",
        options=["Food Insecurity", "Housing Instability", "Child Care", "Career Development", "Disability Services", "Mental Health", "Addiction Services", "Health And Wellness"],
        index= None,
        label_visibility="collapsed",
        horizontal=True,
    )

if aid == "Food Insecurity":
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
                st.write('Website: '+bar_pantry.website)
                st.write('Location: '+bar_pantry.location)
                st.write('Email: '+bar_pantry.email)
                st.write('Phone: '+bar_pantry.phone)
                st.write('Appointment: '+bar_pantry.appointment)
        
        elif college == "Borough of Manhattan Community College":
                st.write('Website: '+bmcc_pantry.website)
                st.write('Location: '+bmcc_pantry.location)
                st.write('Email: '+bmcc_pantry.email)
                st.write('Phone: '+bmcc_pantry.phone)
                st.write('Appointment: '+bmcc_pantry.appointment)
        
        elif college == "Bronx Community College":
                st.write('Website: '+bmcc_pantry.website)
                st.write('Location: '+bmcc_pantry.location)
                st.write('Email: '+bmcc_pantry.email)
                st.write('Phone: '+bmcc_pantry.phone)
                st.write('Appointment: '+bmcc_pantry.appointment)
            
        elif college == "Brooklyn College":
                st.write('Website: '+bc_pantry.website)
                st.write('Location: '+bc_pantry.location)
                st.write('Email: '+bc_pantry.email)
                st.write('Phone: '+bc_pantry.phone)
                st.write('Appointment: '+bc_pantry.appointment)
          
        elif college == "City College of New York":
                st.write('Website: '+ccny_pantry.website)
                st.write('Location: '+ccny_pantry.location)
                st.write('Email: '+ccny_pantry.email)
                st.write('Phone: '+ccny_pantry.phone)
                st.write('Appointment: '+ccny_pantry.appointment)
            
        elif college == "College of Staten Island":
                if csi_pantry.
                st.write('Website: '+csi_pantry.website)
                st.write('Location: '+csi_pantry.location)
                st.write('Email: '+csi_pantry.email)
                st.write('Phone: '+csi_pantry.phone)
                st.write('Appointment: '+csi_pantry.appointment)
           
        elif college == "CUNY School of Law":
                st.write('Website: '+sl_pantry.website)
                st.write('Location: '+sl_pantry.location)
                st.write('Email: '+sl_pantry.email)
                st.write('Phone: '+sl_pantry.phone)
                st.write('Appointment: '+sl_pantry.appointment)

        elif college == "Hostos Community College":
                st.write('Website: '+hcc_pantry.website)
                st.write('Location: '+hcc_pantry.location)
                st.write('Email: '+hcc_pantry.email)
                st.write('Phone: '+hcc_pantry.phone)
                st.write('Appointment: '+hcc_pantry.appointment)

        elif college == "Hunter College":
                st.write('Website: '+hc_pantry.website)
                st.write('Location: '+hc_pantry.location)
                st.write('Email: '+hc_pantry.email)
                st.write('Phone: '+hc_pantry.phone)
                st.write('Appointment: '+hc_pantry.appointment)
          
        elif college == "John Jay College of Criminal Justice":
                st.write('Website: '+jj_pantry.website)
                st.write('Location: '+jj_pantry.location)
                st.write('Email: '+jj_pantry.email)
                st.write('Phone: '+jj_pantry.phone)
                st.write('Appointment: '+jj_pantry.appointment)
        
        elif college == "Kingsborough Community College":
                st.write('Website: '+kcc_pantry.website)
                st.write('Location: '+kcc_pantry.location)
                st.write('Email: '+kcc_pantry.email)
                st.write('Phone: '+kcc_pantry.phone)
                st.write('Appointment: '+kcc_pantry.appointment)
            
        elif college == "LaGuardia Community College":
                st.write('Website: '+lcc_pantry.website)
                st.write('Location: '+lcc_pantry.location)
                st.write('Email: '+lcc_pantry.email)
                st.write('Phone: '+lcc_pantry.phone)
                st.write('Appointment: '+lcc_pantry.appointment)
          
        elif college == "Lehman College":
                st.write('Website: '+lc_pantry.website)
                st.write('Location: '+lc_pantry.location)
                st.write('Email: '+lc_pantry.email)
                st.write('Phone: '+lc_pantry.phone)
                st.write('Appointment: '+lc_pantry.appointment)
          
        elif college == "Medgar Evers College":
                st.write('Website: '+mec_pantry.website)
                st.write('Location: '+mec_pantry.location)
                st.write('Email: '+mec_pantry.email)
                st.write('Phone: '+mec_pantry.phone)
                st.write('Appointment: '+mec_pantry.appointment)
        
        elif college == "New York City College of Technology":
                st.write('Website: '+nct_pantry.website)
                st.write('Location: '+nct_pantry.location)
                st.write('Email: '+nct_pantry.email)
                st.write('Phone: '+nct_pantry.phone)
                st.write('Appointment: '+nct_pantry.appointment)
           
        elif college == "Queens College":
                st.write('Website: '+qc_pantry.website)
                st.write('Location: '+qc_pantry.location)
                st.write('Email: '+qc_pantry.email)
                st.write('Phone: '+qc_pantry.phone)
                st.write('Appointment: '+qc_pantry.appointment)
            
        elif college == "York College":
                st.write('Website: '+y_pantry.website)
                st.write('Location: '+y_pantry.location)
                st.write('Email: '+y_pantry.email)
                st.write('Phone: '+y_pantry.phone)
                st.write('Appointment: '+y_pantry.appointment)