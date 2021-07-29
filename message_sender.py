
import pywhatkit as pwt
import csv
from datetime import datetime


# Enter message in the terminal
msg = input("Enter your message here: ")

# Enter the name of the csv file
whatsapp_csv = input("Enter the csv filename: ")

members = []
with open(whatsapp_csv, encoding='UTF-8') as file:
    Rows = csv.reader(file,delimiter=",",lineterminator='\n')
    next(Rows,None)
    for r in Rows:
        members.append(r[0])

# Printing all the contact numbers which are in the csv file
print(members)

for ph in members:
    time = datetime.now()
    pwt.sendwhatmsg(f"+91-{ph}",msg, time.hour,time.minute+1, 15)
