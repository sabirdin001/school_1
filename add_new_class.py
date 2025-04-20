from flet import *
from database import Database
db = Database()

class NewClass:
    def __init__(self,page:Page):
        self.page = page
        self.session_from_ref = Ref[TextField]()
        self.session_to_ref = Ref[TextField]()

    def get_values(self, e):
        session_from = self.session_from_ref.current.value
        session_to = self.session_to_ref.current.value
        
        
        if session_from != "" and  session_to != "":
            session_from = int(session_from)
            session_to = int(session_to)
            
            try:
                if type(session_to) == int and type(session_from) == int:
                    print("Yes is digits")
                    # self.create_student_table("2024_2028")
                    new_session = f"{session_from}_{session_to}"
                    db.create_student_table(new_session)
                else: 
                    print("it is not digits")
           
            except Exception as e: 
                print('error', e)

            finally:
                
                self.page.snack_bar= SnackBar(
                        content=Text("New class create successfully"),
                        bgcolor='green'
                    )
                self.page.snack_bar.open = True 
                self.page.update()
                
                self.page.go("/managment"),
        else:
            print("plear seesion")

        

    def new_class(self):
            self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                leading=IconButton(icon=icons.MENU),  # Call open_drawer on click
                bgcolor="green",
            )
            return View(
            "/new_class",
            # padding=0,
            padding=0,
            controls=[
                # app_bar,
                self.page.appbar,
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
                                                Text("Collage")
                                            ]),
                                            Text("        Govt post greduat collage miran shah ",size=10),
                                            
                                        ],
                                        spacing=0
                                        ),
                                        width=1366,
                                        height=42,
                                        # bgcolor='white',
                                        bgcolor='yellow',

                                    ),
                                    
                                    Container(
                                        content=Container(          # nested Container
                                            content=Column([  # main Column

                                                # close btn container
                                                Container(
                                                    content=IconButton(
                                                            icon=icons.CLOSE_OUTLINED,
                                                            icon_color='red',
                                                            on_click= lambda e: e.page.go("/managment"),
                                                        ),
                                                    # bgcolor='yellow',
                                                    alignment=alignment.center_right
                                                ),
                                                Container(
                                                    content=Column([
                                                            Container(
                                                                Text("Add New Class",size=30,color='white',font_family=FontWeight.BOLD),
                                                                bgcolor='green',
                                                                # width=1080,
                                                                alignment=alignment.center
                                                            ),
                                                            Row([
                                                                Container(
                                                                        content=Row([
                                                                            TextField(
                                                                                value='Session From',
                                                                                width=130,
                                                                                border_radius=0,
                                                                                bgcolor='grey',
                                                                                disabled=True,
                                                                                color='white'
                                                                            ),
                                                                            TextField(
                                                                                ref=self.session_from_ref,
                                                                                value='--selecte--',
                                                                                width=460,
                                                                                border_radius=0
                                                                            ),
                                                                        ],
                                                                        spacing=0
                                                                        ),
                                                                        padding=10
                                                                    ),

                                                                    Container(
                                                                        content=Row([
                                                                            TextField(
                                                                                value='Session to',
                                                                                width=130,
                                                                                border_radius=0,
                                                                                bgcolor='grey',
                                                                                disabled=True,
                                                                                color='white'
                                                                            ),
                                                                            TextField(
                                                                                ref=self.session_to_ref,
                                                                                value='--selecte--',
                                                                                width=460,
                                                                                border_radius=0
                                                                            ),
                                                                        ],
                                                                        spacing=0
                                                                        ),
                                                                        padding=10
                                                                    )
                                                            ],spacing=10),
                                                            Container(
                                                                content=Container(
                                                                    Text("Create now",color='white',size=16),
                                                                    bgcolor='green',
                                                                    width=120,
                                                                    height=30,
                                                                    ink=True,
                                                                    on_click= self.get_values,
                                                                    alignment=alignment.center,
                                                                    border_radius = 6
                                                                    
                                                                    ),

                                                                height=40,
                                                                # bgcolor="blue",
                                                                alignment=alignment.center
                                                            )
                                                            
                                                        ],
                                                        
                                                        ),
                                                    # padding=padding.only(top=0),
                                                    border=border.all(width=2)
                                                ),
           
                                                
                                            ],spacing=0),
                                            bgcolor='white',
                                            
                                            # border=border.all(width=3),
                                            padding=padding.only(top=0, right=10, left=10),

                                            opacity=0.8
                    
                                        ),
                                        padding=padding.only(left=50, right=50, bottom=300, top=100),
                                        bgcolor= 'grey',
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





