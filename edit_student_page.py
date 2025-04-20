from flet import *
from database import Database
import base64


db=Database()

#when get image from databaae in str format  in set_values_on_textfileds fucntion
# than assign to it variable
image_str = ""
gender_var = ""

class EditStudent:
    def __init__(self,page:Page):
        self.page = page
        # ************************************* make ref form TextField start **********************************************
        self.class_name = Ref[TextField]()
        
        self.rig_no_ref =  Ref[TextField]()
        self.first_name_ref =  Ref[TextField]()
        self.last_name_ref =  Ref[TextField]()
        self.father_name_ref =   Ref[TextField]()
        self.age_ref =   Ref[TextField]()
        self.cnic_ref =   Ref[TextField]()
        self.father_cnic_ref =   Ref[TextField]()
        self.date_of_birth_ref =   Ref[TextField]()
        self.mobile_ref =   Ref[TextField]()
        self.province_ref =   Ref[TextField]()
        self.postel_addres_ref =   Ref[TextField]()
        self.permanent_addres_ref =   Ref[TextField]()
        self.email_ref =  Ref[TextField]()
        # self.gender_ref= Ref[RadioGroup]()

        # metric information ref 
        self.metric_bord_ref  =   Ref[TextField]()
        self.school_name_ref =   Ref[TextField]()
        self.metric_total_ref =   Ref[TextField]()
        self.metric_obt_ref =   Ref[TextField]()
        self.metric_percentage_ref =   Ref[TextField]()
        self.metric_grade_ref =   Ref[TextField]()


        # FSc information_ref
        self.fsc_bord_ref  =   Ref[TextField]()
        self.collage_name_ref =   Ref[TextField]()
        self.fsc_total_ref =   Ref[TextField]()
        self.fsc_obt_ref =   Ref[TextField]()
        self.fsc_percentage_ref =   Ref[TextField]()
        self.fsc_grade_ref =   Ref[TextField]()

        self.error_text_ref = Ref[Text]()
        # ************************************* make ref form TextField end **********************************************

    

    def get_row(self,row, database_name):
        print("\n\n\n\n\n\n\n  calling.......")
        # print(row)

        self.row = row # when click on edit btn which is locatec in managment page than call it fucntion it accect a row of record database name
        
        self.database_name = database_name  # when click on edit btn which is locatec in managment page than call it fucntion it accect a row of record and database name
        self.page.views.clear()
        self.page.views.append(
            self.edit_student_page()
        )
        self.page.update()
        
        # set_values_on_textfileds Fuction call that set values on text field from managment page datatable
        self.set_values_on_textfileds()


    # # # GET ROW FROM DATABASE WHEN YOU CLICK ON EDIT ICON IN MANAGMENT PAGE 
    def set_values_on_textfileds(self):
        
        # # SET VALUES ON PERSNAL INFORMATION TEXTFIELDS

        self.class_name.current.value = self.database_name

        self.rig_no_ref.current.value = self.row[0] # index of rig number
        self.first_name_ref.current.value = self.row[1]
        self.last_name_ref.current.value = self.row[2]
        self.father_name_ref.current.value = self.row[3]
        self.age_ref.current.value = self.row[4]
        self.cnic_ref.current.value = self.row[5]
        self.father_cnic_ref.current.value = self.row[6]
        self.date_of_birth_ref.current.value = self.row[7]
        self.mobile_ref.current.value = self.row[8]
        self.province_ref.current.value = self.row[9]
        self.postel_addres_ref.current.value = self.row[10]
        self.permanent_addres_ref.current.value = self.row[11]
        self.email_ref.current.value = self.row[12]
        # # self.gender_ref= Ref[RadioGroup]()

        # # metric information ref 
        self.metric_bord_ref.current.value = self.row[14]
        self.school_name_ref.current.value = self.row[15]
        self.metric_total_ref.current.value = self.row[16]
        self.metric_obt_ref.current.value = self.row[17]
        self.metric_percentage_ref.current.value = self.row[18]
        self.metric_grade_ref.current.value = self.row[19]


        # # FSc information_ref
        self.fsc_bord_ref .current.value = self.row[20]
        self.collage_name_ref.current.value = self.row[21]
        self.fsc_total_ref.current.value = self.row[22]
        self.fsc_obt_ref.current.value = self.row[23]
        self.fsc_percentage_ref.current.value = self.row[24]
        self.fsc_grade_ref.current.value = self.row[25]
        
        global image_str
        image_str = self.row[26] # image store from databaae

        # print(f"\n\n\n\n\nits global var: {image_str}")
     
    # when you click on submit btn than call get function get all valus from TextFields of add new student
    def get_values(self,e):

        # *************************************  get values from textfield and store in variable start **********************************************
        rig_no =self.rig_no_ref.current.value
        first_name = self.first_name_ref.current.value
        last_name = self.last_name_ref.current.value
        father_name  = self.father_name_ref.current.value
        age = self.age_ref.current.value
        cnic = self.cnic_ref.current.value
        father_cnic = self.father_cnic_ref.current.value
        date_of_birth = self.date_of_birth_ref.current.value
        mobile = self.mobile_ref.current.value
        province = self.province_ref.current.value
        postel_addres = self.postel_addres_ref.current.value
        permanent_addres = self.permanent_addres_ref.current.value
        email = self.email_ref.current.value
        self.gender_data = self.gender.value

        global gender_var
        if self.gender_data == None or self.gender_data == "":
            gender_var = self.row[13]
        else:
            gender_var = self.gender_data
        
        # print("it is a gender: ", gender_data)

        # print(rig_no)
        # print(first_name)
        # print(last_name)
        # print(father_name)
        # print(age)
        # print(cnic)
        # print(father_cnic)
        # print(date_of_birth)
        # print(mobile)
        # print(province)
        # print(postel_addres)
        # print(permanent_addres)
        # print(email)
        # print(gender_data)


        # store in variables metric data 
        # metric information ref 
        metric_bord = self.metric_bord_ref.current.value
        school_name = self.school_name_ref.current.value 
        metric_total = self.metric_total_ref.current.value 
        metric_obt = self.metric_obt_ref.current.value
        metric_percentage = self.metric_percentage_ref.current.value 
        metric_grade = self.metric_grade_ref.current.value 

        
        # FSc information get in store in variables
        fsc_bord = self.fsc_bord_ref.current.value
        collage_name = self.collage_name_ref.current.value
        fsc_total = self.fsc_total_ref.current.value
        fsc_obt = self.fsc_obt_ref.current.value
        fsc_percentage = self.fsc_percentage_ref.current.value
        fsc_grade =self.fsc_grade_ref.current.value
        # *************************************  get values from textfield and store in variable end **********************************************



        # below a many if logics, related this variables if coditin true i assign there related varialble true else false
        self.is_rig_no_valid = False
        self.is_first_name_valid= False
        self.is_last_name_valid = False
        self.is_father_name_valid = False
        self.is_age_valid = False
        self.is_cnic_valid = False
        self.is_father_cnic_valid = False
        self.is_date_of_birth_ref_valid = False
        self.is_mobile_valid = False
        self.is_privince_valid = False
        self.is_postal_address_valid = False
        self.is_permanent_address_valid = False
        self.is_email_valid = False
        
        # # gender
        self.is_gender_valid = False

        # metric logic
        self.is_metric_bord_valid = False
        self.is_school_name_valid = False
        self.is_metric_total_valid = False
        self.is_metric_obt_valid = False
        self.is_metric_percentage_valid = False
        self.is_metric_grade_valid = False
        # FSc logic
        self.is_fsc_bord_valid = False
        self.is_collage_name_valid = False
        self.is_fsc_total_valid = False
        self.is_fsc_obt_valid = False
        self.is_fsc_percentage_valid = False
        self.is_fsc_grede_valid = False


         
        
        # if type(rig_no) == int and len(rig_no) != 0:
        if rig_no == "":
            self.rig_no_ref.current.error_text= "You need to fill it"
            self.is_rig_no_valid = False
            self.rig_no_ref.current.update()
        else: 
            self.rig_no_ref.current.error_text= None
            self.is_rig_no_valid = True
            self.rig_no_ref.current.update()

        if first_name == "":
            self.first_name_ref.current.error_text= "You need to fill it"
            self.is_first_name_valid = False
            self.first_name_ref.current.update()
        else: 
            self.first_name_ref.current.error_text= None
            self.is_first_name_valid = True
            self.first_name_ref.current.update()

        if last_name == "":
            self.last_name_ref.current.error_text= "You need to fill it"
            self.is_last_name_valid = False
            self.last_name_ref.current.update()
        else: 
            self.last_name_ref.current.error_text= None
            self.is_last_name_valid = True
            self.last_name_ref.current.update()

        if father_name == "":
            self.father_name_ref.current.error_text= "You need to fill it"
            self.is_father_name_valid = False
            self.father_name_ref.current.update()
        else: 
            self.father_name_ref.current.error_text= None
            self.is_father_name_valid = True
            self.father_name_ref.current.update()



        if age == "":
            self.age_ref.current.error_text= "You need to fill it"
            self.is_age_valid = False
            self.age_ref.current.update()
        else: 
            self.age_ref.current.error_text= None
            self.is_age_valid = True
            self.age_ref.current.update()

        if cnic != "" and len(cnic) == 13:
            self.cnic_ref.current.error_text= None
            self.is_cnic_valid = True
            self.cnic_ref.current.update()
        else: 
            self.cnic_ref.current.error_text= "You need to fill it"
            self.is_cnic_valid = False
            self.cnic_ref.current.update()


        if father_cnic != "" and len(father_cnic) == 13:
            self.father_cnic_ref.current.error_text= None
            self.is_father_cnic_valid = True
            self.father_cnic_ref.current.update()
        else: 
            self.father_cnic_ref.current.error_text= "You need to fill it"
            self.is_father_cnic_valid = False
            self.father_cnic_ref.current.update()

        if date_of_birth == "":
            self.date_of_birth_ref.current.error_text= "You need to fill it"
            self.is_date_of_birth_ref_valid = False
            self.date_of_birth_ref.current.update()
        else: 
            self.date_of_birth_ref.current.error_text= None
            self.is_date_of_birth_ref_valid = True
            self.date_of_birth_ref.current.update()

        if mobile != "" and len(mobile) == 11:
            self.mobile_ref.current.error_text= None
            self.is_mobile_valid = True
            self.mobile_ref.current.update()
        else: 
            self.mobile_ref.current.error_text= "You need to fill it"
            self.is_mobile_valid = False
            self.mobile_ref.current.update()

        if province == "":
            self.province_ref.current.error_text= "You need to fill it"
            self.is_privince_valid = False
            self.province_ref.current.update()
        else: 
            self.province_ref.current.error_text= None
            self.is_privince_valid = True
            self.province_ref.current.update()

    

        if postel_addres == "":
            self.postel_addres_ref.current.error_text= "You need to fill it"
            self.is_postal_address_valid = False
            self.postel_addres_ref.current.update()
        else: 
            self.postel_addres_ref.current.error_text= None
            self.is_postal_address_valid = True
            self.postel_addres_ref.current.update()

        if permanent_addres == "":
            self.permanent_addres_ref.current.error_text= "You need to fill it"
            self.is_permanent_address_valid = False
            self.permanent_addres_ref.current.update()
        else: 
            self.permanent_addres_ref.current.error_text= None
            self.is_permanent_address_valid = True
            self.permanent_addres_ref.current.update()


        if email == "":
            self.email_ref.current.error_text= "You need to fill it"
            self.is_email_valid = False
            self.email_ref.current.update()
        else: 
            self.email_ref.current.error_text= None
            self.is_email_valid = True
            self.email_ref.current.update()

        # if gender radio btn not empty than true if empty than false
        # if gender_data == None:
        #     self.error_text_ref.current.value = "Please selecte Gender"
        #     self.is_gender_valid = False    
        #     self.error_text_ref.current.update()
        #     # print("gender True blocl")
            
        # else:
        #     self.error_text_ref.current.value = ""
        #     self.is_gender_valid = True
        #     self.error_text_ref.current.update()
            
        #     print("gender False block")


        # ***************** Metric if logic ************************

        if metric_bord == "":
            self.metric_bord_ref.current.error_text= "You need to fill it"
            self.is_metric_bord_valid = False
            self.metric_bord_ref.current.update()
        else: 
            self.metric_bord_ref.current.error_text= None
            self.is_metric_bord_valid = True
            self.metric_bord_ref.current.update()

        if  school_name == "":
            self.school_name_ref.current.error_text= "You need to fill it"
            self.is_school_name_valid = False
            self.school_name_ref.current.update()
        else: 
            self.school_name_ref.current.error_text= None
            self.is_school_name_valid = True
            self.school_name_ref.current.update()

            

        
        if  metric_total == "":
            self.metric_total_ref.current.error_text= "You need to fill it"
            self.is_metric_total_valid = False
            self.metric_total_ref.current.update()
        else: 
            self.metric_total_ref.current.error_text= None
            self.is_metric_total_valid = True
            self.metric_total_ref.current.update()

        if  metric_obt == "":
            self.metric_obt_ref.current.error_text= "You need to fill it"
            self.is_metric_obt_valid = False
            self.metric_obt_ref.current.update()
        else: 
            self.metric_obt_ref.current.error_text= None
            self.is_metric_obt_valid = True
            self.metric_obt_ref.current.update()      

        if  metric_percentage == "":
            self.metric_percentage_ref.current.error_text= "You need to fill it"
            self.is_metric_percentage_valud = False
            self.metric_percentage_ref.current.update()
        else: 
            self.metric_percentage_ref.current.error_text= None
            self.is_metric_percentage_valid = True
            self.metric_percentage_ref.current.update()      
        
    

        if  metric_grade == "":
            self.metric_grade_ref.current.error_text= "You need to fill it"
            self.is_metric_grade_valid = False
            self.metric_grade_ref.current.update()
        else: 
            self.metric_grade_ref.current.error_text= None
            self.is_metric_grade_valid = True
            self.metric_grade_ref.current.update()      
        # ***************** Metric if logic end ************************



        #  ***************** Fsc if logic start ************************
        
        if  fsc_bord == "":
            self.fsc_bord_ref.current.error_text= "You need to fill it"
            self.is_fsc_bord_valid = False
            self.fsc_bord_ref.current.update()
        else: 
            self.fsc_bord_ref.current.error_text= None
            self.is_fsc_bord_valid = True
            self.fsc_bord_ref.current.update()    
       
        if  collage_name == "":
            self.collage_name_ref.current.error_text= "You need to fill it"
            self.is_collage_name_valid = False
            self.collage_name_ref.current.update()
        else: 
            self.collage_name_ref.current.error_text= None
            self.is_collage_name_valid = True
            self.collage_name_ref.current.update()    

        if fsc_total == "":
            self.fsc_total_ref.current.error_text= "You need to fill it"
            self.is_fsc_total_valid = False
            self.fsc_total_ref.current.update()
        else: 
            self.fsc_total_ref.current.error_text= None
            self.is_fsc_total_valid = True
            self.fsc_total_ref.current.update()

        if  fsc_obt == "":
            self.fsc_obt_ref.current.error_text= "You need to fill it"
            self.is_fsc_obt_valid = False
            self.fsc_obt_ref.current.update()
        else: 
            self.fsc_obt_ref.current.error_text= None
            self.is_fsc_obt_valid = True
            self.fsc_obt_ref.current.update()

        if  fsc_percentage == "":
            self.fsc_percentage_ref.current.error_text= "You need to fill it"
            self.is_fsc_percentage_valud = False
            self.fsc_percentage_ref.current.update()
        else: 
            self.fsc_percentage_ref.current.error_text= None
            self.is_fsc_percentage_valid = True
            self.fsc_percentage_ref.current.update()      

        if  fsc_grade == "":
            self.fsc_grade_ref.current.error_text= "You need to fill it"
            self.is_fsc_grede_valid = False
            self.fsc_grade_ref.current.update()
        else: 
            self.fsc_grade_ref.current.error_text= None
            self.is_fsc_grede_valid = True
            self.fsc_grade_ref.current.update()


        global image_str

        if  self.is_rig_no_valid and self.is_first_name_valid and self.is_last_name_valid and self.is_father_name_valid and self.is_age_valid and self.is_cnic_valid and self.is_father_cnic_valid and self.is_date_of_birth_ref_valid and self.is_mobile_valid and self.is_privince_valid and self.is_postal_address_valid and self.is_permanent_address_valid and self.is_email_valid and self.is_metric_bord_valid and self.is_school_name_valid and self.is_metric_total_valid and self.is_metric_obt_valid and self.is_metric_percentage_valid and self.is_metric_grade_valid and self.is_fsc_bord_valid and self.is_collage_name_valid and self.is_fsc_total_valid and self.is_fsc_obt_valid and self.is_fsc_percentage_valid and self.is_fsc_grede_valid:
            print("condition true")
            try:
                db.update_student_record(
                    self.database_name[7:], # means session name
                    rig_no,
                    first_name,
                    last_name,
                    father_name,
                    age,
                    cnic,
                    father_cnic,
                    date_of_birth,
                    mobile,
                    province,
                    postel_addres,
                    permanent_addres,
                    email,
                    gender_var,

                    metric_bord,
                    school_name,
                    metric_total,
                    metric_obt,
                    metric_percentage,
                    metric_grade,

                    fsc_bord,
                    collage_name,
                    fsc_total,
                    fsc_obt,
                    fsc_percentage,
                    fsc_grade,
                    gambar=image_str,
                    )



                # when data update the textfield need clear 
                # when data sent to database than clear text field
                # when data sent to database than clear text field
                self.rig_no_ref.current.value = ""
                self.first_name_ref.current.value = ""
                self.last_name_ref.current.value = ""
                self.father_name_ref.current.value = ""
                self.age_ref.current.value = ""
                self.cnic_ref.current.value = ""
                self.father_cnic_ref.current.value = ""
                self.date_of_birth_ref.current.value = ""
                self.mobile_ref.current.value = ""
                self.province_ref.current.value = ""
                self.postel_addres_ref.current.value = ""
                self.permanent_addres_ref.current.value = ""
                self.email_ref.current.value = ""
                # gender = self.gender_ref.current.values
                


                # metric data  text fileds clear
                # metric information ref 
                self.metric_bord_ref.current.value = ""
                self.school_name_ref.current.value  = ""
                self.metric_total_ref.current.value  = ""
                self.metric_obt_ref.current.value = ""
                self.metric_percentage_ref.current.value  = ""
                self.metric_grade_ref.current.value = "" 

                
                # FSc information textfields clear
                self.fsc_bord_ref.current.value = ""
                self.collage_name_ref.current.value = ""
                self.fsc_total_ref.current.value = ""
                self.fsc_obt_ref.current.value = ""
                self.fsc_percentage_ref.current.value = ""
                self.fsc_grade_ref.current.value = ""
                

                # update ater clear textfields 
                # update textfields when you assign empty string 
                self.rig_no_ref.current.update()
                self.first_name_ref.current.update()
                self.last_name_ref.current.update()
                self.father_name_ref.current.update()
                self.age_ref.current.update()
                self.cnic_ref.current.update()
                self.father_cnic_ref.current.update()
                self.date_of_birth_ref.current.update()
                self.mobile_ref.current.update()
                self.province_ref.current.update()
                self.postel_addres_ref.current.update()
                self.permanent_addres_ref.current.update()
                self.email_ref.current.update()

                self.metric_bord_ref.current.update()
                self.school_name_ref.current.update()
                self.metric_total_ref.current.update()
                self.metric_obt_ref.current.update()
                self.metric_percentage_ref.current.update()
                self.metric_grade_ref.current.update()

                
                # FSc information updates
                self.fsc_bord_ref.current.update()
                self.collage_name_ref.current.update()
                self.fsc_total_ref.current.update()
                self.fsc_obt_ref.current.update()
                self.fsc_percentage_ref.current.update()
                self.fsc_grade_ref.current.update()

                # when data submited that empty it variable
                # get_session_name = ""
                image_str = ""
                gender_var = ""

                self.page.go("/managment")

            except Exception as e:
                self.error_text_ref.current.value = str(e)
                self.error_text_ref.current.update()
        else:
            pass
    





    # when you click on app bar btn call it than open navigarion drawer 
    def open_drawer(self, e):
        self.page.drawer.open = True  # Open the drawer when button is clicked
        print("open_drawer function callling....")
        self.page.update()


    # fucntion for open file picker 
    def upload_now(self, e: FilePickerResultEvent):
        print("e.files = :", e.files)
        if not e.files == "":
            for x in e.files:
                try:
                    with open(x.path, 'rb') as image_file:
                        self.convertImgToStirng = base64.b64encode(image_file.read()).decode()
                        # cursor.execute("INSERT INTO images(gambar) VALUES (?, ?)",
                                        # (txtname.value, convertImgToStirng))
                        # con.commit()
                        print("your file successfully uploaded")
                        self.page.update()
                except Exception as e:
                    print(e)
                    print("you have a problem here")
                    self.page.update()

        if self.convertImgToStirng:
            global image_str
            image_str = ""
            image_str = self.convertImgToStirng
            print("images here")
        # else: 
        #     print("image not found")



    # it is Managment page
    def edit_student_page(self):
        # here i a data table
        # here make tow radio btns and add where add new students 
            self.gender = RadioGroup(
                content=Row([
                    Radio(value='man',label='man'),
                    Radio(value='female',label='female'),
                    # ref=self.gender_ref
                ])
            )   


            
            # self.student_class =Dropdown(
            #                 options=[
            #                 ],
            #                 border_radius=0,
            #                 width=460,
            #                 on_blur=self.option
            #             )
            # tables = db.get_all_tables() # get all tables name form SqLite3 
            
            # for i in tables: # Loop for isert tables name from datablse in to dowpdown list
            #     i = i[0] #use Index
            #     session= i[0:7] #use slice on table first 7 charecters
            #     if i[0:7] == 'session':
            #         # Add all SqLite tables on dowpdown list
            #         self.student_class.options.append(
            #                 dropdown.Option(i)
            #             )


            # Navigation Drawer
            self.page.drawer = NavigationDrawer(
                    controls=[
                            Container(height=50),  # Space at the top
                            NavigationDrawerDestination(icon=icons.HOME, label="Home"),
                            NavigationDrawerDestination(icon=icons.SETTINGS, label="Settings"),
                            NavigationDrawerDestination(icon=icons.INFO, label="About"),
                        ]
                    )

                # it ia App Bar 
            app_bar = self.page.appbar = AppBar(
                    # title=Text("Student managment system"),
                    leading=IconButton(icon=icons.MENU, on_click=self.open_drawer),
                    bgcolor='green',
                    # height=30,
                )

            # file picker 
            file_picker = FilePicker(
                on_result= self.upload_now
            )
            self.page.overlay.append(file_picker)
        

            return View(
            "add_new_student",
            # padding=0,
            padding=0,
            controls=[
                app_bar,
                Row(
                    spacing=0,
                    controls=[
                        # ****************************** left side btn code start***********************
                        # Container(
                        #     content=Column([
                        #                 Text(
                        #                     "Student mangment",
                        #                     bgcolor="greem",
                        #                     font_family=FontWeight.BOLD,
                        #                     size=20,
                        #                 ),
                        #                 # that is profile icond and neme contaner
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.PERSON),
                        #                         Text('Sabir u din admin')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # that is for dashbord icond and text
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.SHOP),
                        #                         Text("DASHBORD")
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # it is for portal request 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHAT),
                        #                         Text('Portal request')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.PERSON),
                        #                         Text('Profile')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # it is for administrative manager 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'black',
                        #                     content=Row([
                        #                         IconButton(icon=icons.ADD),
                        #                         Text('Add new student',color='white')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # class atendness btn 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.WATCH),
                        #                         Text('Class Atendness')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : e.page.go('/')
                        #                 ),
                        #                 # View attendness record 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('View attendness record')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # Behavviorar analysis 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('Class Atendness')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # class managment btn 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('Class Managment',font_family=FontWeight.BOLD)
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : e.page.go("/managment")
                        #                 ),
                        #                 # subject managment btn
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                                            
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('Subject Managment')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),
                        #                 # subject managment btn 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('Subject Managment')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
                        #                 ),

                        #             ],
                        #     width=200,
                        #     height=self.page.height,
                        #     spacing=0
                            
                        #     ),
                        #     border=border.all(width=3),
                        #     bgcolor='yellow'
                        # ),
                        # ****************************** left side btn code end ***********************
                        Container(
                            content=Column(
                                controls=[
                                    Container(
                                        content=Column([
                                            Row([
                                                Icon(name=icons.LAPTOP_OUTLINED),
                                                Text("Add new student")
                                            ]),
                                            Text("        Save Daily Roll Call",size=10),
                                            
                                        ],
                                        spacing=0
                                        ),
                                        width=1366,
                                        height=42,
                                        bgcolor='white',

                                    ),
                                    
                                    Container(
                                        content=Container(          # nested Container
                                            content=Column([  # main Column
                                                Container(
                                                    content=Column([
                                                            Container(
                                                                Text("EDIT STUDENT RECORD",size=30,color='white',font_family=FontWeight.BOLD),
                                                                bgcolor='green',
                                                                # width=1080,
                                                                alignment=alignment.center,
                                                                
                                                            ),
                                                            Container(
                                                                content=Row([
                                                                    TextField(
                                                                        value='Session',
                                                                        width=130,
                                                                        border_radius=0,
                                                                        bgcolor='grey',
                                                                        disabled=True,
                                                                        color='white'
                                                                    ),
                                                                    # self.student_class, # is is drop down llist define in it function bode
                                                                    TextField(
                                                                        # value='--selecte--',
                                                                        width=460,
                                                                        border_radius=0,
                                                                        disabled = True,
                                                                        ref=self.class_name,
                                                                    ),
                                                                    Container( # it container set for empty space
                                                                        # bgcolor="green",
                                                                        width=70,
                                                                        height=30,
                                                                        alignment=alignment.center
                                                                    ),
                                                                    Container(
                                                                        content=Text("Update page",font_family=FontWeight.BOLD, color='white'),
                                                                        bgcolor="green",
                                                                        width=170,
                                                                        height=40,
                                                                        alignment=alignment.center,
                                                                        ink = True,
                                                                        on_click = lambda _: self.set_values_on_textfileds()
                                                                    )
                                                                ],
                                                                spacing=0
                                                                ),
                                                                padding=10
                                                            )
                                                        ],
                                                        ),
                                                    border=border.all(width=2)
                                                ),
                                                Container(

                                                    content=Column(
                                                                # here get data from studnt (add new student)
                                                                controls=[ 
                                                                    # 1st row to enter new student data 
                                                                    Row([
                                                                        Column([
                                                                            Text(" Rig no"),
                                                                            TextField(hint_text='Rig no',width=100,height=40,border_radius=0,
                                                                            bgcolor='00ff55',autofocus=True,
                                                                            ref=self.rig_no_ref),
                                                                        ]),
                                                                        Text("ADD NEW STUDENT",size=20,font_family=FontWeight.BOLD,bgcolor='green',color='white')
                                                                    ],
                                                                    spacing=440),
                                                                    

                                                                    # 2nd row
                                                                    Row([
                                                                        Column([
                                                                            Text("First Name"),
                                                                            TextField(hint_text='First Name',width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.first_name_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("last Name"),
                                                                            TextField(hint_text='Last Name',width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.last_name_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("F.Name"),
                                                                            TextField(hint_text='F.Name',width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.father_name_ref),
                                                                        ],spacing=5),

                                                                        
                                                                        Column([
                                                                            Text("Age"),
                                                                            TextField(hint_text='Age',width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.age_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("National ID No"),
                                                                            TextField(hint_text="Enter National ID card no",width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.cnic_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("F.National ID No"),
                                                                            TextField(hint_text="Enter father natioanl id no",
                                                                            width=200,height=40,border_radius=0, bgcolor='00ff55',
                                                                            ref=self.father_cnic_ref)
                                                                        ],spacing=5),
                                                                        
                                                                        
                                                                    ]),

                                                                    

                                                                    # 3rd row 
                                                                    Row([


                                                                        Column([
                                                                            Text("Date of birth"),
                                                                            TextField(hint_text="Enter mobile no",width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.date_of_birth_ref),
                                                                        ],spacing=5),

                                                                        
                                                                        Column([
                                                                            Text("Mobile No"),
                                                                            TextField(hint_text="Enter f/mobile no",width=200,height=40,
                                                                            border_radius=0, bgcolor='00ff55',
                                                                            ref=self.mobile_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Province"),
                                                                            TextField(hint_text="Enter provice of scholl",width=200,height=40,
                                                                            border_radius=0, bgcolor='00000000ff55',
                                                                            ref=self.province_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Postal Address"),
                                                                            TextField(hint_text='Enter Postal address',width=200,height=40,
                                                                            border_radius=0, bgcolor='00000000ff55',
                                                                            ref=self.postel_addres_ref)
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Permanent Address"),
                                                                            TextField(hint_text='Enter Permanent address',width=200,height=40,
                                                                            border_radius=0, bgcolor='00000000ff55',
                                                                            ref=self.permanent_addres_ref),
                                                                        ],spacing=5),

                                                                        
                                                                        Column([
                                                                            Text("Email"),
                                                                            TextField(hint_text='Enter Email address',width=200,height=40,
                                                                            border_radius=0, bgcolor='00000000ff55',
                                                                            ref=self.email_ref),
                                                                        ],spacing=5),
                                                                        
                                                                    ]),
                                                                    

                                                                    # self.gender is a tow radio btn  store in self.gender variable and it is declear in it fuction boy 
                                                                    self.gender,

                                                                    # 4th row 
                                                                    Text("    "),
                                                                    Text("Metric Informatin"),
                                                                    # Row([
                                                                        
                                                                        
                                                                    # ]),

                                                                    # 5th row 
                                                                    Row([
                                                                        Column([
                                                                            Text("Bord"),
                                                                            TextField(hint_text='Enter bord name',width=200,height=40,border_radius=0,
                                                                            bgcolor='0000ff55',ref=self.metric_bord_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("School Name"),
                                                                            TextField(hint_text='School Name',width=200,height=40,border_radius=0,
                                                                            bgcolor='0000ff55',ref=self.school_name_ref)
                                                                        ],spacing=5),
                                                                        Column([
                                                                            Text("Total Marks"),
                                                                            TextField(hint_text='Enter Total marks',width=200,height=40,border_radius=0,
                                                                            bgcolor='000000ff55',ref=self.metric_total_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Obt Marks"),
                                                                            TextField(hint_text='Enter obt marks',width=200,height=40,border_radius=0,
                                                                            bgcolor='000000ff55',ref=self.metric_obt_ref)
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Percentage"),
                                                                            TextField(hint_text='Enter percentage',width=200,height=40,border_radius=0,
                                                                            bgcolor='000000ff55',ref=self.metric_percentage_ref),
                                                                        ],spacing=5),

                                                                        
                                                                        Column([
                                                                            Text("Grade"),
                                                                            TextField(hint_text='Enter grade',width=200,height=40,border_radius=0,
                                                                            bgcolor='000000ff55',ref=self.metric_grade_ref),
                                                                        ],spacing=5),
                                                                        
                                                                    ]),

                                                                    # fac information
                                                                    Text("\nFSc Informatin"),
                                                                    Row([
    
                                                                        

                                                                        Column([
                                                                            Text("Bord"),
                                                                            TextField(hint_text='Enter bord name',width=200,height=40,border_radius=0,
                                                                            bgcolor='0000ff55',ref=self.fsc_bord_ref)
                                                                        ],spacing=5),

                                                                        
                                                                        Column([
                                                                            Text("Collage Name"),
                                                                            TextField(hint_text='Enter collage name',width=200,height=40,border_radius=0,
                                                                            bgcolor='0000ff55',ref=self.collage_name_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Total Marks"),
                                                                            TextField(hint_text="Enter Total marks",width=200,height=40,border_radius=0,
                                                                            bgcolor='00ff55', ref=self.fsc_total_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Obt Marks"),
                                                                            TextField(hint_text='Enter obt marks',width=200,height=40,border_radius=0,
                                                                            bgcolor='00ff55',ref=self.fsc_obt_ref)
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Percentage"),
                                                                            TextField(hint_text='Enter percentage',width=200,height=40,border_radius=0,
                                                                            bgcolor='00ff55', ref=self.fsc_percentage_ref),
                                                                        ],spacing=5),

                                                                        Column([
                                                                            Text("Grade"),
                                                                            TextField(hint_text='Enter grade',width=200,height=40,border_radius=0,
                                                                            bgcolor='0000ff55', ref=self.fsc_grade_ref),
                                                                        ],spacing=5),

                                                                        
                                                                    ]),


                                                                    Row([
                                                                        Container(
                                                                            content=TextButton("Upload Image",on_click= lambda e: file_picker.pick_files()),
                                                                            # bgcolor = 'white',
                                                                            # width=140,
                                                                            # height=25,
                                                                            # # border=border.all(width=1)
                                                                        ),
                                                                        Container(
                                                                            content=Text(
                                                                                ref= self.error_text_ref,
                                                                                color= 'red',
                                                                            ),
                                                                            # bgcolor = 'red',
                                                                            width= 700,
                                                                        ),
                                                                        # for empty space to left right align submit btn
                                                                        # Text("                                                                                                                                                                                                                                   "), 
                                                                        ElevatedButton(text="Submit",bgcolor='green',width=150,color="white",
                                                                        on_click=self.get_values,
                                                                        # on_click = lambda _: self.set_values_on_textfileds()
                                                                        ),
                                                                    ],spacing=130),

                                                                ],
                                                                scroll='always',
                                                                expand=True,
                                                                spacing=5,
                                                            ),
                                                    width=1330,
                                                    bgcolor='yellow',
                                                    height=400,
                                                    border_radius=20,
                                                    border=border.all(width=2),
                                                    padding=20,
                                                ),

                                                #  Back btn
                                                TextButton(
                                                    text='Back',
                                                    # on_click= lambda e: e.page.go("/home_page")
                                                    on_click= lambda e: e.page.go("/managment")
                                                    )
                                            ]),
                                            bgcolor='white',
                                            # border=border.all(width=3),
                                            padding=10,
                                            opacity=0.8,
                                            
                    
                                        ),
                                        padding=25,
                                        # bgcolor= 'grey',
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        height= 635,
                                        expand=True,  # Fills the screen
                                        image_fit="cover",  # Covers the entire background
                                        width=1366,

                                    ),

                                    # contaner
                                ],
                                spacing=0,
                                # width=self.page.width,
                                # height=self.page.height    

                            ),
                            # border=border.all(width=3),

                            
                        ),
                    ]
                )
            ]
        )



