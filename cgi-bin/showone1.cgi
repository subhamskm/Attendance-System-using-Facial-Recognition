#!/usr/bin/python3

import cgi

print('''Content-type: text/html\n\n
        <html>
        <body>
	<form action="showone2.cgi" method="post">
	<p>Enter Roll:    </p>
	<input type="texbox" name="roll">
	<input type="submit" value="Search">
	</form>
	</body>
        </html>''')

