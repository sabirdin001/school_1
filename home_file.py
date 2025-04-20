from flet import *


class HomePage:
    def __init__(self,page:Page):
        self.page = page
        # ********************** data for attendness record start ************************************
       
    # when you click on app bar btn call it than open navigarion drawer 

    # when you click edit btn on managment page that call it fuction and recive here single student record on a student 
    
    # it is Managment page
    def home_page(self):
        

            # it ia App Bar 
            app_bar = self.page.appbar = AppBar(
                title=Text("STUDENT MANAGMENT SYSTEM",font_family=FontWeight.BOLD),
                bgcolor='green',
                # height=30,
            )

            return View(
            "/",
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
                                                Row([
                                                    Icon(name=icons.LAPTOP_OUTLINED),
                                                    Text("Government post graduat collage miran shah",font_family=FontWeight.BOLD)
                                                ]),
                                                
                                                IconButton(
                                                    icon=icons.LOGOUT,
                                                    on_click = lambda e : e.page.go("/")
                                                    
                                                    ),
                                            ],alignment="spaceBetween"),
                                            Text("          Bs 4th year program",size=10),

                                            # IconButton(icon=icons.LOGOUT)
                                
                                            
                                        ],
                                        spacing=0
                                        ),
                                        width=1366,
                                        height=42,
                                        bgcolor='white',
                                        # bgcolor='yellow',
                                        padding= padding.only(left=10, right=10)

                                    ),
                                    Container(
                                        content=Text('HOME PAGE',font_family=FontWeight.BOLD,size=20),
                                        bgcolor='green',
                                        height=50,
                                        width=1366,
                                        alignment=alignment.center,
                                        ),
                                    
                                    Container(
                                        content=Container(          # nested Container
                                            content=Column([  # main Column
                                                
                                              

                                              Container(
                                                content=Column([
                                                    
                                                    # 1st row 
                                                    Row([
                                                        Container(
                                                            content=Column([
                                                                Text("ADD New Student"),
                                                                Image(
                                                                    src="images/add.png",  # Online image URL
                                                                    width=130,  # Set width
                                                                    height=130,  # Set height
                                                                    fit="contain",  # Ensure proper scaling
                                                                ),
                                                            ],spacing=20),
                                                            width=200,
                                                            height=200,
                                                            bgcolor='grey',
                                                            border_radius=20,
                                                            alignment=alignment.center,
                                                            ink=True,
                                                            on_click= lambda e: e.page.go("/add_new_student")
                                                        ),

                                                        # Container 2
                                                        Container(
                                                            content=Column([
                                                                Text("Atendness"),
                                                                Image(
                                                                    src="images/attendness.png",  # Online image URL
                                                                    width=130,  # Set width
                                                                    height=130,  # Set height
                                                                    fit="contain",  # Ensure proper scaling
                                                                ),
                                                            ],spacing=20),
                                                            width=200,
                                                            height=200,
                                                            bgcolor='grey',
                                                            border_radius=20,
                                                            alignment=alignment.center,
                                                            ink=True,
                                                            on_click= lambda e: e.page.go("/atendness_page")
                                                        ),
                                                        # Container 3
                                                        Container(
                                                            content=Column([
                                                                Text("Class Managment"),
                                                                Image(
                                                                    src="images/nanagment.png",  # Online image URL
                                                                    width=130,  # Set width
                                                                    height=130,  # Set height
                                                                    fit="contain",  # Ensure proper scaling
                                                                ),
                                                            ],spacing=20),
                                                            width=200,
                                                            height=200,
                                                            bgcolor='grey',
                                                            border_radius=20,
                                                            alignment=alignment.center,
                                                            ink=True,
                                                            on_click= lambda e: e.page.go("/managment"),
                                                        ),
                                                    ],
                                                    spacing=50),

                                                    # 2nd row 
                                                    Row([
                                                        Container(
                                                            content=Column([
                                                                Text("ADD New Staff"),
                                                                Image(
                                                                    src="images/add_staff.png",  # Online image URL
                                                                    width=130,  # Set width
                                                                    height=130,  # Set height
                                                                    fit="contain",  # Ensure proper scaling
                                                                ),
                                                            ],spacing=20),
                                                            width=200,
                                                            height=200,
                                                            bgcolor='grey',
                                                            border_radius=20,
                                                            alignment=alignment.center,
                                                            ink=True,
                                                            on_click= lambda e: e.page.go("/new_staff"),
                                                        ),

                                                        # Container 2
                                                        Container(
                                                            content=Column([
                                                                Text("View Attendness"),
                                                                Image(
                                                                    src="images/view_attendness.png",  # Online image URL
                                                                    width=130,  # Set width
                                                                    height=130,  # Set height
                                                                    fit="contain",  # Ensure proper scaling
                                                                ),
                                                            ],spacing=20),
                                                            width=200,
                                                            height=200,
                                                            bgcolor='grey',
                                                            border_radius=20,
                                                            alignment=alignment.center,
                                                            ink=True,
                                                            on_click= lambda e: e.page.go("/view_attendness")
                                                        ),
                                                        # Container 3
                                                        Container(
                                                            content=Column([
                                                                Text("Reset Password"),
                                                                Image(
                                                                    src="images/reset_lock.png",  # Online image URL
                                                                    width=130,  # Set width
                                                                    height=130,  # Set height
                                                                    fit="contain",  # Ensure proper scaling
                                                                ),
                                                            ],spacing=20),
                                                            width=200,
                                                            height=200,
                                                            bgcolor='grey',
                                                            border_radius=20,
                                                            alignment=alignment.center,
                                                            ink=True,
                                                            on_click= lambda e : e.page.go("/reset_page")
                                                        ),
                                                        
                                                    ],
                                                    spacing=50
                                                    ),
                                                    TextButton("Developer",on_click=  lambda e: e.page.go("/devleoper_page")), # when you click, it show you Developer information page
                                                ],
                                                spacing=20),
                                                # border=border.all(width=2),
                                                
                                                padding=60
                                              )
                                                
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8
                                        ),
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        padding=padding.only(left=270,right=270,top=10,bottom=25),
                                        height= 570,
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





