
from flet import *

from file_pages import Athintication
from flet import IconButton
from add_student_page import AddNewStudent
from class_mangment_page import ClassManagment
from home_file import HomePage
from staff_payroll import NewStaff
from signup_page import SignUp
from login_page import LogIn
from forget import Forget
from view_attendness import ViewAttendness
from password_reset_page import ResetPassword
from add_new_class import NewClass
from edit_student_page import EditStudent
from view_student import ViewStudent
from create_new_month import NewMonth
from developer_page import DeveloperPage
from developer_page import DeveloperPage
# from flet import adaptiv

class software:
    def __init__(self, page:Page):
        self.page = page
        self.athintication = Athintication(self.page)
        self.AddNewStudent = AddNewStudent(self.page)
        self.ClassManagment =ClassManagment(self.page)
        self.HomePage = HomePage(self.page)
        self.NewStaff = NewStaff(self.page)
        self.SignUp = SignUp(self.page)
        self.LogIn = LogIn(self.page)
        self.Forget = Forget(self.page)
        self.ViewAttendness =ViewAttendness(self.page)
        self.ResetPassword=ResetPassword(self.page)
        self.NewClass = NewClass(self.page)
        self.EditStudent = EditStudent(self.page)
        self.ViewStudent = ViewStudent(self.page)
        self.NewMonth = NewMonth(self.page)
        self.DeveloperPage = DeveloperPage(self.page)
     
    
    def route_change(self,route):
        
        # that is login page 
        if self.page.route == "/":
            self.page.views.clear()
            self.page.views.append(
                self.LogIn.log_in()
            )
            self.page.update()


        # it is for Signup page
        elif self.page.route == "/signup":
            self.page.views.clear()
            self.page.views.append(
                self.SignUp.Sign_up()
            )
            self.page.update()

        elif self.page.route == "/forget":
            self.page.views.clear()
            self.page.views.append(
                self.Forget.forget_password()
            )
            self.page.update()

        # it is for home page
        elif self.page.route == "/home_page":
            self.page.views.clear()
            self.page.views.append(
                self.HomePage.home_page()
            )
            self.page.update()

        elif self.page.route == "/add_new_student":
            self.page.views.clear()
            self.page.views.append(
                self.AddNewStudent.add_studen()
            )
            self.page.update()

        #Note  that is import form file page Athintication class for attendness page
        elif self.page.route == "/atendness_page":
            self.page.views.clear()
            self.page.views.append(
                self.athintication.Atendness_page()
            )
            self.page.update()

        elif self.page.route == "/managment":
        # if self.page.route == "/":
            
            self.page.views.clear()
            self.page.views.append(
                self.ClassManagment.managment()
            )
            self.page.update()

        elif self.page.route == "/new_staff":
            self.page.views.clear()
            self.page.views.append(
                self.NewStaff.add_new_staff()
            )
            self.page.update()

        elif self.page.route == "/view_attendness":
            self.page.views.clear()
            self.page.views.append(
                self.ViewAttendness.view_attendness()
            )
            self.page.update()

        elif self.page.route == "/reset_page":
            self.page.views.clear()
            self.page.views.append(
                self.ResetPassword.reset_password()
            )
            self.page.update()

         # that is login page 
        elif self.page.route == "/new_class":
            self.page.views.clear()
            self.page.views.append(
                self.NewClass.new_class()
            )
            self.page.update()
        # if self.page.route == "/":
        elif self.page.route == "/edit_student_page":
            pass

            # self.page.views.clear()
            # self.page.views.append(
            #     self.EditStudent.edit_student_page()
            # )
            # self.page.update()

        elif self.page.route == "/view_student":
            pass
            # self.page.views.clear()
            # self.page.views.append(
            #     self.ViewStudent.view_student()
            # )
            self.page.update()

        elif self.page.route == "/new_month":
            self.page.views.clear()
            self.page.views.append(
                self.NewMonth.new_month()
            )

        elif self.page.route == "/devleoper_page":
            self.page.views.clear()
            self.page.views.append(
                self.DeveloperPage.devleoper_page()
            )



        

    # HEre is a fucntion go to back page 
    def pop_view(self,e):
        self.page.views.pop()
        top_page = self.page.views[-1]
        self.page.go(self.page.route)
        # page.update()``

def main(page:Page):
    page.window_width = 1366
    page.window_height = 768
    page.padding=0
    # page.window_always_on_top = True
    page.scroll = "auto"
    page.title= "Student Managment System"
    # page.padding = 0

    soft = software(page=page)
    page.on_route_change = soft.route_change
    page.go(page.route)
    page.on_view_pop = soft.pop_view

if __name__ == '__main__':
    app(target=main,view=FLET_APP)
    
