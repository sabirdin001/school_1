from flet import *
from database import Database
db=Database()

class SignUp:
    def __init__(self,page:Page):
        self.page = page
       
    #    Make ref of a text fields on signup page 
        self.first_name_ref =Ref[TextField]()
        self.last_name_ref =Ref[TextField]()
        self.father_name_ref =Ref[TextField]()
        self.mobile_ref =Ref[TextField]()
        self.cnic_ref =Ref[TextField]()
        self.email_ref =Ref[TextField]()
        self.passwrod_ref =Ref[TextField]()
        self.confirm_password_ref =Ref[TextField]()

    # Get values of signup TextFields values 
    def get_values(self,e):
        first_name = self.first_name_ref.current.value
        last_name = self.last_name_ref.current.value
        father_name = self.father_name_ref.current.value
        mobile = self.mobile_ref.current.value
        cnic= self.cnic_ref.current.value
        email = self.email_ref.current.value
        password = self.passwrod_ref.current.value
        confirm_password = self.confirm_password_ref.current.value


        print("your db record",db.get_register_record())

        # in if codition match than we will assign it Ture 
        self.is_first_name_valid = False
        self.is_last_name_valid = False
        self.is_father_name_valid = False
        self.is_mobile_valid = False
        self.is_cnic_valid= False
        self.is_email_valid = False
        self.is_password_valid= False
        self.is_confirm_password_valid = False



        if first_name == "":
            self.first_name_ref.current.error_text = " "
            self.is_first_name_valid = False
            self.first_name_ref.current.update()
        else:
            self.first_name_ref.current.error_text = None
            self.is_first_name_valid = True
            self.first_name_ref.current.update()

        # last naem logic
        if last_name == "":
            self.last_name_ref.current.error_text = " "
            self.is_last_name_valid = False
            self.last_name_ref.current.update()

        else:
            self.last_name_ref.current.error_text = None
            self.is_last_name_valid=True
            self.last_name_ref.current.update()

        # codition for father name 
        if father_name == "":
            self.father_name_ref.current.error_text = " "
            self.is_father_name_valid = False
            self.father_name_ref.current.update()

        else:
            self.father_name_ref.current.error_text = None
            self.is_father_name_valid=True
            self.father_name_ref.current.update()

         # codition for mobile
        if mobile == "":
            self.mobile_ref.current.error_text = " "
            self.is_mobile_valid = False
            self.mobile_ref.current.update()
        else:
            self.mobile_ref.current.error_text = None
            self.is_mobile_valid=True
            self.mobile_ref.current.update()

        # codition for cnic
        # if len(cnic) != 14:
        if cnic == "":
            self.cnic_ref.current.error_text = " "
            self.is_cnic_valid = False
            self.cnic_ref.current.update()
        else:
            self.cnic_ref.current.error_text = None
            self.is_cnic_valid=True
            self.cnic_ref.current.update()
        
        # codition for email
        if email == "":
            self.email_ref.current.error_text = " "
            self.is_email_valid = False
            self.email_ref.current.update()
        else:
            self.email_ref.current.error_text = None
            self.is_email_valid=True
            self.email_ref.current.update()


        # codition for password
        if password == "" :
            self.passwrod_ref.current.error_text = " "
            self.is_password_valid = False
            self.passwrod_ref.current.update()
        else:
            self.passwrod_ref.current.error_text = None
            self.is_password_valid=True
            self.passwrod_ref.current.update()

        if confirm_password == "" or password != confirm_password:
            self.confirm_password_ref.current.error_text = " "
            self.is_confirm_password_valid = False
            print("error")
            self.confirm_password_ref.current.update()
        else:
            self.confirm_password_ref.current.error_text = None
            self.is_confirm_password_valid=True
            self.confirm_password_ref.current.update()

        # if all condition True:
        if self.is_first_name_valid and self.is_last_name_valid and self.is_father_name_valid and self.is_mobile_valid and self.is_cnic_valid and self.is_email_valid and self.is_password_valid and self.is_confirm_password_valid:
            # print(f"first_name: {first_name}   last_name: {last_name}    father_name: {father_name} mobile: {mobile} cnic: {cnic} email: {email}  passwor:{password} confirm {confirm_password}")
            # send data to database
            db.create_signup_record(first_name, last_name, father_name, mobile, cnic,email,  password,)
            # SnackBar open 
            self.page.snack_bar=SnackBar(
                content=Text(
                    "Passwrof forget successfuly",
                    ),
                bgcolor='green'
            )
            self.page.snack_bar.open = True
            self.page.update()
        
            self.first_name_ref.current.value =""
            self.last_name_ref.current.value =""
            self.father_name_ref.current.value =""
            self.mobile_ref.current.value =""
            self.cnic_ref.current.value =""
            self.email_ref.current.value =""
            self.passwrod_ref.current.value =""
            self.confirm_password_ref.current.value =""
            
        else:
            print("some conditon false")

            print(self.is_first_name_valid)
            print(self.is_last_name_valid)
            print(self.is_father_name_valid)
            print(self.is_mobile_valid)
            print(self.is_cnic_valid)
            print(self.is_email_valid)
            print(self.is_password_valid)
            print(self.is_confirm_password_valid)

    # it is Managment page
    def Sign_up(self):
        

          

            return View(
            "/",
            # padding=0,
            padding=0,
            controls=[
                Row(
                    spacing=0,
                    controls=[

                       
                        Container(
                            content=Column(
                                controls=[

                                  
                                    
                                    Container(
                                        content=Container(          # nested Container
                                            content=Column([  # main Column
                                                
                                              

                                              Container(
                                                content=Column([
                                                    # Hader text
                                                    # Container(
                                                    #     Text("COLLAGE MANAGMENT SYSTEM",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                    #     alignment=alignment.center
                                                    # ),
                                                    # Container(
                                                    #     Text("Register",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                    #     alignment=alignment.center
                                                    # ),
                                                    
                                                    Container(
                                                        content=Column([

                                                            Container(
                                                                Text("Register",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                                alignment=alignment.center
                                                            ),

                                                            # 1st row  first name last name
                                                            Row([
                                                                # First name 
                                                                Column([
                                                                    Text('First Name'),
                                                                    TextField(hint_text='First Name',width=290,border_radius=0, bgcolor='00ff55',ref=self.first_name_ref)
                                                                ]),

                                                                # last name 
                                                                Column([
                                                                    Text('Last Name'),
                                                                    TextField(hint_text='Last Name',width=290,border_radius=0, bgcolor='00ff55',ref=self.last_name_ref)
                                                                ])
                                                            ],spacing=30),

                                                            # 2nd row father name mobile no 
                                                            Row([
                                                                #Father name 
                                                                Column([
                                                                    Text('F.Name'),
                                                                    TextField(hint_text='Father Name',width=290,border_radius=0, bgcolor='00ff55',ref=self.father_name_ref)
                                                                ]),
                                                                # Mobile no 
                                                                Column([
                                                                    Text('Mobile No'),
                                                                    TextField(hint_text='Mobile',width=290,border_radius=0, bgcolor='00ff55',ref=self.mobile_ref)
                                                                ]),
                                                            ],spacing=30),

                                                            # 3rd row cnic and email 
                                                            Row([
                                                                # CNIC 
                                                                Column([
                                                                    Text('National ID Card No'),
                                                                    TextField(hint_text='National ID Card No',width=290,border_radius=0, bgcolor='00ff55',ref=self.cnic_ref),
                                                                ]),

                                                                # Email 
                                                                Column([
                                                                    Text('Email'),
                                                                    TextField(hint_text='Email Address',width=290,border_radius=0, bgcolor='00ff55',ref=self.email_ref)
                                                                ]),
                                                                
                                                            ],spacing=30),

                                                            # password and confirm password 
                                                            Row([
                                                                # CNIC 
                                                                Column([
                                                                    Text('Password'),
                                                                    TextField(hint_text='password',width=290,border_radius=0, bgcolor='00ff55',password=True,can_reveal_password=True,ref=self.passwrod_ref)
                                                                ]),

                                                                # Email 
                                                                Column([
                                                                    Text('Confirm Password'),
                                                                    TextField(hint_text='Confirm password',width=290,border_radius=0, bgcolor='00ff55',password=True,can_reveal_password=True,ref=self.confirm_password_ref)
                                                                ]),
                                                                
                                                            ],spacing=30),


                                                            # Register btn 
                                                            Container(
                                                                content=ElevatedButton(
                                                                    text="Register",
                                                                    width=100,
                                                                    bgcolor='blue',
                                                                    color='white',
                                                                    # on_click= lambda e:e.page.go("/")
                                                                    on_click=self.get_values
                                                                    ),
                                                                # bgcolor='yellow',
                                                                # width=618,
                                                                alignment=alignment.center
                                                            ),

                                                            Row([
                                                                TextButton(
                                                                    text="Already have an account",
                                                                    on_click= lambda e: e.page.go("/")
                                                                ),
                                                            ])

                                                        ],spacing=10),
                                                        border=border.all(width=1),
                                                        border_radius=10,
                                                        padding=5
                                                    )

                                                    
                                                ],
                                                spacing=30, # IT is perent Column
                                                ),
                                                alignment=alignment.center,
                                                # border=border.all(width=2),
                                                
                                                padding=20
                                              ),

                                            # back btn 
                                            TextButton(
                                                text='  Back',
                                                on_click= lambda e:e.page.go("/")
                                                )
                                                
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8,
                                            border_radius=20
                                        ),
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        padding=padding.only(left=350,right=350,top=50,bottom=100),
                                        height= 768,
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





