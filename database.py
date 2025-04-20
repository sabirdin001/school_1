import sqlite3

class Database():
    def __init__(self):
        # self.con.sqlite3.connect("db.db")
        self.con = sqlite3.connect('collage_managment.db',check_same_thread=False)
        self.cursor = self.con.cursor()
        self.create_sign_up_table()
        self.create_staff_table()
        # self.create_student_personal_table()
        # self.create_acadamic_information_table()
        # self.create_tables()

        # Database file path
        # self.db_path = "collage_managment.db"
    def get_all_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        tables = self.cursor.fetchall()
        self.con.close

        return tables

    def get_all_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        tables = self.cursor.fetchall()
        self.con.close

        return tables


    def create_sign_up_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS signup_user(id integer PRIMARY KEY AUTOINCREMENT, first_name varchar(50), last_name varchar(50), f_name varchar(50), mobile varchar(50), cnic varchar(50),  email varchar(50), password varchar(100))")
        self.con.commit()
        
    def create_signup_record(self,first_name, last_name, f_name, mobile, cnic, email,password):
        self.cursor.execute("INSERT INTO signup_user(first_name, last_name, f_name,mobile, cnic, email, password) VALUES( ?, ?,?,?,?,?,?)",
        (first_name,last_name,f_name,mobile,cnic,email, password))
        self.con.commit()


    
    # read record from databaae
    def get_register_record(self):
        first_row = (self.cursor.execute("SELECT* FROM signup_user WHERE id = 1 ").fetchall())
        return first_row


    
    def forget_password(self, new_password):
        self.cursor.execute("""
            UPDATE signup_user
            SET password = ?
            WHERE id = 1
        """, (new_password,))  # Note the comma after new_password
        self.con.commit()
        print('reach passeord to database code', new_password)


    def create_staff_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS staff (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                staff_name TEXT NOT NULL,
                staff_mobile TEXT NOT NULL,
                staff_cnic TEXT UNIQUE NOT NULL,
                staff_salary REAL NOT NULL
            )
        """)

    # isert value in staff table 
    def insert_staff(self,staff_name, staff_cnic, staff_mobile, staff_salary):

        # Insert data into the table
        self.cursor.execute("""
            INSERT INTO staff (staff_name, staff_cnic,staff_mobile, staff_salary)
            VALUES (?, ?, ?, ?)
        """, (staff_name, staff_cnic, staff_mobile, staff_salary))

        # Commit the transaction and close the connection
        self.con.commit()

        print("Staff record inserted successfully!")

        

    # Function to create  new class calling... from add_new_class_page
    def create_student_table(self,session):
        
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS session{session}(
                rig_no TEXT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                father_name TEXT,
                age INTEGER,
                cnic TEXT UNIQUE,
                father_cnic TEXT,
                date_of_birth TEXT,
                mobile TEXT,
                province TEXT,
                postel_address TEXT,
                permanent_address TEXT,  -- Fixed this line
                email TEXT,
                gender TEXT,

                metric_bord TEXT,
                school_name TEXT,
                metric_total INTEGER,
                metric_obt INTEGER,
                metric_percentage REAL,
                metric_grade TEXT,

                fsc_bord TEXT,
                collage_name TEXT,
                fsc_total INTEGER,
                fsc_obt INTEGER,
                fsc_percentage REAL,
                fsc_grade TEXT,
                gambar BLOD
            )
    """)

        
        self.con.commit()


    

    # second issue ----------------------------------------->
    # def create_table_attendness(self,month, session,year):
    #     print("\n\n\n\n\n\n\n i am from database.py create_table_attendness function")
    #     # print(f"month: {month}    session: {session} year: {year}")
       
    #     split_session= session[7:16] # we receve in session like (session_2003_2007) we just store like (2003_2007) for the help of index
    #     # print("here is your splite session: ",split_session)
    #     print(f"_{split_session}_Y_{year}_{month}")
    #      # Create April_2025 table (Attendance/Marks for 31 days) linked with session2025
    #     self.cursor.execute(f"""
    #         CREATE TABLE IF NOT EXISTS _{split_session}_Y_{year}_{month} (
    #             id INTEGER PRIMARY KEY AUTOINCREMENT,
    #             student_id INTEGER NOT NULL,
    #             day01 TEXT, day02 TEXT, day03 TEXT, day04 TEXT, day05 TEXT, day06 TEXT, day07 TEXT, day08 TEXT, 
    #             day09 TEXT, day10 TEXT, day11 TEXT, day12 TEXT, day13 TEXT, day14 TEXT, day15 TEXT, day16 TEXT, 
    #             day17 TEXT, day18 TEXT, day19 TEXT, day20 TEXT, day21 TEXT, day22 TEXT, day23 TEXT, day24 TEXT, 
    #             day25 TEXT, day26 TEXT, day27 TEXT, day28 TEXT, day29 TEXT, day30 TEXT, day31 TEXT,
    #             FOREIGN KEY (student_id) REFERENCES {session}(id) ON DELETE CASCADE
    #         )
    #     """)

    #     self.con.commit()
    #     print("Tables Created Successfully ✅")

    def create_table_attendness(self, month, session, year):
        # split_session= session[7:16]
        # print(f"_{split_session}_Y_{year}_{month}")
        self.cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS _{session}_{month}_{year}(
                student_rig_no TEXT,
                day01 TEXT, day02 TEXT, day03 TEXT, day04 TEXT, day05 TEXT,
                day06 TEXT, day07 TEXT, day08 TEXT, day09 TEXT, day10 TEXT,
                day11 TEXT, day12 TEXT, day13 TEXT, day14 TEXT, day15 TEXT,
                day16 TEXT, day17 TEXT, day18 TEXT, day19 TEXT, day20 TEXT,
                day21 TEXT, day22 TEXT, day23 TEXT, day24 TEXT, day25 TEXT,
                day26 TEXT, day27 TEXT, day28 TEXT, day29 TEXT, day30 TEXT,
                day31 TEXT,
                FOREIGN KEY (student_rig_no) REFERENCES {session}(rig_no) ON DELETE CASCADE

            )
        """)
        self.con.commit()




    # # Function to insert student data  an rendom database
    def insert_student_record_redom_tablse(self,database_name,rig_no, first_name, last_name, father_name, age, cnic, father_cnic, date_of_birth, 
                            mobile, province, postel_address, permanent_address, email,gender,
                            metric_bord, school_name, metric_total, metric_obt, metric_percentage, metric_grade,
                            fsc_bord, collage_name, fsc_total, fsc_obt, fsc_percentage, fsc_grade, gambar):
        self.cursor.execute(f"""
            INSERT INTO {database_name} (
                rig_no, first_name, last_name, father_name, age, cnic, father_cnic, date_of_birth, 
                mobile, province, postel_address, permanent_address, email,gender,
                metric_bord, school_name, metric_total, metric_obt, metric_percentage, metric_grade,
                fsc_bord, collage_name, fsc_total, fsc_obt, fsc_percentage, fsc_grade , gambar 
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (rig_no, first_name, last_name, father_name, age, cnic, father_cnic, date_of_birth,
            mobile, province, postel_address, permanent_address, email, gender,
            metric_bord, school_name, metric_total, metric_obt, metric_percentage, metric_grade,
            fsc_bord, collage_name, fsc_total, fsc_obt, fsc_percentage, fsc_grade, gambar))

        self.con.commit()
        print("Student record inserted successfully!")

        # except sqlite3.IntegrityError:
        #     print("Error: Duplicate CNIC not allowed!")
        #     return "Error: Duplicate CNIC not allowed!"

    def update_student_record(self,
                session,
                    rig_no,
                    first_name,
                    last_name,
                    father_name,
                    age,
                    cnic,
                    father_cnic,
                    date_of_birth,
                    mobile,
                    province,
                    postel_address,
                    permanent_address,
                    email,
                    gender,

                    metric_bord,
                    school_name,
                    metric_total,
                    metric_obt,
                    metric_percentage,
                    metric_grade,

                    fsc_bord,
                    collage_name,
                    fsc_total,
                    fsc_obt,
                    fsc_percentage,
                    fsc_grade,
                    gambar,
                    ):
        self.session = session
        print("it si session from database",self.session)
        

        # if session = "":
        #     print("yes")
        # else: 
        #     print("no")

        table_name = f"session{session}"
        sql = f"""
            UPDATE {table_name} SET
                first_name = ?,
                last_name = ?,
                father_name = ?,
                age = ?,
                cnic = ?,
                father_cnic = ?,
                date_of_birth = ?,
                mobile = ?,
                province = ?,
                postel_address = ?,
                permanent_address = ?,
                email = ?,
                gender = ?,

                metric_bord = ?,
                school_name = ?,
                metric_total = ?,
                metric_obt = ?,
                metric_percentage = ?,
                metric_grade = ?,

                fsc_bord = ?,
                collage_name = ?,
                fsc_total = ?,
                fsc_obt = ?,
                fsc_percentage = ?,
                fsc_grade = ?,
                gambar = ?

            WHERE rig_no = ?
        """

        values = (
            first_name, last_name, father_name, age, cnic, father_cnic, date_of_birth, mobile,
            province, postel_address, permanent_address, email, gender,
            metric_bord, school_name, metric_total, metric_obt, metric_percentage, metric_grade,
            fsc_bord, collage_name, fsc_total, fsc_obt, fsc_percentage, fsc_grade,
            gambar,  # image/blob
            rig_no  # WHERE condition
        )

        self.cursor.execute(sql, values)
        self.con.commit()



    def get_student_record_rendom_tablse(self,table_name):
        self.cursor.execute(f"SELECT * FROM {table_name}")
        self.rows = self.cursor.fetchall()
        self.con.commit()

        return self.rows

    def get_attendness_month_rendom_tablse(self,month):
        self.cursor.execute(f"SELECT * FROM _{month}")
        self.rows = self.cursor.fetchall()
        self.con.commit()

        return self.rows

    



    



   


    # get staff record  it will return all record from where you calling
    def get_staff_record(self):
        self.cursor.execute("SELECT * FROM staff")
        self.rows = self.cursor.fetchall()
        self.con.commit()

        return self.rows

        self.con.commit()
        print("Tables Created Successfully ✅")



    def insert_single_day_attendance(self, session, rig_no, date, attendance):
        # print("in database code")
        # print(session)
        # print(rig_no)
        # print(date)
        # print(attendance)
        # Check if the student_rig_no already exists
        self.cursor.execute(f"SELECT 1 FROM {session} WHERE student_rig_no = ?", (rig_no,))
        exists = self.cursor.fetchone()

        if exists:
            # Update only the dayXX column
            self.cursor.execute(
                f"UPDATE {session} SET day{date} = ? WHERE student_rig_no = ?",
                (attendance, rig_no)
            )
            print(f"Updated day{date} for rig_no {rig_no}.")
        else:
            # Insert a new row with student_rig_no and the specific day filled
            day_columns = ", ".join(["student_rig_no", f"day{date}"])
            placeholders = ", ".join(["?", "?"])
            self.cursor.execute(
                f"INSERT INTO {session} ({day_columns}) VALUES ({placeholders})",
                (rig_no, attendance)
            )
            print(f"Inserted new row with day{date} for rig_no {rig_no}.")
#
        self.con.commit()

    



    def read_student_with_attendance(self, student_id):
        """ Fetch student details along with their April_2025 attendance. """
        try:
            # Fetch student details
            student_query = """
                SELECT * FROM _2006_2002_Y_2025_July WHERE id = ?
            """
            self.cursor.execute(student_query, (student_id,))
            student_row = self.cursor.fetchall()

        except Exception as e:
            print(e)

        return student_row

    
    def get_attendness_record(self,session, month, year):
        # get staff record  it will return all record from where you calling
        try:
            self.cursor.execute(f"SELECT * FROM _{session}_{month}_2025")
            self.rows = self.cursor.fetchall()
            self.con.commit()
            return self.rows
        except Exception as e:
            return self.rows

        self.con.commit()
        print("Tables Created Successfully ✅")

    # delete staff user 
    def delete_staff(self, id ,table_name):
        """deleting the task"""
        self.cursor.execute(f"DELETE FROM {table_name} WHERE id = ?",(id,))
        self.con.commit()

    # delete student users
    def delete_student(self, rig_no ,table_name):
        """deleting the task"""
        self.cursor.execute(f"DELETE FROM {table_name} WHERE rig_no = ?",(rig_no,))
        self.con.commit()
    


    

# Run the database
# db = Database()
# db.update_student_record(
#     session="2004_2008",
#     rig_no="1234",
#     first_name="Zahir",
#     last_name="Afridi",
#     father_name="Rehmat Khan",
#     age=22,
#     cnic="12345-6789012-3",
#     father_cnic="54321-9876543-2",
#     date_of_birth="2002-05-10",
#     mobile="03001234567",
#     province="KPK",
#     postel_address="Hostel Street, Peshawar",
#     permanent_address="Village ABC, Khyber",
#     email="zahid.afridi@gmail.com",
#     gender="Male",

#     metric_bord="BISE Peshawar",
#     school_name="Iqra Model School",
#     metric_total=1100,
#     metric_obt=990,
#     metric_percentage=90.0,
#     metric_grade="A+",

#     fsc_bord="BISE Peshawar",
#     collage_name="Islamia College",
#     fsc_total=1100,
#     fsc_obt=1020,
#     fsc_percentage=92.7,
#     fsc_grade="A+",

#     gambar=None  # or use image bytes here
# )
# db.delete_student('123',"session2002_2006")
# db.insert_single_day_attendance("_2022","123","02","P")
# db.create_student_table("_26_25")
# db.create_table_attendness("april","222","2122")
# db.insert_single_day_attendance("session_23_25","123","01", "p")
# db.insert_single_day_attendance("_session2002_2006_April_2025","121","01","A")
# attendance_recod = db.get_attendness_record("session2004_2008","January",2025)
# print(attendance_recod)
# signup_user
# sqlite_sequence
# staff
# _2022
# session2002_2006
# _session2002_2006_April_2025  
# session2004_2008
# _session2004_2008_Augst_2025  
# _session2004_2008_January_2025
# tb = db.get_all_tables()
# for i in tb:
#     i = i[0]
#     print(i)

# db.create_student_table("2030")
# db.create_table_attendness("des", "session2030")
# db.create_tables_links()

# db = Database()
# db.create_tables()

# ✅ Insert a student with attendance
# student_info = (
#     "R-1001", "Ali", "Khan", "Ahmed Khan", 18, "1234567890123", "9876543210987", "2005-04-10",
#     "03123456789", "KPK", "Peshawar", "Kohat", "ali@example.com", "Male",
#     "BISE Peshawar", "City School", 1100, 980, 89.1, "A",
#     "BISE Peshawar", "College ABC", 1100, 960, 87.3, "A+", None
# )

# april_attendance = ["P"] * 31  # Example: Present ("P") for all 31 days
# print(april_attendance)

# Insert into both tables
# db.insert_student_with_attendance(student_info, april_attendance)
# print(db.read_student_with_attendance(1))
# record = db.read_student_with_attendance(1)
# print(record)
# get = db.get_student_record_rendom_tablse("session1233_112")
# print(get)
# i = 1
# tab = db.get_all_tables()
# for t in tab:
#     print(f"{i}: {t}")
#     i=i+1
# all = db.get_staff_record()
# print(all)
# # Example Usage (Uncomment to Test)
# db.insert_metric_info("Punjab Board", "ABC School", 1100, 999, 43, "A1")

# # Example Usage (Uncomment to Test)
# db.insert_student_personal_info(
#     "RIG-001", "Ali", "Khan", "Ahmed Khan", 22, "12345-6789012-3", "54321-0987654-3", 
#     "2000-05-15", "03001234567", "Punjab", "Street 10, City A", "Village X, City B", 
#     "student@example.com", "Male"
# )
    
# db.update_password("1234")
# db.forget_password('javid','khan','akhtar','0333','21506','sabir','1234')
# db.create_signup_record('sabir','din','akhtar','9890','8879789','sabir','123')
# db.forget_password()