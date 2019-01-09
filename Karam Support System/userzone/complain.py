#!C:\Python27\python.exe

print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>UserZone</title>
<link href="../css/userstyle.css" rel="stylesheet" type="text/css"/>
<link href="../css/usermenu.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form action="complaincode.py" method="post">
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
		<div id="container">
			<table style="margin:0 auto;width:50%;">
				<tr>
					<td style="color:navy;font-size:30px;text-align:center;" colspan="2"><u>Raise Complain</u></td>
				</tr>
				<tr>
					<td>Subject:</td>
					<td><textarea name="subject" ></textarea></td>
				</tr>
				<tr>
					<td>Write Complain:</td>
					<td><textarea name="complaintext" ></textarea></td>
				</tr>
				<tr>
					<td>&nbsp;</td>
					<td><input type="submit" value="Submit"></td>
				
			</table>
		</div>
		<div id="footer">
			<div id="lfooter">Copyright &copy; to Karam Support System</div>
			<div id="rfooter">Developed By:Saurabh Kasaudhan</div>
		</div>
		
	</div>
</form>
</body>
</html>
"""