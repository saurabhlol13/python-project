#!C:\Python27\python.exe

print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>Admin Zone</title>
<link href="../css/userstyle.css" rel="stylesheet" type="text/css"/>
<link href="../css/adminmenu.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form action="savenotification.py" method="post">
	<div id="outer">
		<div id="menu">
			<ul>
				<li><a href="adminhome.py">Notification</a></li>
				<li><a href="userinfo.py">User Info</a></li>
				<li><a href="feedbackmgmt.py">Feedback Mgmt</a></li>
				<li><a href="enquirymgmt.py">Enquiry Mgmt</a></li>
				<li><a href="complainmgmt.py">Complain Mgmt</a></li>
				<li><a href="changepassword.py">Change Pwd</a></li>
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
