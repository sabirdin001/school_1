from flet import *
from database import Database
db = Database()


set_year = []
class ViewAttendness:
    def __init__(self,page:Page):
        self.page = page

        
        # it is attendance DataTable 
        self.student_data_table = DataTable(
            columns=[
                DataColumn(Text("RIG NO ")),
                DataColumn(Text("01")),
                DataColumn(Text("02")),
                DataColumn(Text("03")),
                DataColumn(Text("04")),
                DataColumn(Text("05")),
                DataColumn(Text("06")),
                DataColumn(Text("07")),
                DataColumn(Text("08")),
                DataColumn(Text("09")),
                DataColumn(Text("10")),
                DataColumn(Text("11")),
                DataColumn(Text("12")),
                DataColumn(Text("13")),
                DataColumn(Text("14")),
                DataColumn(Text("15")),
                DataColumn(Text("16")),
                DataColumn(Text("17")),
                DataColumn(Text("18")),
                DataColumn(Text("19")),
                DataColumn(Text("20")),
                DataColumn(Text("21")),
                DataColumn(Text("22")),
                DataColumn(Text("23")),
                DataColumn(Text("24")),
                DataColumn(Text("25")),
                DataColumn(Text("26")),
                DataColumn(Text("27")),
                DataColumn(Text("28")),
                DataColumn(Text("29")),
                DataColumn(Text("30")),
                DataColumn(Text("31")),
            ],
            rows=[],
            column_spacing=24.5,
            horizontal_lines=border.all(width=1),
            vertical_lines=border.all(width=1),
            heading_row_color='blue',
            border=border.all(width=1),
        )
        
        # ********************** data for student managment  record end ************************************
    
    # when you click on app bar btn call it than open navigarion drawer 
    # def open_drawer(self, e):
        # self.page.drawer.open = True  # Open the drawer when button is clicked
        # print("open_drawer function callling....")
        # self.page.update()

    # update table and get data from dateabse 
    def update_table(self, session, month, year):
        attendness_table = db.get_attendness_record(session, month, year)
        # print("date is: ",attendness_table)
        self.student_data_table.rows.clear()
        for i in attendness_table:
            print(i[0])
            self.student_data_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(Text(i[0])),
                        DataCell(Text(i[1])),
                        DataCell(Text(i[2])),
                        DataCell(Text(i[3])),
                        DataCell(Text(i[4])),
                        DataCell(Text(i[5])),
                        DataCell(Text(i[6])),
                        DataCell(Text(i[7])),
                        DataCell(Text(i[8])),
                        DataCell(Text(i[9])),
                        DataCell(Text(i[10])),

                        DataCell(Text(i[11])),
                        DataCell(Text(i[12])),
                        DataCell(Text(i[13])),
                        DataCell(Text(i[14])),
                        DataCell(Text(i[15])),
                        DataCell(Text(i[16])),
                        DataCell(Text(i[17])),
                        DataCell(Text(i[18])),
                        DataCell(Text(i[19])),
                        DataCell(Text(i[20])),

                        DataCell(Text(i[21])),
                        DataCell(Text(i[22])),
                        DataCell(Text(i[23])),
                        DataCell(Text(i[24])),
                        DataCell(Text(i[25])),
                        DataCell(Text(i[26])),
                        DataCell(Text(i[27])),
                        DataCell(Text(i[28])),
                        DataCell(Text(i[29])),
                        DataCell(Text(i[30])),
                        DataCell(Text(i[31])),
                    ]
                )
            )
            self.student_data_table.update()

    



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
        print(edit_id)


    # when you click delete btn on managment page that call it fuction and recive here id on a student 
    def for_delete_record(self, id):
        print("i called successfullu........ and i and from delete fuction")
        data_delete = id.control.data
        print("My ID: ",data_delete)


    # get valus form lies
    def option(self, e):
        self.session_name =self.student_class.value

        print("clss ", self.session_name)

        if self.session_name:
            print("yes")
            table = db.get_all_tables() # get all table from database sqlite
            # print(table)


            # that is clear old item from dropdown list, and add new for the help of below loop
            self.month_dropdown.options.clear()
            self.year_dropdown.options.clear()

            
            # Add table in month_dropdown list for the help of loop 
            for i in table:
                i = i[0]
                
                # here is main logic: Note: you attendness tables start with underscore "_",
                # now if session i[0:17] == f"_{self.session_name}", now just attendness table add in
                # if block, other table skip it
                if i[0:17] == f"_{self.session_name}":  # here assigning month name from databaae to month dropdown
                    self.month_dropdown.options.append(
                        dropdown.Option(i[18:-5])
                    )

                    # ******************* it dublicate years remove and just sign year name add on set 
                    # set_year list after that we will make loop on global set_year: list
                    year = []
                    year.append(i[-4:])

                    global set_year
                    for y in year:
                        if y not in set_year:
                            set_year.append(y)
                    # *****************

            # it append year from blobal set year list
            for j in set_year:
                self.year_dropdown.options.append(  # here assigning YEAR name from databaae to YEAR dropdown
                    dropdown.Option(j[-4:])
                )

                    
            self.month_dropdown.update()
            self.year_dropdown.update()

            # get values from 3 dropdowns adn send to update table

            session =self.student_class.value
            month =self.month_dropdown.value
            year = self.year_dropdown.value
            print(f"1 {session}")
            print(f"1 {month}")
            print(f"1 {year}")
            if session and month and year:
                self.update_table(session,month, year)
            else: 
                print("else block in option fuction")

    # it is Managment page
    def view_attendness(self):
        # Student session dropdown list
            self.student_class =Dropdown(
                            options=[],
                            border_radius=0,
                            width=300,
                            on_change=self.option
                        )
            # get all table from db and set just session tables on dropdown lsit 
            tables = db.get_all_tables()
            for i in tables:
                i = i[0] #use Index
                session= i[0:7] #use slice on table first 7 charecters
                if i[0:7] == 'session':
                    # Add all SqLite tables on dowpdown list
                    self.student_class.options.append(
                            dropdown.Option(i)
                        )
            self.year_dropdown =Dropdown(
                            options=[],
                            border_radius=0,
                            width=300,
                            on_change=self.option
                        )


            self.month_dropdown =Dropdown(
                            options=[],
                            border_radius=0,
                            width=300,
                            on_change=self.option
                        )
                




    
            
           

            # it ia App Bar 
            # app_bar = self.page.appbar = AppBar(
            #     title=Text("Flet Navigation Drawer"),
            #     leading=IconButton(icon=icons.MENU, on_click=self.open_drawer),
            #     bgcolor='green',
            #     # height=30,
            # )
            self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                leading=IconButton(icon=icons.MENU, on_click=self.open_drawer),  # Call open_drawer on click
                bgcolor="green",
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
                        Container(
                            content=Column(
                                controls=[

                                    Container(
                                        content=Column([
                                            Row([
                                                Icon(name=icons.LAPTOP_OUTLINED),
                                                Text("GOVT: POST GRADUAT COLLAGE MIRAN SHAH")
                                            ]),
                                            Text("           District nort wazirstan",size=10),
                                            
                                        ],
                                        spacing=0
                                        ),
                                        width=1366,
                                        height=42,
                                        # bgcolor='white',
                                        # bgcolor='yellow',

                                    ),
                                    
                                    Container(
                                        content=Container(          # nested Container
                                            content=Column([  # main Column
                                                Container(
                                                    content=Column([
                                                            Container(
                                                                Text("View class Atendness",size=30,color='white',font_family=FontWeight.BOLD),
                                                                bgcolor='green',
                                                                # width=1080,
                                                                alignment=alignment.center
                                                            ),
                                                            Container(
                                                                content=Row([
                                                                    Row([
                                                                        TextField(
                                                                            value='Student class',
                                                                            width=130,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white'
                                                                        ),
                                                                        self.student_class, # it is drop down list define in it function body

                                                                    ],spacing=0),

                                                                    Row([
                                                                        TextField(
                                                                            value='Year',
                                                                            width=80,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white'
                                                                        ),
                                                                        self.year_dropdown, # it is drop down list define in it function body

                                                                    ],spacing=0),

                                                                    Row([
                                                                        TextField(
                                                                            value='Month',
                                                                            width=80,
                                                                            border_radius=0,
                                                                            bgcolor='grey',
                                                                            disabled=True,
                                                                            color='white'
                                                                        ),
                                                                        self.month_dropdown, # it is drop down list define in it function body

                                                                    ],spacing=0),
                                                                    
                                                                ],
                                                                spacing=10
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
                                                    content=Column(
                                                                controls=[
                                                                    self.student_data_table
                                                                ],
                                                                scroll='auto',
                                                                # expand=True
                                                            ),
                                                    width=1330,
                                                    bgcolor='#BCCCC9',
                                                    height=400,
                                                    # border_radius=10,
                                                    border=border.all(width=1),
                                                    # padding=padding.only(left=10,right=10)
                                                    
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





