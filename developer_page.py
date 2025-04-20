from flet import *


class DeveloperPage:
    def __init__(self,page:Page):
        self.page = page
    
    # it is Managment page
    def devleoper_page(self):
        


            # it ia App Bar 
            app_bar = self.page.appbar = AppBar(
                title=Text("STUDENT MANAGMENT SYSTEM",font_family=FontWeight.BOLD),
                leading=IconButton(icon=icons.MENU,),
                bgcolor='green',
                # height=30,
            )

            return View(
            "/devleoper_page",
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
                                                
                                            ],spacing=950),
                                            Text("          Bs 4th year program",size=10),

                                            # IconButton(icon=icons.LOGOUT)
                                
                                            
                                        ],
                                        spacing=0
                                        ),
                                        width=1366,
                                        height=42,
                                        bgcolor='white',
                                        # bgcolor='yellow',

                                    ),
                                    Container(
                                        content=Text('ABOUT DEVELOPER',font_family=FontWeight.BOLD,size=20),
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

                                                    Container(
                                                        IconButton(
                                                            icon="close",
                                                            on_click = lambda e: e.page.go("/home_page"),
                                                            icon_color = "red"
                                                        ),
                                                        alignment=alignment.top_right,
                                                        # bgcolor="grey",
                                                        height=25,
                                                    ),
                                                    Row([
                                                        # progile image 
                                                        Container(
                                                            image_src="images/sabir.png",
                                                            bgcolor= "blue",
                                                            width = 200,
                                                            height = 250,
                                                            image_fit = "cover",
                                                            border=border.all(width=3)
                                                        ),
                                                        Container(
                                                            Column([
                                                                Text("Name: Sabir u din Dawar",font_family="Arial",size=40,color="black",weight=FontWeight.BOLD),
                                                                Text("Student of Govt Post Graduad Collage Miran shah",font_family="Arial",size=22,color="black",weight=FontWeight.BOLD),
                                                                Text("Studing in BS Computer Science",font_family="Arial",size=18,color="black"),
                                                                Text("Email: fullbakwas08@gmail.com",font_family="Arial",size=18,color="black"),
                                                                Text("Facebook: Sabir u din dawar ",font_family="Arial",size=18,color="black"),
                                                         
                                                                
                                                            ]),
                                                            # bgcolor= 'green',
                                                            # width = 200,
                                                            expand = True,
                                                            height = 250,
                                                            # border=border.all(width=2)
                                                        ),
                                                        

                                                    ],spacing=25)
                                                ],
                                                spacing=0),
                                                # border=border.all(width=2),
                                                
                                                padding=padding.only(left=20,right=20,top=0,bottom=20)
                                              )
                                                
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8,
                                            alignment=alignment.center,
                                            border=border.all(width=4,color='yellow')
                                        ),
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        padding=padding.only(left=270,right=270,top=30,bottom=235),
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





