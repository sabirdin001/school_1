import sqlite3

class Database():
    def __init__(self):
        # Connect to the database
        self.con = sqlite3.connect('student.db', check_same_thread=False)
        self.con.execute("PRAGMA foreign_keys = ON")  # Enable foreign key constraints
        self.cursor = self.con.cursor()

        # Create tables
        self.create_student_personal_table()
        self.create_table_attendness()

    def get_all_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        tables = self.cursor.fetchall()
        return tables

    def create_student_personal_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS session2022_2026(
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
                fsc_grade TEXT
            )
        """)
        self.con.commit()

    def create_table_attendness(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS april(
                day01 TEXT, day02 TEXT, day03 TEXT, day04 TEXT, day05 TEXT,
                day06 TEXT, day07 TEXT, day08 TEXT, day09 TEXT, day10 TEXT,
                day11 TEXT, day12 TEXT, day13 TEXT, day14 TEXT, day15 TEXT,
                day16 TEXT, day17 TEXT, day18 TEXT, day19 TEXT, day20 TEXT,
                day21 TEXT, day22 TEXT, day23 TEXT, day24 TEXT, day25 TEXT,
                day26 TEXT, day27 TEXT, day28 TEXT, day29 TEXT, day30 TEXT,
                day31 TEXT,student_rig_no TEXT,
                FOREIGN KEY (student_rig_no) REFERENCES session2022_2026(rig_no) ON DELETE CASCADE
            )
        """)
        self.con.commit()


    
    def insert_student_data(self, student_data):
        """Insert student data into the session2022_2026 table."""
        self.cursor.execute("""
            INSERT INTO session2022_2026 (rig_no, first_name, last_name, father_name, age, cnic, father_cnic, 
                                        date_of_birth, mobile, province, postel_address, permanent_address, 
                                        email, gender, metric_bord, school_name, metric_total, metric_obt, 
                                        metric_percentage, metric_grade, fsc_bord, collage_name, fsc_total, 
                                        fsc_obt, fsc_percentage, fsc_grade)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, student_data)
        
        # Commit the changes to the database
        self.con.commit()
        print("Student data inserted successfully.")


        print("Data inserted successfully.")

    


    def insert_single_day_attendance(self):
        try:
            self.cursor.execute("""
                INSERT INTO april (student_rig_no, day01)
                VALUES (?, ?)
            """, ('7889', 'P'))  # '1001' must match a rig_no in session2022_2026

            self.con.commit()
            print("Only day01 inserted successfully.")
        except sqlite3.IntegrityError as e:
            print(f"Error: {e}")




# Run the database operations
db = Database()

student_data = (
    '78389', 'fohn', 'Dod', 'Mikd', 81, '14345-1233467-1', '12235-9876543-1', '2334-05-05', 
    '03033234567', 'Punjab', 'Street 123', 'Street 456', 'john.doe@example.com', 'Male', 
    'ABC Board', 'ABC School', 1000, 900, 90.0, 'A', 'XYZ Board', 'XYZ College', 1100, 1000, 90.9, 'A'
)
# Sample attendance data for April (31 days, e.g., 'p' for present, 'a' for absent)


# Insert data into both tables
# db.insert_student_data(student_data)
db.insert_single_day_attendance()
