from flet import *
from database import Database
from edit_student_page import EditStudent 
from view_student import ViewStudent
from edit_student_page import EditStudent
from view_student import ViewStudent
db = Database()

class ClassManagment:
    def __init__(self,page:Page):
        self.page = page
        self.ob =EditStudent(self.page)
        self.view_page_ob = ViewStudent(self.page)


        # ********************** data for attendness record start ************************************
        # self.full_student_record = db.get_student_record()
        # self.full_student_record = self.full_student_record[0]
        # for i in self.full_student_record:
        #     print(f"{count}: {i}")
        #     count = count + 1
        # print()
        # ********************** data for student mangment record start ************************************
        


        

        # self.student_data_table = DataTable(
        #     columns=[
        #         DataColumn(Text('id')),
        #         DataColumn(Text("RIG NO")),
        #         DataColumn(Text("Name")),
        #         DataColumn(Text("Class")),
        #         DataColumn(Text("Roll no")),
        #         DataColumn(Text("Action")),
        #     ],
        #     rows=[]
        # )
        
        # # for i in self.data:
        # for i in self.full_student_record:
        #     self.student_data_table.rows.append(
        #         DataRow(
        #             cells=[
        #                 DataCell(Text(i[0])),
        #                 DataCell(Text(i[1])),
        #                 DataCell(Text(i[2] + i[3])), # concatenet first name and last name
        #                 DataCell(Text("BS Cs")),
        #                 DataCell(Text(i[6])),
        #                 DataCell(Row([
        #                     # now create edit and delete btn
        #                     IconButton(
        #                         icon='create',
        #                         icon_color='blue',
        #                         data=i,
        #                         on_click=self.for_edit_record
        #                     ),
        #                     IconButton(
        #                         icon='delete',
        #                         icon_color='red',
        #                         data=i[0],
        #                         on_click=self.for_delete_record
        #                         # on_click= self.showedit(i)
        #                     ),
        #                 ])),
                        
        #             ]
        #         )
        #     )


                # ********************** data for student managment  record end ************************************
    
    # when you click on app bar btn call it than open navigarion drawer 

    def open_drawer(self, e):
        if self.page.drawer:  # Ensure the drawer exists before opening
            self.page.drawer.open = True  # Open the drawer
            print("open_drawer function calling....")
            self.page.drawer.update()  # Update the drawer UI
        else:
            print("Drawer is not initialized!")

    # when you click edit btn on managment page that call it fuction and recive here single student record on a student 
    def for_edit_record(self,id):
        print(f"i called seccessfuly ......... and i am form edit function record")
        edit_id = id.control.data
        if self.table_name != "":
            self.ob.get_row(edit_id,self.table_name) # Note: self.((table_name)) location in the option function in current page
            self.page.go("/edit_student_page")
        else:
            print("else class managment")
    

    # when you click on view btn in managment page  it call ui_ready function which is located in View page
    def view_student_record(self,id):
        print(f"i called seccessfuly ......... and i am form view_student_record function record")
        view_row = id.control.data
        # print(edit_id)
        # self.view_page_ob.set_values_text(view_row)
        self.view_page_ob.ui_ready(view_row)
        self.page.go("/view_student")

    # when you click delete btn on managment page that call it fuction and recive here id on a student 
    def for_delete_record(self, id):
        print("i called successfullu........ and i and from delete fuction")
        data_delete = id.control.data
        try:
            db.delete_student(data_delete,self.table_name ) # call databaae file fucntion to delete student
            self.update_data_table(self.table_name) # and update page when studet deleted
        except:
            self.page.snack_bar = SnackBar(
                content= Text("Something went wrong, student not deleted"),
                bgcolor = "red"
            ),
            self.page.snack_bar.open = True
            self.page.update()
        
        print("My ID: ",data_delete)


    # get valus form lies
    def option(self, e):
        self.table_name =self.student_class.value
        self.update_data_table(self.table_name)
        print("clss ", self.table_name)

    def update_data_table(self,table_name):
        print("yess i am calling")
        print("here is your table name: ", table_name)
        self.student_data_table.rows.clear()
        self.student_data_table.update()
        self.full_student_record = db.get_student_record_rendom_tablse(table_name) 
            
        # for i in self.data:
        for i in self.full_student_record:
            self.student_data_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(i[0])),
                        DataCell(Text(i[1] +" "+ i[2])), # concatenet first name and last name
                        DataCell(Text(i[3])),
                        DataCell(Text("BS Cs")),
                        DataCell(Text(i[5])),
                        DataCell(Row([
                            # now create edit and delete btn
                            IconButton(
                                icon='create',
                                icon_color='blue',
                                data=i,
                                on_click=self.for_edit_record
                            ),
                            IconButton(
                                icon='delete',
                                icon_color='red',
                                data=i[0],
                                on_click=self.for_delete_record
                                # on_click= self.showedit(i)
                            ),

                            TextButton(
                                # icon='create',
                                # icon_color='blue',
                                text='View',
                                data=i,
                                on_click=self.view_student_record
                            ),
                        ])),
                    ]
                )
            )
            self.student_data_table.update()




    

    # it is Managment page
    def managment(self):
            

            # here i a data table
            self.student_class =Dropdown(
                            options=[
                                # dropdown.Option('1st Semester'),
                                # dropdown.Option("2nd Semester"),

                            ],
                            border_radius=0,
                            width=460,
                            on_change=self.option
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
                



            self.page.drawer = NavigationDrawer(
                controls=[
                    NavigationDrawerDestination(icon=icons.HOME, label="Home"),
                    NavigationDrawerDestination(icon=icons.SETTINGS, label="Settings"),
                    NavigationDrawerDestination(icon=icons.INFO, label="About"),
                ]
            )
            
    

            # )
            self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                leading=IconButton(icon=icons.MENU, on_click=self.open_drawer),  # Call open_drawer on click
                bgcolor="green",
            )

            self.student_data_table = DataTable(
                columns=[
                    DataColumn(Text("RIG NO")),
                    DataColumn(Text("Name")),
                    DataColumn(Text('F.Name')),
                    DataColumn(Text("Class")),
                    DataColumn(Text("Roll no")),
                    DataColumn(Text("Action")),
                ],
                rows=[]
            )

    

            return View(
            "/",
            # padding=0,
            padding=0,
            controls=[
                # app_bar,
                self.page.appbar,
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
                        #                 # it is for add new student 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.ADD),
                        #                         Text('Add new student',)
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : e.page.go("/add_new_student")
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
                        #                     bgcolor= 'black',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('Class Managment',color='white',font_family=FontWeight.BOLD)
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
                                                Container(
                                                    content=Column([
                                                            Container(
                                                                Text("Class Managment",size=30,color='white',font_family=FontWeight.BOLD),
                                                                bgcolor='green',
                                                                alignment=alignment.center,
                                                                
                                                            ),
                                                            Container(
                                                                content=Row([
                                                                    TextField(
                                                                        value='Student class',
                                                                        width=130,
                                                                        border_radius=0,
                                                                        bgcolor='grey',
                                                                        disabled=True,
                                                                        color='white'
                                                                    ),
                                                                    # TextField(
                                                                    #     value='--selecte--',
                                                                    #     width=460,
                                                                    #     border_radius=0
                                                                    # ),
                                                                    self.student_class, # it is drop down list define in it function body
                                                                    Container( # it container set for empty space
                                                                        # bgcolor="green",
                                                                        width=70,
                                                                        height=30,
                                                                        alignment=alignment.center
                                                                    ),
                                                                    # create new class btn
                                                                    Container(
                                                                        content=Text("Create New class",font_family=FontWeight.BOLD, color='white'),
                                                                        bgcolor="green",
                                                                        width=170,
                                                                        height=40,
                                                                        alignment=alignment.center,
                                                                        ink=True,
                                                                        on_click = lambda e: e.page.go("/new_class")
                                                                    ),
                                                                    
                                                                    Container( # it container set for empty space
                                                                        # bgcolor="green",
                                                                        width=70,
                                                                        height=30,
                                                                        alignment=alignment.center
                                                                    ),

                                                                    # create new month 
                                                                    Container(
                                                                        content=Text("Add Month",font_family=FontWeight.BOLD, color='white'),
                                                                        bgcolor="green",
                                                                        width=170,
                                                                        height=40,
                                                                        alignment=alignment.center,
                                                                        ink=True,
                                                                        on_click = lambda e: e.page.go("/new_month")
                                                                    ),
                                                                    
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
                                                    # use colunm for scrolling datatable items rows
                                                    # content=self.student_data_table,
                                                    # content=Column(
                                                    #         controls=[
                                                    #             self.student_data_table
                                                    #         ],
                                                    #         scroll='always',
                                                    #         expand=True
                                                    #     ),

                                                    # """But i thing ListView is best"""
                                                    content=ListView(
                                                                controls=[
                                                                    self.student_data_table
                                                                ],
                                                                # scroll='always',
                                                                expand=True
                                                            ),
                                                    width=1330,
                                                    bgcolor='yellow',
                                                    height=400,
                                                    border_radius=20,
                                                    border=border.all(width=2)
                                                ),

                                                TextButton(
                                                    text='Back',
                                                    # height=10,
                                                    on_click= lambda e: e.page.go("/home_page"),
                                                    )
                                                
                                            ]),
                                            bgcolor='white',
                                            # border=border.all(width=3),
                                            padding=10,
                                            opacity=0.8
                    
                                        ),
                                        padding=25,
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





