import smtplib
import urllib.request as urllib
sender_email = "email@gmail.com"
rec_email = "emai@gmail.com"

message = """ The Model has been created glad ! """
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("email@gmail.com", "password")
print("Login Success!")
server.sendmail("bhanvi", "email@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")
