from flet import *
from database import Database
import sqlite3
db = Database()

total_salaries = 0
class NewStaff:
    def __init__(self,page:Page):
        self.page = page

        # Make a Ref of textfelds
        self.total_salaries_ref = Ref[Text]()
        self.staff_name_ref = Ref[TextField]()
        self.staff_cnic_ref = Ref[TextField]()
        self.staff_mobile_ref = Ref[TextField]()
        self.staff_salary_ref = Ref[TextField]()


        self.full_staff_record = db.get_staff_record()
        # here i a data table
        self.staff_table=DataTable(
            columns=[
                DataColumn(Text("S/NO")),
                DataColumn(Text("STAFF NAME")),
                DataColumn(Text("NATIONAL ID CARD NO")),
                DataColumn(Text("MOBILE")),
                DataColumn(Text("SALARY")),
                DataColumn(Text("Action")),
            ],
            rows=[],
            column_spacing=100,
            heading_row_color="green",
            # horizontal_lines=1
            # border=border.all(width=1)
            # bgcolor="grey",
            horizontal_lines=border.all(width=1),
            # vertical_lines=border.all(width=1),
            border=border.all(width=1)
            

        )

        global total_salaries
        total_salaries = 0

        self.full_staff_record = db.get_staff_record()
        # isert data in table for the help of loop 

        for i in self.full_staff_record:
            # print(i)
            self.staff_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(i[0])),
                        DataCell(Text(i[1])),
                        DataCell(Text(i[3])),
                        DataCell(Text(i[2])),
                        DataCell(Text(i[4])),
                        DataCell(  # it is icon btn
                            IconButton(
                                icon=icons.DELETE,
                                icon_color='red',
                                data = i[0],
                                on_click= self.delete_record
                            )
                        ),
                        
                    ]
                )
            )
            self.page.update()
            total_salaries = total_salaries + i[4]


    def auto_set_salaries(self,e):
        print("are  you calling")
        
        global total_salaries
        self.total_salaries_ref.current.value = str(total_salaries)
        self.total_salaries_ref.current.update()


    # it a snack_bar bar fucntion, when i need to show error on snack_bar i will call it 
    def snack_bar(self, message):
        self.page.snack_bar = SnackBar(
            content= Text(f"{message}"),
            bgcolor='red',
        )
        self.page.snack_bar.open = True
        self.page.update()


    def get_values_of_staff(self, e):
        # get values of textfields for the help of ref and store in variable 
        staff_name = self.staff_name_ref.current.value
        staff_cnic = self.staff_cnic_ref.current.value
        staff_mobile = self.staff_mobile_ref.current.value
        staff_salary = self.staff_salary_ref.current.value


        self.is_staff_name_valid = False
        self.is_staff_cnic_valid = False
        self.is_staff_mobile_valid = False
        self.is_staff_salary_valid = False
        
        # print variables values that you have assign from textfields for the help of Ref
        # print(staff_name)
        # print(staff_cnic)
        # print(staff_mobile)
        # print(staff_salary)

        if staff_name == "":
            # self.staff_name_ref.current.error_text = "You need to fill it"
            self.is_staff_name_valid = False
            # self.staff_name_ref.current.update()
            self.snack_bar("Please enter staff name") # call user define snack_bar fucntion
        else:
            # self.staff_name_ref.current.error_text = None
            self.is_staff_name_valid = True
            # self.staff_name_ref.current.update()

        if staff_cnic != "" and len(staff_cnic) == 13:
            # self.staff_cnic_ref.current.error_text = None
            self.is_staff_cnic_valid = True
            # self.staff_cnic_ref.current.update()
        else:
            # self.staff_cnic_ref.current.error_text = "You need to fill it"
            self.is_staff_cnic_valid = False
            # self.staff_cnic_ref.current.update()
            self.snack_bar("Please check you Nationl ID Card field") # call user define snack_bar fucntion

        if staff_mobile != "" and len(staff_mobile) == 11 :
            # self.staff_mobile_ref.current.error_text = None
            self.is_staff_mobile_valid = True
            # self.staff_mobile_ref.current.update()
        else:
            # self.staff_mobile_ref.current.error_text = "You need to fill it"
            self.is_staff_mobile_valid = False
            self.snack_bar("Please enter Mobile number") # call user define snack_bar fucntion
            # self.staff_mobile_ref.current.update()
        
        try:
            staff_salary = int(staff_salary)
            if type(staff_salary) == int and staff_salary != 0:
                # self.staff_salary_ref.current.error_text = None
                self.is_staff_salary_valid = True
                # self.staff_salary_ref.current.update()
            
            else:
                # self.staff_salary_ref.current.error_text = "You need to fill it"
                self.is_staff_salary_valid = False
                # self.staff_salary_ref.current.update()
                self.snack_bar("Please enter salary") # call user define snack_bar fucntion
        except:
            self.snack_bar("check salary field") # call user define snack_bar fucntion
        
        
        # if all condition True then excute if block other esle
        if self.is_staff_name_valid and self. is_staff_cnic_valid and self.is_staff_mobile_valid and self.is_staff_salary_valid:
            try:
                # print('if bloxk')
                # print(self.is_staff_name_valid)
                # print(self.is_staff_cnic_valid)
                # print(self.is_staff_mobile_valid)
                # print(self.is_staff_salary_valid)
                db.insert_staff(staff_name, staff_cnic, staff_mobile, staff_salary)

                self.staff_name_ref.current.value = ""
                self.staff_cnic_ref.current.value = ""
                self.staff_mobile_ref.current.value = ""
                self.staff_salary_ref.current.value = ""

            except sqlite3.IntegrityError:
                self.page.snack_bar = SnackBar(
                    content=Text("Error: Duplicate CNIC not allowed!"),
                    bgcolor='red',
                )
                self.page.snack_bar.open = True
                self.page.update()


            except Exception as e:
                self.page.snack_bar = SnackBar(
                    content=Text(str(e)),
                    bgcolor='red',
                )
                self.page.snack_bar.open = True
                self.page.update()

            

            
            
        else:
            print("else block")
            print(self.is_staff_name_valid)
            print(self.is_staff_cnic_valid)
            print(self.is_staff_mobile_valid)
            print(self.is_staff_salary_valid)

        

        
        # print(self.full_staff_record[-1])
        self.update_data_table() #clall update fucntion to table update, when you click save btn

    def update_data_table(self):

        global total_salaries
        total_salaries = 0

        # here is update you table
        self.full_staff_record = db.get_staff_record()
        # isert data in table for the help of loop
        self.staff_table.rows.clear()
        self.staff_table.update()
        for i in self.full_staff_record:
            # print(i)
            self.staff_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(i[0])),
                        DataCell(Text(i[1])),
                        DataCell(Text(i[3])),
                        DataCell(Text(i[2])),
                        DataCell(Text(i[4])),
                        DataCell(  # it is icon btn
                            IconButton(
                                icon=icons.DELETE,
                                icon_color='red',
                                data = i[0],
                                on_click= self.delete_record
                            )
                        ),
                        
                    ]
                ),
                
            )
            self.staff_table.update()
            self.page.update()
            total_salaries = total_salaries + i[4]

            

        print(f"your total salries is: {total_salaries}")
        self.total_salaries_ref.current.value = str(total_salaries)
        self.total_salaries_ref.current.update()


    # when you click on app bar btn call it than open navigarion drawer 
    def open_drawer(self, e):
        self.page.drawer.open = True  # Open the drawer when button is clicked
        print("open_drawer function callling....")
        self.page.update()

    def delete_record(self,id):
        delete_id = id.control.data
        print(delete_id)
        db.delete_staff(delete_id, "staff")
        self.update_data_table()

    # it is Managment page
    def add_new_staff(self):
    #     # here i a data table


        # Navigation Drawer
        self.page.drawer = NavigationDrawer(
                controls=[
                        Container(height=50),  # Space at the top
                        NavigationDrawerDestination(icon=icons.HOME, label="Home"),
                        NavigationDrawerDestination(icon=icons.SETTINGS, label="Settings"),
                        NavigationDrawerDestination(icon=icons.INFO, label="About"),
                    ]
                )

            # it ia App Bar 
        app_bar = self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                leading=IconButton(icon=icons.MENU, on_click=self.open_drawer),
                bgcolor='green',
                # height=30,
            )
    

        return View(
            "add_new_student",
            # padding=0,
            padding=0,
            controls=[
                app_bar,
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
                        #                 # it is for administrative manager 
                        #                 Container(
                        #                     height= 50,
                        #                     bgcolor= 'black',
                        #                     content=Row([
                        #                         IconButton(icon=icons.ADD),
                        #                         Text('Add new student',color='white')
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : print(f"here make a clickable: {e}")
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
                        #                     bgcolor= 'grey',
                        #                     content=Row([
                        #                         IconButton(icon=icons.CHECK),
                        #                         Text('Class Managment',font_family=FontWeight.BOLD)
                        #                     ]),
                        #                     ink = True,
                        #                     on_click = lambda e : e.page.go("/managment")
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
                                                    content=Column([
                                                            Container(
                                                                Text("Add New Staff Payroll",size=30,color='white',font_family=FontWeight.BOLD),
                                                                bgcolor='green',
                                                                # width=1080,
                                                                alignment=alignment.center
                                                            ),
                                                            Container(
                                                                content=Row([

                                                                    # enter name of new staff 
                                                                    Row([
                                                                        TextField(
                                                                            value=' Staff Name',
                                                                            width=96,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white',
                                                                            content_padding=0
                                                                        ),
                                    
                                                                        TextField(
                                                                            value='---Enter New Staff---',
                                                                            width=200,
                                                                            border_radius=0,
                                                                            ref=self.staff_name_ref
                                                                        ),
                                                                    ],spacing=0),
                                                                    # cnic of new staff
                                                                    Row([
                                                                        TextField(
                                                                            value=' Nationl ID *',
                                                                            width=96,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white',
                                                                            content_padding=0,
                                                                        ),
                                    
                                                                        TextField(
                                                                            value='---Enter Natonal ID---',
                                                                            width=200,
                                                                            border_radius=0,
                                                                            ref=self.staff_cnic_ref
                                                                        ),

                                                                    ],spacing=0),

                                                                    # mobile no of staff
                                                                     Row([
                                                                        TextField(
                                                                            value=' Mobile',
                                                                            width=90,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white',
                                                                            content_padding=0,
                                                                        ),
                                    
                                                                        TextField(
                                                                            value='---Enter mobile number---',
                                                                            width=200,
                                                                            border_radius=0,
                                                                            ref=self.staff_mobile_ref,
                                                                        ),

                                                                    ],spacing=0),
                                                                   

                                                                    # salary of staff
                                                                    Row([
                                                                        TextField(
                                                                            value=' Salary',
                                                                            width=90,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white',
                                                                            content_padding=0
                                                                        ),
                                    
                                                                        TextField(
                                                                            value='---Enter Salary---',
                                                                            width=200,
                                                                            border_radius=0,
                                                                            ref=self.staff_salary_ref
                                                                        ),

                                                                    ],spacing=0),
                                                                    # Save btn 
                                                                    ElevatedButton(text="Save",bgcolor="green",color="white",on_click=self.get_values_of_staff),
                                                                    # 

                                                                    
                                                                    
                                                                ],
                                                                spacing=5
                                                                ),
                                                                padding=10
                                                            ),

                                                            # contaner for set view staff  payroll text
                                                            Container(
                                                                content=Text("View staff Payroll",size=20,font_family=FontWeight.BOLD),
                                                            alignment=alignment.center
                                                            ),

                                                            # Make a container for set DataTable
                                                            Container(
                                                                content=ListView([
                                                                    # self.my_data_table
                                                                    self.staff_table,
                                                                    
                                                                    # it contaner make total of staff slaries ``
                                                                    Container(
                                                                        content=Row([
                                                                                Text("     Total Staff Salaries",size=20,font_family='bold'),
                                                                                
                                                                                Row([
                                                                                    Text(
                                                                                    "****",
                                                                                    ref=self.total_salaries_ref,
                                                                                    size=20,
                                                                                    ),
                                                                                    ElevatedButton(text='show',bgcolor="grey",color="white",on_click=self.auto_set_salaries)
                                                                                ]),

                                                                            ],spacing=900),
                                                                        bgcolor='grey',
                                                                        border=border.all(width=1)
                                                                    )
                                                                ]),
                                                                # bgcolor='grey',
                                                                padding=10,
                                                                height=390,
                                                                # border=border.all(width=1)

                                                            )

                                                        ],
                                                        spacing=0
                                                        ),
                                                    border=border.all(width=2),
                                                    height=530
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



