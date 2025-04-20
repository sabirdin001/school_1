from flet import *
from database import Database
db = Database()

class LogIn:
    def __init__(self,page:Page):
        self.page = page
        # ********************** data for attendness record start ************************************
       
        self.login_email_ref= Ref[TextField]()
        self.login_password_ref= Ref[TextField]()
        self.error_text_ref = Ref[Text]()

    # when you click edit btn on managment page that call it fuction and recive here single student record on a student 
    
        # get values form login page
    def get_values(self,e):
        email_value = self.login_email_ref.current.value
        password_value = self.login_password_ref.current.value


        # logic when enter text if there condition ture than set from thir True other wise fialse
        self.is_email_valid= False
        self.is_password_valid = False

        self.user = db.get_register_record()
        if self.user != []:
            self.user = self.user[0] # to extract tuples from list
            user_email = self.user[6]
            user_password = self.user[7]
            # logic for email 
            if email_value != user_email:
                # e.page.go("/home_page")
                self.login_email_ref.current.error_text = 'Please check your email'
                self.is_email_valid = False
                self.login_email_ref.current.update()
                
            else:
                self.login_email_ref.current.error_text = None
                self.is_email_valid = True
                self.login_email_ref.current.update()
                
            # Logic for password 
            if password_value != user_password:
                # e.page.go("/home_page")
                self.login_password_ref.current.error_text = 'Please check your password'
                self.is_password_valid = False
                self.login_password_ref.current.update()
                
            else:
                self.login_password_ref.current.error_text = None
                self.is_password_valid = True
                self.login_password_ref.current.update()        
        

            # if all condition true than print
            if self.is_email_valid and self.is_password_valid:

                print(email_value)
                print(password_value)
                print(self.is_email_valid)
                print(self.is_password_valid)
                
                # page routing
                e.page.go("/home_page")
            else:
                print("your got error")
                print(self.is_email_valid)
                print(self.is_password_valid)

        else:
            self.error_text_ref.current.value= "first you need to Register"
            self.error_text_ref.current.update()

    # it is LogIn  Function return UI of login page
    def log_in(self):
        

          

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
                                                    Text("COLLAGE MANAGMENT SYSTEM",size=40,font_family=FontWeight.BOLD,color='blue'),
                                                    alignment=alignment.center
                                                ),
                                              

                                              Row(
                                                controls=[

                                                    Container(
                                                        image_src='images/login.png',
                                                        image_fit= "cover",
                                                     
                                                        width=400,
                                                        height=400,
                                                        # bgcolor='blue'
                                                    ),
                                                    Container(
                                                        content=Column([
                                                            # Hader text
                                                            # Container(
                                                            #     Text("COLLAGE MANAGMENT SYSTEM",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                            #     alignment=alignment.center
                                                            # ),

                                                            
                                                            Container(
                                                                content=Column([

                                                                    Container(
                                                                        Text("LOGIN",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                                        alignment=alignment.center
                                                                    ),

                                                                    # email address text and TextField
                                                                    Column([
                                                                        Column([
                                                                            Text("Email",size=20),
                                                                            TextField(
                                                                                hint_text="Enter email address",
                                                                                prefix_icon=(icons.PERSON),
                                                                                ref=self.login_email_ref,
                                                                            )
                                                                        ])

                                                                    ]),
                                                                    
                                                                    # passwrod text and TextField
                                                                    Column([
                                                                        Column([
                                                                            Text("Password",size=20),
                                                                            TextField(
                                                                                hint_text="Enter strong password",
                                                                                # width=700,
                                                                                prefix_icon=(icons.LOCK),
                                                                                password=True,can_reveal_password=True,
                                                                                ref=self.login_password_ref

                                                                            )
                                                                        ])

                                                                    ]),

                                                                    # Register btn 
                                                                    Container(
                                                                        content=ElevatedButton(
                                                                            text="LOGIN",
                                                                            width=100,
                                                                            bgcolor='blue',
                                                                            color='white',
                                                                            on_click= lambda e: e.page.go('/home_page')
                                                                            # on_click= self.get_values
                                                                            ),
                                                                        # bgcolor='yellow',
                                                                        width=618,
                                                                        alignment=alignment.center
                                                                    ),

                                                                    Row([
                                                                        TextButton(
                                                                            text="Don't have an accout",
                                                                            on_click= lambda e: e.page.go("/signup")
                                                                        ),
                                                                        Container(
                                                                            content=Text(
                                                                                ref=self.error_text_ref,
                                                                                color='red'
                                                                            ),
                                                                            # bgcolor= 'black',
                                                                            width=150,
                                                                        ),
                                                                        TextButton(
                                                                            text="Forget",
                                                                            on_click=lambda e: e.page.go('/forget')
                                                                        ),
                                                                    ],
                                                                    spacing=5,
                                                                    width=400,
                                                                    )

                                                                ],spacing=10),
                                                                border=border.all(width=1),
                                                                border_radius=20,
                                                                padding=padding.only(left=10,right=10,top=10,bottom=10),
                                                                width=400,
                                                                height=350
                                                            )

                                                            
                                                        ],
                                                        spacing=30, # IT is perent Column
                                                        ),
                                                        alignment=alignment.center,
                                                        # border=border.all(width=2),
                                                        
                                                        padding=20
                                                    ),
                                                ]
                                              )
                                            
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8,
                                            border_radius=20,
                                            padding=10
                                        ),
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        
                                        # padding=padding.only(left=350,right=350,top=90,bottom=150),
                                        padding=padding.only(left=250,right=250,top=90,bottom=150),
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





