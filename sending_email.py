import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

class SendingEmail:
    def email(self, receiver_email, student_name, date_now, month, attend):
        self.present_or_obsent = ""

        if attend == "P" or attend =="p":
            self.present_or_obsent = 'present'
        else:
            
            self.present_or_obsent = 'Absent'
            # 'sabirdin777@gmail.com',"sabir", "88",'88',"A"
            
        # Email details"
        print("Email class callling.........")
        sender_email = "fullbakwas08@gmail.com"
        sender_password = "xpnh dict fyxj gkva"  # Use App Password if 2FA is enabled
        # receiver_email = "sabirdin777@gmail.com"
        subject = "GPGC Miran shah student Attendance"
        body = f"""
        Dear perents Alsalam o Allaikon!
        we are from GOVT POST GRADUAT COLLAGE,
        that email inform you you, your child {student_name} is {self.present_or_obsent}
        at the date {date_now} - {month} 

        """
        # print(body)

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the message body
        msg.attach(MIMEText(body, 'plain'))

        try:
            # Set up the Gmail server
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()  # Upgrade connection to secure TLS
            server.login(sender_email, sender_password)
            
            # Send the email
            server.send_message(msg)
            print("Email sent successfully!")

            # Close the server connection
            server.quit()

            

        except Exception as e:
            return f"Failed to send email: {e}"


ob = SendingEmail()
ob.email('sabirdin777@gmail.com',"sabir", "88",'88',"A")