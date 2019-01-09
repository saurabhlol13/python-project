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
<form action="ticketcode.py" method="post">
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
					<td style="color:navy;font-size:30px;text-align:center;" colspan="2"><u>Generate Ticket</u></td>
				</tr>
				<tr>
					<td>Problem Description:</td>
					<td><textarea name="problemdesc" rows="15" cols="40" ></textarea></td>
				</tr>
				<tr>
					<td>In Department:</td>
					<td><input type="text" name="indepartment" /></td>
				</tr>
				<tr>
					<td>Concern Department:</td>
					<td><input type="text" name="concerndepartment" /></td>
				</tr>
				<tr>
					<td>&nbsp;</td>
					<td><input type="submit" value="Submit"></td>
			    </tr>
				
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
