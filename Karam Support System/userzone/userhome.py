#!C:\Python27\python.exe

import cgi
import Cookie
import os
c=Cookie.SimpleCookie()
c['userid']=cgi.FieldStorage().getvalue('userid')
c['userid']['expires']=3*60*60
print c['userid']
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>UserZone</title>
<link href="../css/userstyle.css" rel="stylesheet" type="text/css"/>
<link href="../css/usermenu.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form>
	<div id="outer">
		<div id="menu">
			<ul>
				<li><a href="userhome.py">Home</a></li>
				<li><a href="complain.py">Complain</a></li>
				<li><a href="feedback.py">Feedback</a></li>
				<li><a href="ticket.py">Ticket</a></li>
				<li><a href="changepwd.py">Change Password</a></li>
				<li><a href="logout.py">Logout</a></li>
			</ul>
		</div>
		<div id="header">
			<div id="logo">
			 <img src="../images/logo.jpeg" width="150px" height="150px" />
			</div>
			<div id="banner">
				Karam Support System
			</div>	
		</div>
		<div id="container"></div>
		<div id="footer">
			<div id="lfooter">Copyright &copy; to Karam Support System</div>
			<div id="rfooter">Developed By:Saurabh Kasaudhan</div>
		</div>
		
	</div>
</form>
</body>
</html>
"""
