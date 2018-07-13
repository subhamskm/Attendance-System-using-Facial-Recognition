#!/usr/bin/python3

import cgi
import requests
import json
import mysql.connector as hi
import base64

print("Content-type: text/html")
print("")
page_data=cgi.FieldStorage()
image=page_data.getvalue('mydata')
emailof = page_data.getvalue('email')
nameof = page_data.getvalue('name')
phoneof = page_data.getvalue('phone')
#img_data = base64.b64decode(str(image))
print('<img src="data:image/png;base64, '+str(image)+'" alt="Red dot" /> <br />')
#with open("/home/subhham/Desktop/imageToSave.png", "wb") as fh:
    #fh.write(base64.b64decode(str(image)))

#put your keys in the header
headers = {
    "app_id" : "",
    "app_key" : ""
}

conn = hi.connect(user='root',password='1234',database='attendance',host='localhost')
sql_lang = conn.cursor()
sql_lang.execute("select roll from record order by roll desc limit 1;")
roll = int(sql_lang.fetchall()[0][0])+1

#data to be sent to API for recognizing
payload = '{"image":" '+str(image)+' ", "gallery_name":"Attendance", "subject_id":" '+str(roll)+' "}'

#URL of the API
url = "https://api.kairos.com/enroll"

#make request
r = requests.post(url, data = payload, headers = headers)

#updating new student in database

sql_lang.execute("insert into record(name,email,phone) values('"+nameof+"','"+emailof+"','"+phoneof+"');")
conn.commit()
conn.close()

print (r.content.decode('utf-8'))
