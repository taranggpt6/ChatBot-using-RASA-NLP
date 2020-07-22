import email
from email.message import EmailMessage
import smtplib
import json

class SendEmail:

    def send_Email(self,email,budget,less_3,t3_s7,more_7):
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.login('something@gmail.com','<Passoword>')
        me = 'something@gmail.com'
        msg = EmailMessage()
        msg['Subject'] = 'Top Rated Restaurants in your area'
        msg['From'] = 'testprojectdummy@gmail.com'
        msg['To'] = email
        if(budget=='Lesser than Rs.300'):
            msg.set_content("Hi there!, Here is the list of Top Restaurant in your area\n\n"+"\n".join(less_3[:10]))
            server.send_message(msg)
            server.quit()
            return(True)
        elif(budget=='Rs. 300 to 700'):
            msg.set_content("Hi there!, Here is the list of Top Restaurant in your area\n\n"+"\n".join(t3_s7[:10]))
            server.send_message(msg)
            server.quit()
            return(True)
        elif(budget=='More than Rs. 700'):
            msg.set_content("Hi there!, Here is the list of Top Restaurant in your area\n\n"+"\n".join(more_7[:10]))
            server.send_message(msg)
            server.quit()
            return(True)
