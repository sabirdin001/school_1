from flet import *
from database import Database

db = Database()

class ResetPassword:
    def __init__(self,page:Page):
        self.page = page
        # ********************** data for attendness record start ************************************
       
        self.old_password_ref = Ref[TextField]()
        self.new_password_ref = Ref[TextField]()
        self.confirm_password_ref = Ref[TextField]()


    def get_values(self, e):
        # signup ppage data 
        row = db.get_register_record()
        row = row[0]
        # print(row)
        old_password = self.old_password_ref.current.value
        new_password = self.new_password_ref.current.value
        confirm_password = self.confirm_password_ref.current.value


        self.is_old_passwrod_valid = False
        self.is_new_passwrod_valid = False
        self.is_confirm_passwrod_valid = False

        # print(old_password)
        # print(new_password)
        # print(confirm_password)
        # print("passeord", row[7])
        
        if old_password ==  row[7]: # use indixing
            self.old_password_ref.current.error_text = None
            self.is_old_passwrod_valid = True
            self.old_password_ref.current.update()

        else:
            self.old_password_ref.current.error_text = "You need to enter exict old password"
            self.is_old_passwrod_valid = False
            self.old_password_ref.current.update()

        if new_password != "": 
            self.new_password_ref.current.error_text = None
            self.is_new_passwrod_valid = True
            self.new_password_ref.current.update()

        else:
            self.new_password_ref.current.error_text = "You need to fill it"
            self.is_new_passwrod_valid = False
            self.new_password_ref.current.update()
           
        if confirm_password == new_password: 
            self.confirm_password_ref.current.error_text = None
            self.is_confirm_passwrod_valid = True
            self.confirm_password_ref.current.update()

        else:
            self.confirm_password_ref.current.error_text = "passward not match"
            self.is_confirm_passwrod_valid = False
            self.confirm_password_ref.current.update()
           

        if   self.is_old_passwrod_valid and self.is_new_passwrod_valid and self.is_confirm_passwrod_valid:
            # print("all True")
            # print(self.is_old_passwrod_valid)
            # print(self.is_new_passwrod_valid)
            # print(self.is_confirm_passwrod_valid)
            try:
                db.forget_password(confirm_password)

                self.old_password_ref.current.value =""
                self.new_password_ref.current.value =""
                self.confirm_password_ref.current.value =""

                self.old_password_ref.current.update()
                self.new_password_ref.current.update()
                self.confirm_password_ref.current.update()

                self.page.snack_bar = SnackBar(
                    content=Text('passeord reset successfully'),
                    bgcolor='green'
                )
                self.page.snack_bar.open = True
                self.page.update()
            except Exception as e:
                print(e)
        else:
            print("some conditon false")
            # print(self.is_old_passwrod_valid)
            # print(self.is_new_passwrod_valid)
            # print(self.is_confirm_passwrod_valid)
           

    # it is Managment page
    def reset_password(self):
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
                                                        Text("RESET YOU PASSWORD",size=40,font_family=FontWeight.BOLD,color='blue'),
                                                        alignment=alignment.center
                                                    ),
                                                    # Container(
                                                    #     Text("Register",size=30,font_family=FontWeight.BOLD,color='blue'),
                                                    #     alignment=alignment.center
                                                    # ),
                                                    
                                                    # Row([
                                                    #     Container(
                                                    #         width=100,
                                                    #         height=100,
                                                    #         bgcolor='blue',
                                                    #     ),
                                                    # ],alignment=alignment.center),

                                                    Container(
                                                        content=Row([
                                                                # set image 
                                                                Container(
                                                                    width=200,
                                                                    height=200,
                                                                    # bgcolor='blue',
                                                                    image_src="images/reset.png",
                                                                ),
                                                                # right side full code without of image container 
                                                                Column([

                                                                # email address text and TextField
                                                                Column([
                                                                    Column([
                                                                        Text("Old password",size=20),
                                                                        TextField(
                                                                            hint_text="Enter Old password",
                                                                            ref= self.old_password_ref,
                                                                            prefix_icon=(icons.PERSON),
                                                                            width=360
                                                                        )
                                                                    ],spacing=3)

                                                                ]),
                                                                
                                                                # passwrod text and TextField
                                                                Column([
                                                                    Column([
                                                                        Text("New Password",size=20),
                                                                        TextField(
                                                                            hint_text="Enter new password",
                                                                            ref= self.new_password_ref,
                                                                            prefix_icon=(icons.LOCK),
                                                                            password=True,can_reveal_password=True,
                                                                            width=360,

                                                                        )
                                                                    ],spacing=3)

                                                                ]),

                                                                Column([
                                                                    Column([
                                                                        Text("Confirm Password",size=20),
                                                                        TextField(
                                                                            hint_text="Enter Confirm password",
                                                                            ref= self.confirm_password_ref,
                                                                            prefix_icon=(icons.LOCK),
                                                                            password=True,can_reveal_password=True,
                                                                            width=360,

                                                                        )
                                                                    ],spacing=3)

                                                                ]),

                                                                # Register btn 
                                                                Container(
                                                                    content=ElevatedButton(
                                                                        text="RESET NOW",
                                                                        width=100,
                                                                        bgcolor='blue',
                                                                        color='white',
                                                                        # on_click= lambda e: e.page.go('/home_page')
                                                                        on_click= self.get_values
                                                                        ),
                                                                    # bgcolor='yellow',
                                                                    width=360,
                                                                    alignment=alignment.center
                                                                ),

                                                                

                                                            ],spacing=10),
                                                        ],spacing=20), #end
                                                        border=border.all(width=1),
                                                        border_radius= 20,
                                                        padding=padding.only(left=20,right=20,top=10,bottom=20)
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
                                                    on_click= lambda e : e.page.go("/home_page")
                                                    )
                                            
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8,
                                            border_radius=20
                                        ),
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        padding=padding.only(left=350,right=350,top=90,bottom=180),
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





