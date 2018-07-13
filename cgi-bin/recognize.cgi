#!/usr/bin/python3

import cgi
import requests
import json
import mysql.connector as mysql
import datetime

print("""Content-type: text/html\n
	<!DOCTYPE html>
	<html>
	<body>""")
page_data=cgi.FieldStorage()
image=page_data.getvalue("param1")

#print('<img src="data:image/png;base64, '+image+'" alt="Red dot" /> <br />')


#put your keys in the header
headers = {
    "app_id" : "",
    "app_key" : ""
}

#data to be sent to API for recognizing
payload = '{"image":" '+str(image)+' ", "gallery_name":"Attendance"}'

#URL of the API
url = "https://api.kairos.com/recognize"

#make request
r = requests.post(url, data = payload, headers = headers)

#decode the JSON data received 
json_data = r.content.decode('utf-8')

#Dictionaries can also be seen as JSON strings. Thus we can use the json module to convert a string to dict as well.
data = json.loads(json_data)
#name = "Subham Kumar"
#print("<p>"+str(data)+"</p>")
roll = data["images"][0]["candidates"][0]["subject_id"]

now = datetime.datetime.now()
now = now.strftime("%Y-%m-%d %H:%M:%S")

conn = mysql.connect(user='root', password='1234', database='attendance', host='localhost')
sql_lang = conn.cursor()
sql_lang.execute("insert into attendance_record (DateTime,Roll) values('"+str(now)+"',"+str(roll)+");")
sql_lang.execute("update record set Present=Present+1 where Roll = "+str(roll)+";")
sql_lang.execute("select name from record where roll="+str(roll)+";")
name = sql_lang.fetchall()[0][0]
conn.commit()
conn.close()

print("<p>"+str(name)+"</p>")
print("""</body>
	 </html>""")



