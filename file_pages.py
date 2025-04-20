import asyncio  # make sure it's at the top
from flet import *
from datetime import datetime
from database import Database
from sending_email import SendingEmail
import sqlite3
import socket # for checking internet connection
import time


db = Database()
send_message = SendingEmail()
progress = ProgressBar(
                color = "black"
            )

set_year = [] # it set on year text field  year value from database



class Athintication:
    def __init__(self,page:Page):
        self.page = page



        self.current_date = datetime.now().strftime("%d") 
        # print("\n\n\nhere is curent time",self.current_date)

        self.error_text_ref = Ref[Text]()
        self.year_text_ref = Ref[TextField]()
        

        self.my_data_table = DataTable(
            columns=[
                DataColumn(Text("RIG NO")),
                DataColumn(Text("Name")),
                DataColumn(Text('F/Name')),
                DataColumn(Text("Class")),
                DataColumn(Text("Present or absent")),
            ],
            rows=[],
            column_spacing=10
        )
        
        

         # ********************** data for attendness record end ************************************


    # when it fucntion call, so in then fucntion body code, get all record of student info 
    def get_student_record(self,session_name): # it fucntion call from option table 

        attendance_dropdwon = Dropdown(
                                options=[
                                    dropdown.Option("Yes"),
                                    dropdown.Option("No"),
                                ],
                                height=40,
                                width=300
                            )
        self.all_student_record = db.get_student_record_rendom_tablse(session_name) #that is another file class methon, which get record from datebase

        self.rig_no_set_on_dropdown = "" # when below loop excutrion start, than give it rig no and set on datatable in loop
        
        self.my_data_table.rows.clear()
        self.my_data_table.update()

        for index, x in enumerate(self.all_student_record):
            # Unique dropdown for each row
            dropdown_item = Dropdown(
                width=300,
                height=40,
                options=[
                    dropdown.Option("Yes"),
                    dropdown.Option("No")
                ],
                
                value=None,  # or default to "Yes"/"No"
                # on_change=lambda e, i=index: self.dropdown_changed(e, i)  # pass row index
            )
            self.my_data_table.rows.append(
                DataRow(
                    cells=[
                        DataCell(TextField(height=40, value=x[0], width=600)),
                        DataCell(TextField(height=40, value=x[1]+x[2], width=300)),
                        DataCell(TextField(height=40, value=x[3], width=300)),
                        DataCell(TextField(height=40, value=x[12], width=300)),
                        DataCell(dropdown_item),  # <- Here's the dropdown
                    ]
                )
            )
        self.my_data_table.update()




    def check_internet_connection(self):
        try:
            # Try to connect to Google's DNS
            socket.create_connection(("8.8.8.8", 53), timeout=3)
            return True
        except OSError:
            return False



    
        
    def input_search(self, e):
        # print("chnaging fucntion calling.....")
        keyword = e.control.value.strip().lower()

        if keyword == "":
            # Reload full table
            self.get_student_record(self.session_name)
        else:
            # Filter from previously loaded records
            filtered = [
                x for x in self.all_student_record 
                if keyword in f"{x[1]}{x[2]}".lower() or keyword in str(x[0]).lower()
            ]

            self.my_data_table.rows.clear()

            if filtered:
                for x in filtered:
                    dropdown_item = Dropdown(
                        width=300,
                        height=40,
                        options=[dropdown.Option("Yes"), dropdown.Option("No")],
                        value=None
                    )

                    self.my_data_table.rows.append(
                        DataRow(
                            cells=[
                                DataCell(TextField(height=40, value=x[0], width=600)),
                                DataCell(TextField(height=40, value=x[1] + x[2], width=300)),
                                DataCell(TextField(height=40, value=x[3], width=300)),
                                DataCell(TextField(height=40, value=x[12], width=300)),
                                DataCell(dropdown_item),
                            ]
                        )
                    )
            # Optionally show a message or keep table empty if no match
            self.my_data_table.update()






    # it when you click on submit btn it get all data from DataTable
    #  and attendness in database
    def submit_attendness(self, e):
        print("submit_attendness fucntion is calling")
        session = self.cls_dropdown.value # take value from session dropdown list
        month = self.month_dropdown.value
        year = datetime.now().strftime("%Y") # it take current year from system
        date_now = self.date.value # it take value from date TextField i
        date_now = date_now[18:20] # to remove demo text and get date from date TextField

        session_month = f"_{session}_{month}_{year}"
        # print(session_month)
        
        
        # if you internet connected than it return True other wise reture false 
        internet = self.check_internet_connection()
        global progress
        self.page.views.append(progress)
        self.page.update()

        
        # progress.open = True
        # progress.update()

        # self.page.update()
        # count = 0
        
        # Take value from Atendness DataTable
        for row in self.my_data_table.rows:
            rig_no = row.cells[0].content.value
            name = row.cells[1].content.value
            f_name = row.cells[2].content.value
            email = row.cells[3].content.value
            attendness = row.cells[4].content.value
            month = self.month_dropdown.value

            # progress.value = count*0.001
            # time.sleep(0.0001) # stop excution one second and start when loop excuted first itme then sleep one second and start again
            # print(f"counter: {count}")
            # count = count + 1 # count increament

            
            # print(f"currint date: {date_now},  rig no: {rig_no},  name: {name}, F/Name: {f_name}, email: {email}, attendness: {attendness}, Month: {month}")

            try:
                # db.insert_single_day_attendance(session_month,rig_no, date_now, attendness)
                # print("table",session_month,rig_no, date_now[18:20], attendness)
                db.insert_single_day_attendance(session_month,rig_no, date_now, attendness)

                if internet:
                    # firt you need to check internet connect connect
                    send_message.email(email, name, date_now, month, attendness) # to send email it studet is present or absent from email file code
                    self.page.snack_bar = SnackBar(
                        content=Text("attendance make successfully, and send email to condidates"),
                        bgcolor="green"
                    )
                    self.page.snack_bar.open = True
                    self.page.update()
                    print("email send")
                else:
                    self.page.snack_bar = SnackBar(
                        content=Text("attendance make successfully, but email not sent  becuse internet not connected",color='black'),
                        bgcolor="yellow"
                    )
                    self.page.snack_bar.open= True
                    self.page.update()
                    print("email skiped")

            except sqlite3.IntegrityError as e:
                # print(f"IntegrityError: {e}")
                self.error_text_ref.current.value = str(e)
                self.error_text_ref.current.update()
                

            except Exception as e:
                # print(f"Error: {e}")
                self.error_text_ref.current.value = str(e)
                self.error_text_ref.current.update()
            
            

    

    # Get values of drop down lists
    def option(self, e):
        self.session_name =self.cls_dropdown.value
        self.month = self.month_dropdown.value
        # self.year_value  = self.year_dropdown.value
        # print("clss ", self.session_name)  
        # print("month", self.month)
        # print("year: ", self.year)
        self.year_text_ref.current.value = str(datetime.now().strftime("%Y"))
        self.year_text_ref.current.update()

        if self.session_name:
            self.get_student_record(self.session_name)
            
            table = db.get_all_tables() # get all table from database sqlite

            # that is clear old item from dropdown list, and add new for the help of below loop
            self.month_dropdown.options.clear()
            # self.year_dropdown.options.clear()
           


            # Add table in month_dropdown list for the help of loop 
            for i in table:
                i = i[0]
                # print(i[0:17])
                if i[0:17] == f"_{self.session_name}":
                    self.month_dropdown.options.append(
                        dropdown.Option(i[18:-5])
                    )
                    # self.year_dropdown.options.append(
                    #             dropdown.Option(i[-4:])
                    #         )

                # ******************* it dublicate years remove and just sign year name add on set 
                # set_year list after that we will make loop on global set_year: list
                    # year = []
                    # year.append(i[-4:])

                    # global set_year
                    # for y in year:
                    #     if y not in set_year:
                    #         set_year.append(y)
                    # *****************


            # for j in set_year:
            #     self.year_dropdown.options.append(
            #                     dropdown.Option(j[-4:])
            #                 )

            self.month_dropdown.update()
            # self.year_dropdown.update()
            # global set_year
            # print(f"it blobal year: {set_year}")


        


        
            self.page.update()
            print("after")
        else: 
            print("false") 




    def send_mail(self, e):
        
        pass
        # session = self.cls_dropdown.value # take value from session dropdown list
        # month = self.month_dropdown.value
        # year = datetime.now().strftime("%Y") # it take current year from system
        # date_now = self.date.value # it take value from date TextField i
        # date_now = date_now[18:20] # to remove demo text and get date from date TextField

        # session_month = f"_{session}_{month}_{year}"
        
        # global lsit_store_email
        # print(lsit_store_email)

        # if session == "" and month == "" and year == "" and date_now == "":
        #     self.error_text_ref.current.value = "please SELECT all field"
        #     self.error_text_ref.current.update()

        # else:
        #     self.error_text_ref.current.value = ""
        #     self.error_text_ref.current.update()
            # try:
                

            # except Exception as e:
            #     print(f"error message:  {e}") 




    def Atendness_page(self):
            
            self.date= TextField(
                    # value='Type all date eg. 2121172818',
                    width=200,
                    height=40,
                    border_radius=border_radius.only(top_left=0,bottom_left=0)
                )

            # Session dropdown list
            self.cls_dropdown =Dropdown(
                            options=[
                                # dropdown.Option('1st Semester')
                            ],
                            border_radius=0,
                            on_change=self.option
                        )
            self.tables = db.get_all_tables() # get all table from database sqlite
            # set drop down opotion from database (sqlite table make up dropdwon list)
            for i in self.tables:
                i = i[0] #use Index
                session= i[0:7] #use slice on table first 7 charecters
                if session == 'session':
                    # Add all SqLite tables on dowpdown list
                    self.cls_dropdown.options.append(
                            dropdown.Option(i)
                        )



            # Month dropdown list 
            self.month_dropdown =Dropdown(
                        options=[
                            # "here is app Option for the help of loop"
                        ],
                        border_radius=0,
                        width=200,
                        height=40,
                        content_padding=0,
                        on_change=self.option
                    )

            
            # Year dropdown list 
            # Month dropdown list 
            # self.year_dropdown =Dropdown(
            #             options=[
            #                 # "here is app Option for the help of loop"
            #             ],
            #             border_radius=0,
            #             width=200,
            #             height=40,
            #             content_padding=0,
            #             on_change=self.option
            #         )


           
            self.date.value=f"Type all date eg. {self.current_date}"

            app_bar = self.page.appbar = AppBar(
                # title=Text("Flet Navigation Drawer"),
                bgcolor='green',
                # height=30,
            )

            return View(
            "/attendness",
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
                                                Icon(name=icons.LAPTOP_OUTLINED),
                                                Text("Class Attendness")
                                            ]),
                                            Text("        Save Daily Roll Call",size=10),
                                            
                                        ],
                                        spacing=0
                                        ),
                                        width=1366,
                                        height=42,
                                        # bgcolor='yellow',
                                        bgcolor='white',

                                    ),
                                    
                                    Container(
                                        content=Container(          # nested Container
                                            content=Column([  # main Column
                                                Container(
                                                    content=Column([
                                                            Container(
                                                                Text("Class Atendness",size=30,color='white',font_family=FontWeight.BOLD),
                                                                bgcolor='green',
                                                                # width=1080,
                                                                alignment=alignment.center
                                                            ),
                                                            Container(
                                                                content=Row([
                                                                    TextField(
                                                                        value=' Session',
                                                                        width=130,
                                                                        border_radius=0,
                                                                        bgcolor='grey',
                                                                        disabled=True,
                                                                        color='white',
                                                                        content_padding=0
                                                                    ),
                                                                    self.cls_dropdown, # it is a drop down list define in it function body
                                                                    Container( # it container set for empty space
                                                                        # bgcolor="green",
                                                                        width=200,
                                                                        height=30,
                                                                        alignment=alignment.center
                                                                    ),
                                                                    Container(
                                                                        content=Text("View class comments",font_family=FontWeight.BOLD, color='white'),
                                                                        bgcolor="green",
                                                                        width=170,
                                                                        height=40,
                                                                        alignment=alignment.center,
                                                                        ink= True,
                                                                        on_click = self.send_mail
                                                                    ),
                                                                    Container( # it container set for empty space
                                                                        # bgcolor="green",
                                                                        width=140,
                                                                        height=30,
                                                                        alignment=alignment.center
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
                                                    content=Row([
                                                        # it is for data and textfile of data 
                                                        Row([
                                                            TextField(
                                                                value=' Date',
                                                                width=70,
                                                                height=40,
                                                                disabled=True,
                                                                bgcolor='grey',
                                                                border_radius=border_radius.only(top_right=0,bottom_right=0),
                                                                color='white',
                                                                content_padding=0
                                                            ),
                                                            self.date # it is a text field define in it function body
                                                        ],
                                                        spacing=0
                                                        ),
                                                        # it is for term and textfi
                                                        Row([
                                                            TextField(
                                                                value=' Month',
                                                                width=70,
                                                                height=40,
                                                                disabled=True,
                                                                bgcolor='grey',
                                                                border_radius=border_radius.only(top_right=0,bottom_right=0),
                                                                color='white',
                                                                content_padding=0
                                                            ),
                                                            # TextField(
                                                            #     value='month here',
                                                            #     width=250,
                                                            #     height=40,
                                                            #     border_radius=border_radius.only(top_left=0,bottom_left=0)
                                                            # )
                                                            self.month_dropdown,
                                                        ],
                                                        spacing=0
                                                        ),

                                                        # it is for session 
                                                        Row([
                                                            TextField(
                                                                value='  Year',
                                                                width=70,
                                                                height=40,
                                                                disabled=True,
                                                                bgcolor='grey',
                                                                border_radius=border_radius.only(top_right=0,bottom_right=0),
                                                                content_padding=0,
                                                                color="white",
                                                            ),
                                                            TextField(
                                                                value='  --Year--',
                                                                ref=self.year_text_ref,
                                                                width=200,
                                                                height=40,
                                                                border_radius=border_radius.only(top_left=0,bottom_left=0),
                                                                content_padding=0,
                                                                disabled = True,
                                                            ),
                                                            # self.year_dropdown,
                                                            
                                                        ],
                                                        spacing=0
                                                        ),

                                                        Row([
                                                            TextField(
                                                                value=' Search',
                                                                width=70,
                                                                height=40,
                                                                disabled=True,
                                                                bgcolor='grey',
                                                                border_radius=border_radius.only(top_right=0,bottom_right=0),
                                                                content_padding=0,
                                                                color="white",
                                                            ),
                                                            TextField(
                                                                # value='  --Search--',
                                                                width=250,
                                                                height=40,
                                                                border_radius=border_radius.only(top_left=0,bottom_left=0),
                                                                content_padding=0,
                                                                on_change = self.input_search # it function call, than searching in datatable
                                                            ),
                                                        ],
                                                        spacing=0
                                                        ),

                                                       
                                                    ],
                                                    spacing=70
                                                    ),
                                                    # border=border.all(width=2)

                                                ),
                                                Container(

                                                    # content=Column([
                                                    #         self.my_data_table,

                                                    #         ],
                                                    #     scroll='always',
                                                    #     width=1130
                                                    #     ),
                                                    # """ but ListView is best """
                                                    content=ListView(
                                                                controls=[
                                                                    self.my_data_table
                                                                ],
                                                                # scroll='always',
                                                                expand=True
                                                            ),
                                                    # content=self.my_data_table,
                                                    width=1390,
                                                    bgcolor='yellow',
                                                    height=355,
                                                    border_radius=20,
                                                    border=border.all(width=2),
                                                    
                                                ),

                                                # back btn and
                                                Row([

                                                    #back btn
                                                    TextButton(
                                                        text='Back',
                                                        # height=10,
                                                        on_click= lambda e: e.page.go("/home_page"),
                                                    ),
                                                    
                                                    # it for error message
                                                    Container(
                                                        content=Text(
                                                            # "It's for error text",
                                                            ref=self.error_text_ref,
                                                            color="red",
                                                        ),
                                                        # bgcolor="blue",
                                                        width=700,
                                                    ),

                                                    # submite btn
                                                    ElevatedButton(text="Submit",bgcolor='blue',width=150,color="white",on_click=self.submit_attendness)
                                                    
                                                ],spacing=180)
                                            ]),
                                            bgcolor='white',
                                            opacity=0.8,
                                            # border=border.all(width=3,color='green'),
                                            padding=padding.only(left=10,top=10,right=10,bottom=0),
  
                    
                                        ),
                                        padding=padding.only(left=10,top=10,right=10,bottom=25),
                                        # bgcolor= 'grey',
                                        image_src="images/bg.jpg",  # Ensure this image is in the same directory as your script
                                        expand=True,  # Fills the screen
                                        image_fit="cover",  # Covers the entire background
                                        width=1366,
                                        height= 635,

                                    ),
                                ],
                                spacing=0    

                            ),
                            # border=border.all(width=3,color='red'),
                            # width=1190,
                            
                        ),
                    ]
                )
            ]
        )


