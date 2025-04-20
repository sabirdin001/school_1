from flet import *
from database import Database
from datetime import datetime
db = Database()


class NewMonth:
    def __init__(self,page:Page):
        self.page = page
        self.session_from_ref = Ref[TextField]()
        self.session_to_ref = Ref[TextField]()

    def get_values(self, e):
        # session_from = self.session_from_ref.current.value
        # session_to = self.session_to_ref.current.value
        # print(self.session)
        # print(self.month)
        self.year = datetime.now().strftime("%Y") # that statment take from System date only year
        if self.session != "" and  self.month != "":

            try:
                    # self.create_student_table("2024_2028")
                    # new_session = f"{session_to}_{session_from}"
                    db.create_table_attendness(self.month, self.session, self.year)
           
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
            print("please selecte seesion or month")

    def seassion_option(self, e):
        self.session =self.student_class.value
        # self.update_data_table(self.table_name)
        # print("clss ", self.session)

    def month_option(self, e):
        self.month =self.month_droopdown.value
        # self.update_data_table(self.table_name)
        # print("Month ", self.month)
   
    def new_month(self):
            self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                leading=IconButton(icon=icons.MENU),  # Call open_drawer on click
                bgcolor="green",
            )

            # list all seassion tables on dowpdown
            self.student_class =Dropdown(
                            options=[
                                # dropdown.Option('1st Semester'),
                                # dropdown.Option("2nd Semester"),

                            ],
                            border_radius=0,
                            width=460,
                            on_change=self.seassion_option
                        )
            tables = db.get_all_tables()
            for i in tables:

                i = i[0] #use Index
                session= i[0:7] #use slice on table first 7 charecters
                if i[0:7] == 'session':
                    # Add all SqLite tables on dowpdown list
                    self.student_class.options.append(
                            dropdown.Option(i)
                        )

            # dropdown for months 
            self.month_droopdown =Dropdown(
                            options=[
                                dropdown.Option('January'),
                                dropdown.Option("Feberuary"),
                                dropdown.Option("March"),
                                dropdown.Option("April"),
                                dropdown.Option("May"),
                                dropdown.Option("Jun"),
                                dropdown.Option("July"),
                                dropdown.Option("Augst"),
                                dropdown.Option("Setember"),
                                dropdown.Option("Actober"),
                                dropdown.Option("Noumber"),
                                dropdown.Option("December"),

                            ],
                            border_radius=0,
                            width=460,
                            on_change=self.month_option
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
                                                                                value='Sessions',
                                                                                width=130,
                                                                                border_radius=0,
                                                                                bgcolor='grey',
                                                                                disabled=True,
                                                                                color='white'
                                                                            ),
                                                                            self.student_class
                                                                            # TextField(
                                                                            #     ref=self.session_from_ref,
                                                                            #     value='--selecte--',
                                                                            #     width=460,
                                                                            #     border_radius=0
                                                                            # ),
                                                                        ],
                                                                        spacing=0
                                                                        ),
                                                                        padding=10
                                                                    ),

                                                                    Container(
                                                                        content=Row([
                                                                            TextField(
                                                                                value='Months',
                                                                                width=130,
                                                                                border_radius=0,
                                                                                bgcolor='grey',
                                                                                disabled=True,
                                                                                color='white'
                                                                            ),
                                                                            self.month_droopdown, #Dropdown
                                                                            # TextField(
                                                                            #     ref=self.session_to_ref,
                                                                            #     value='--selecte--',
                                                                            #     width=460,
                                                                            #     border_radius=0
                                                                            # ),
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





