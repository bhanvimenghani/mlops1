import smtplib
import urllib.request as urllib
sender_email = "menghanibhanvi@gmail.com"
rec_email = "menghanibhannvi@gmail.com"

message = """ The Model has been created glad ! """
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("menghanibhanvi@gmail.com", "jack3141")
print("Login Success!")
server.sendmail("bhanvi", "menghanibhanvi@gmail.com", message)
print(f"Email has been sent successfully to {rec_email}")
