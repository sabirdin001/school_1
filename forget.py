from flet import *
from database import Database
db = Database()


class Forget:
    def __init__(self,page:Page):
        self.page = page
        # ********************** data for attendness record start ************************************
       
        self.first_name_ref = Ref[TextField]()
        self.last_name_ref  = Ref[TextField]()
        self.cnic_ref = Ref[TextField]()
        self.email_ref  = Ref[TextField]()
        self.password_ref =  Ref[TextField]()
        self.confirm_password_ref  = Ref[TextField]()

    def get_values(self,e):
        row = db.get_register_record()
        row = row[0]
        print(row)
        first_name= self.first_name_ref.current.value
        last_name = self.last_name_ref.current.value
        mobile=self.last_name_ref.current.value
        cnic = self.cnic_ref.current.value
        email = self.email_ref.current.value 
        password = self.password_ref.current.value 
        confirm_password = self.confirm_password_ref.current.value 

        # print(full_name)
        # print(mobile)
        # print(cnic)
        # print(email)
        # print(password)
        # print(confirm_password)
        # print(row[1]+" "+row[2])

        # logic if all condition true in if blocks
        self.is_first_name_valid= False
        self.is_last_name_valid = False
        self.is_mobile_valid= False
        self.is_cnic_valid= False
        self.is_email_valid= False
        self.is_password_valid= False
        self.is_confirm_password_valid= False

        # row[1]  # make index and concatenet 1st
        if row[1] == first_name:
            print('condition Ture')
            self.first_name_ref.current.error_text = None
            self.is_first_name_valid = True
            self.first_name_ref.current.update()
        else:
            print('condition fase')
            self.first_name_ref.current.error_text = "Full name not matched"
            self.is_first_name_valid = False
            self.first_name_ref.current.update()

        if row[2] == last_name:
            print('condition Ture')
            self.first_name_ref.current.error_text = None
            self.is_last_name_valid = True
            self.last_name_ref.current.update()
        else:
            print('condition fase')
            self.first_name_ref.current.error_text = "Full name not matched"
            self.is_first_name_valid = False
            self.first_name_ref.current.update()
        
        # if row[4] == mobile:
        #     print('condition Ture')
        #     self.last_name_ref.current.error_text = None
        #     self.is_mobile_valid = True
        #     self.last_name_ref.current.update()
        # else:
        #     print('condition fase')
        #     self.last_name_ref.current.error_text = "Mobile not matched"
        #     self.is_mobile_valid = False
        #     self.last_name_ref.current.update()

        if row[5] == cnic:
            print('condition Ture')
            self.cnic_ref.current.error_text = None
            self.is_cnic_valid = True
            self.cnic_ref.current.update()
        else:
            print('condition fase')
            self.cnic_ref.current.error_text = "Nic not matched"
            self.is_cnic_valid = False
            self.cnic_ref.current.update()

        if row[6] == email:
            print('condition Ture')
            self.email_ref.current.error_text = None
            self.is_email_valid = True
            self.email_ref.current.update()
        else:
            print('condition fase')
            self.email_ref.current.error_text = "email not matched"
            self.is_email_valid = False
            self.email_ref.current.update()

        # print(self.is_first_name_valid)
        # print(self.is_last_name_valid)
        # print(self.is_cnic_valid)
        # print(self.is_email_valid)
        # print(e)
        # if all above condition if all Ture than excure if or if all False than excute else 
        if self.is_first_name_valid and self.is_last_name_valid and self.is_cnic_valid and self.is_email_valid:
            print('you can able to chabe your password'),
            db.forget_password(password)
            e.page.go('/')
            
        else:
            print("you can not able to change your password")





    # it is Managment page
    def forget_password(self):
        

          

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
                                                    Container(
                                                        Text("COLLAGE MANAGMENT SYSTEM",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                        alignment=alignment.center
                                                    ),
                                                    # Container(
                                                    #     Text("Register",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                    #     alignment=alignment.center
                                                    # ),
                                                    
                                                    Container(
                                                        content=Column([

                                                            Container(
                                                                Text("Forget password",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                                alignment=alignment.center
                                                            ),

                                                            # 1st row  first name last name
                                                            Row([
                                                                # First name 
                                                                Column([
                                                                    Text('Firt Name'),
                                                                    TextField(hint_text='Full Name',width=290,height=40,border_radius=0, bgcolor='00ff55',
                                                                    ref=self.first_name_ref)
                                                                ]),

                                                                # last name 
                                                                Column([
                                                                    Text('Last name'),
                                                                    TextField(hint_text='Mobile no',width=290,height=40,border_radius=0, bgcolor='00ff55',
                                                                    ref=self.last_name_ref)
                                                                ])
                                                            ],spacing=30),

                                                            # 2nd row cnic name mobile no 
                                                            Row([
                                                                #Cnic 
                                                                Column([
                                                                    Text('National ID Card No'),
                                                                    TextField(hint_text='National ID Card No',width=290,height=40,border_radius=0, bgcolor='00ff55',
                                                                    ref=self.cnic_ref)
                                                                ]),
                                                                # Mobile no 
                                                                Column([
                                                                    Text('Email'),
                                                                    TextField(hint_text='Email address',width=290,height=40,border_radius=0, bgcolor='00ff55',
                                                                    ref=self.email_ref)
                                                                ]),
                                                            ],spacing=30),

                                                            # 3rd row cnic and email 

                                                            # password and confirm password 
                                                            Row([
                                                                # CNIC 
                                                                Column([
                                                                    Text('New Password'),
                                                                    TextField(hint_text='password',width=290,height=40,border_radius=0, bgcolor='00ff55',
                                                                    password=True,can_reveal_password=True,
                                                                    ref=self.password_ref)
                                                                ]),

                                                                # Email 
                                                                Column([
                                                                    Text('Confirm Password'),
                                                                    TextField(hint_text='Confirm password',width=290,height=40,border_radius=0, 
                                                                    bgcolor='00ff55',password=True,can_reveal_password=True,
                                                                    ref=self.confirm_password_ref)
                                                                ]),
                                                                
                                                            ],spacing=30),


                                                            # Register btn 
                                                            Container(
                                                                content=ElevatedButton(
                                                                    text="Forget",
                                                                    width=100,
                                                                    bgcolor='blue',
                                                                    color='white',
                                                                    # on_click= lambda e: e.page.go('/') # Go to login page
                                                                    on_click= self.get_values
                                                                    ),
                                                                # bgcolor='yellow',
                                                                width=618,
                                                                alignment=alignment.center
                                                            ),

                                                        
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

                                              TextButton(
                                                text='  Back',
                                                on_click= lambda e : e.page.go("/")
                                                )
                                                
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8,
                                            border_radius=20
                                        ),
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        padding=padding.only(left=350,right=350,top=100,bottom=150),
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





