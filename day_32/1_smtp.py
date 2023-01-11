#Simple Mail Transfer Protocol (SMPP)
import smtplib
#  SMTP client session object that can be used to send mail
my_email="forpython959@gmail.com"
# aafno email
password="epsagwvcmvrdbzou"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # gmail ko lagi chai yoho
    # yahoo ko lagi smtp.mail.yahoo.com
    connection.starttls()
    #python-libtls is a Python library which provides a high-level interface for secure network
    #  communication using the latest versions of Transport Layer Security (TLS).
    connection.login(user=my_email,password=password)
    connection.sendmail(from_addr=my_email,to_addrs="secondpython@yahoo.com",msg="subject:Thist is subject.\n\n This is mail.")
