#!/usr/bin/python3

import cgi
import mysql.connector as mysql

print('''Content-type: text/html\n\n
         <html>
         <head>
	 <title>::Main::</title>
         </head>
         <body>''')
form = cgi.FieldStorage()
userid = form.getvalue("userid")
passwd = form.getvalue("passwd")

conn=mysql.connect(user='root', password='1234', database='attendance', host='localhost')
sql_lang = conn.cursor()
sql_lang.execute("select * from admin where userid='"+str(userid)+"';")
data = sql_lang.fetchall()
conn.close()

if (len(data)>0) and (data[0][0] == userid) and (data[0][1] == passwd) :
   print('<p><a href="/recognize.html">Go to Attendance System</a><p><br />')
   print('<p><a href="/cgi-bin/showall.cgi">Show details of all students</a><p><br />')
   print('<p><a href="/cgi-bin/showone1.cgi">Show attendance record of a student</a></p><br />')
else :
   print('<p>Invalid UserID or Password</p><br />')
   print('<a href="/index.html">Click here to move to LogIn page.</a>')
print('''</body>
         </html>''')
