from flet import *
from database import Database
db = Database()
import base64


image_str = "" # it is a global variable to store image from datebase
class ViewStudent:
    def __init__(self,page:Page):
        self.page = page
        self.rig_ref= Ref[Text]()
        self.full_name_ref= Ref[Text]()
        self.f_name_ref = Ref[Text]()
        self.cnic_ref= Ref[Text]()
        self.f_cnic_ref= Ref[Text]()
        self.mobile_ref= Ref[Text]()
        self.province_ref= Ref[Text]()
        self.date_of_birth_ref= Ref[Text]()
        self.email_ref= Ref[Text]()
        self.gender_ref= Ref[Text]()
        self.age_ref= Ref[Text]()
        self.postel_address_ref= Ref[Text]()
        self.permanent_address_ref= Ref[Text]()


        self.m_bord_ref= Ref[Text]()
        self.m_school_ref= Ref[Text]()
        self.m_total_ref= Ref[Text]()
        self.m_obt_ref= Ref[Text]()
        self.m_percentage_ref= Ref[Text]()
        self.m_grade_ref= Ref[Text]()


        self.f_bord_ref= Ref[Text]()
        self.f_collage_ref= Ref[Text]()
        self.f_total_ref= Ref[Text]()
        self.f_obt_ref= Ref[Text]()
        self.f_percentage_ref= Ref[Text]()
        self.f_grade_ref= Ref[Text]()
        self.image_ref = Ref[Image]()
        
        



    def ui_ready(self, row):
        global image_str  #it is a global variable to store image from datebase
        image_str = row[-1]   # here is assigning image from database in str format
        self.page.views.clear()
        self.page.views.append(self.view_student())
        self.page.update()
        self.row =  row
        self.set_values_text()
        
        print("\n\n\n\n\n\nui ready funcion")
        

        # read image form database and decode in image 
        # self.image = Image(
        #                     src_base64=self.row[-1],
        #                     # width=300,
        #                     # height=200,
        #                     # fit='cover'
        #                     # src_base64=,
        #                     width=300,  # Set width
        #                     height=200  # Set height
        #                 )


    def set_values_text(self):
    # Ensure the reference exists before assigning values
        if self.rig_ref.current:

            self.rig_ref.current.value = self.row[0]
            self.full_name_ref.current.value = f"{self.row[1] + self.row[2]}"
            self.f_name_ref.current.value = self.row[3]
            self.cnic_ref.current.value = self.row[5]
            self.f_cnic_ref.current.value = self.row[6]
            self.mobile_ref.current.value = self.row[8]
            self.province_ref.current.value = self.row[9]
            self.date_of_birth_ref.current.value = self.row[7]
            self.email_ref.current.value = self.row[12]
            self.gender_ref.current.value =self.row[13] 
            self.age_ref.current.value = self.row[4]
            self.postel_address_ref.current.value = self.row[10]
            self.permanent_address_ref.current.value = self.row[11]

            

            self.m_bord_ref.current.value = self.row[14]
            self.m_school_ref.current.value = self.row[15]
            self.m_total_ref.current.value = self.row[16]
            self.m_obt_ref.current.value = self.row[17]
            self.m_percentage_ref.current.value = self.row[18]
            self.m_grade_ref.current.value = self.row[19]


            self.f_bord_ref.current.value = self.row[20]
            self.f_collage_ref.current.value = self.row[21]
            self.f_total_ref.current.value = self.row[22]
            self.f_obt_ref.current.value = self.row[23]
            self.f_percentage_ref.current.value = self.row[24]
            self.f_grade_ref.current.value = self.row[25]
            
            # self.image_ref.current.value = self.image
        else:
            print("Error: self.rig_ref_text is None")

        


    # it is View page
    def view_student(self):
        # print("\n\n\n\n\n\view_student() function is being called! befofe")
        # rig = self.rig_ref_text.current.value  # Get updated value
        # print(rig)  # make error
        global image_str # it is a global variable to store image from datebase

        print("\n\n\n\n\n\nview_student caling.....")
        print("\n\n\n\n\n\nview_ it is a global val.....",image_str)

        app_bar = self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                # leading=IconButton(icon=icons.MENU, on_click=self.open_drawer),
                bgcolor='green',
                # height=30,
            )
        
        def close_page():
            self.page.go("/managment")
            print("are calling...........")


        return View(
            "add_new_student",
            # padding=0,
            padding=0,
            controls=[
                app_bar,
                Row(
                    spacing=0,
                    controls=[
                       
                        Container(
                            content=Column(
                                controls=[
                                    Container(
                                        content=Column([
                                            Row([
                                                Icon(name=icons.LAPTOP_OUTLINED),
                                                Text("staff payroll")
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
                                                        content=IconButton(
                                                            icon='close',
                                                            icon_color = 'red',
                                                            on_click= lambda e: close_page(),
                                                            
                                                        ), 
                                                       alignment=alignment.center_right
                                                    ),    

                                                    Row(
                                                        controls=[
                                                            Container(
                                                                content=Column([

                                                                            # 1st row
                                                                            Container(

                                                                                
                                                                                content=Row(
                                                                                    controls=[
                                            

                                                                                                Column([
                                                                                                    Text("Rig no"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.rig_ref),
                                                                                                        width=90,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("full name name"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.full_name_ref),
                                                                                                        width=210,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("Father name"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.f_name_ref),
                                                                                                        width=210,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                

                                                                                                Column([
                                                                                                    Text("National id no"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref= self.cnic_ref),
                                                                                                        width=220,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("F/National id no"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.f_cnic_ref),
                                                                                                        width=220,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),



                                                                                                

                                                                                    ],
                                                                                ),
                                                                                # width=270,
                                                                                # height=140,
                                                                                # bgcolor='red'
                                                                            ),

                                                                    
                                                                            # 2nd row on text files
                                                                            Container(
                                                                                content=Row(
                                                                                    controls=[
                                                                                                

                                                                                                Column([
                                                                                                    Text("Mobile No"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.mobile_ref),
                                                                                                        width=150,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Province"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.province_ref),
                                                                                                        width=200,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("D.O.B"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.date_of_birth_ref),
                                                                                                        width=130,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("Email"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.email_ref),
                                                                                                        width=300,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Gender"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.gender_ref),
                                                                                                        width=80,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Age"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.age_ref),
                                                                                                        width=80,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                

                                                                                            

                                                                                    ],
                                                                                ),
                                                                                # width=270,
                                                                                # height=140,
                                                                                # bgcolor='red'
                                                                            ),



                                                                            # 3rd row 
                                                                             Container(

                                                                                # 1st row on text files
                                                                                content=Row(
                                                                                    controls=[
                                                                                                
                                                                                            Column([
                                                                                                    Text("Postel address"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.postel_address_ref),
                                                                                                        width=490,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Permanent address"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.permanent_address_ref),
                                                                                                        width=490,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                    ],
                                                                                ),
                                                                                # width=270,
                                                                                # height=140,
                                                                                # bgcolor='red'
                                                                            ),

                                                                            # it is text of Metriculation
                                                                            Text("Metriculation", size=20),


                                                                            # 4th row 
                                                                            Container(           
                                                                                content=Row(
                                                                                    controls=[
                                                                                                Column([
                                                                                                    Text("Bord"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.m_bord_ref),
                                                                                                        width=150,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("School name"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.m_school_ref),
                                                                                                        width=360,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Total Marks"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref=self.m_total_ref),
                                                                                                        width=110,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("Obt Marks"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.m_obt_ref),
                                                                                                        width=110,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                

                                                                                                Column([
                                                                                                    Text("Percentage"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref= self.m_percentage_ref),
                                                                                                        width=110,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("Grade"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref= self.m_grade_ref),
                                                                                                        width=100,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),



                                                                                                

                                                                                    ],
                                                                                ),
                                                                                # width=270,
                                                                                # height=140,
                                                                                # bgcolor='red'
                                                                            ),

                                                                            

                                                                            # it is text of FSc
                                                                            Text("Intermediate", size=20),


                                                                            # 5th row 
                                                                            Container(           
                                                                                content=Row(
                                                                                    controls=[
                                                                                                Column([
                                                                                                    Text("Bord"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref= self.f_bord_ref),
                                                                                                        width=150,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Collage name"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.f_collage_ref),
                                                                                                        width=360,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                Column([
                                                                                                    Text("Total Marks"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20,ref=self.f_total_ref),
                                                                                                        width=110,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("Obt Marks"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref= self.f_obt_ref),
                                                                                                        width=110,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),

                                                                                                

                                                                                                Column([
                                                                                                    Text("Percentage"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref= self.f_percentage_ref),
                                                                                                        width=110,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),


                                                                                                Column([
                                                                                                    Text("Grade"),
                                                                                                    Container(
                                                                                                        content=Text("",size=20, ref=self.f_grade_ref),
                                                                                                        width=100,
                                                                                                        height=46,
                                                                                                        # bgcolor='grey',
                                                                                                        border=border.all(width=1),
                                                                                                        alignment=alignment.center,
                                                                            
                                                                                                        
                                                                                                    ),
                                                                                                ],spacing=0),



                                                                                                

                                                                                    ],
                                                                                ),
                                                                                # width=270,
                                                                                # height=140,
                                                                                # bgcolor='red'
                                                                            ),

                                                                    ],
                                                                    spacing=0
                                                                    ),
                                                    border=border.all(width=2),
                                                    height=420,
                                                    width=1010,
                                                    # bgcolor='green',
                                                    padding=10
                                                ),

                                                Column(
                                                    controls=[
                                                        Container(
                                                            Image(
                                                                    src_base64 = image_str, # it is a global variable, store image in str format
                                                                    fit='cover',
                                                                    width=300,  # Set width
                                                                    height=200  # Set height
                                                                ),
                        
                                                            bgcolor="blue",
                                                            width=230,
                                                            height=210,
                                                            image_fit = "cover",
                                                            border=border.all(width=1,color='black'),
                                                        ),

                                                    Container(
                                                            image_src = "images/cap.png",
                                                            bgcolor="",
                                                            width=230,
                                                            height=200
                                                        )
                                                    ],
                                                    # spacing=0
                                                )
                                                
                                                ]
                                            ),

                                                
                                                
                        
                                        
                                    ]),
                                    bgcolor='white',
                                    # border=border.all(width=3),
                                    padding=10,
                                    opacity=0.8,
                                    border=border.all(width=1)
            
                                ),
                                padding=padding.only(left=45, right=45,top=20,bottom=120),
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



