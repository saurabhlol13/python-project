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
<form action="changepwdcode.py" method="post">
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
		   <div style="width:1000px; height:auto; min-height:800px;">
			<table cellpadding="10px" style="margin:0px auto;">
				<tr>	
					<td colspan="2"style="text-align:center;font-size:30px; color:navy;"><u>Change Password</u></td>
				</tr>
				<tr>
				 <td>Old Password:</td>
				 <td><input type="password" name="oldpassword" required /></td>
				</tr>
				<tr>
				 <td>New Password:</td>
				 <td><input type="password" name="newpassword" required /></td>
				</tr>
				<tr>
				 <td>Confirm Password:</td>
				 <td><input type="password" name="confirmpassword"required /></td>
				</tr>
				<tr>
					<td>&nbsp;</td>
					<td><input type="Submit" value="Change Password" /></td>
				</tr>
			</table>
		   </div>
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
