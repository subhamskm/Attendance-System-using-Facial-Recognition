#!/usr/bin/python3

import cgi
import mysql.connector as mysql

print('''Content-type: text/html\n\n
         <html>
         <head>
<style>
table {
    width:100%;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 15px;
    text-align: left;
}
table#t01 tr:nth-child(even) {
    background-color: #eee;
}
table#t01 tr:nth-child(odd) {
   background-color: #fff;
}
table#t01 th {
    background-color: black;
    color: white;
}
</style>
</head>
         <body>''')
form = cgi.FieldStorage()
roll = form.getvalue('roll')
conn = mysql.connect(user='root', password='1234', database='attendance', host='localhost')
sql_lang = conn.cursor()
sql_lang.execute("select DateTime from attendance_record where roll="+roll+";")
data=sql_lang.fetchall()
conn.close()

print('''<table id='t01'>
         <tr>
         <th>Date and Time</th>
         </tr>''')
for i in data:
    print('<tr>')
    for j in i:
        print('<td>'+str(j)+'</td>')
    print('</tr>')
print('''</table>
         </html>''')
	
