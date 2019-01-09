#!C:\Python27\python.exe
import cgi,MySQLdb
print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>Admin Zone</title>
<link href="../css/userstyle.css" rel="stylesheet" type="text/css"/>
<link href="../css/adminmenu.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form method="post">
	<div id="outer">
		<div id="menu">
			<ul>
				<li><a href="adminhome.py">Notification</a></li>
				<li><a href="userinfo.py">User Info</a></li>
				<li><a href="feedbackmgmt.py">Feedback Mgmt</a></li>
				<li><a href="enquirymgmt.py">Enquiry Mgmt</a></li>
				<li><a href="ticket.py">Ticket Mgmt</a></li>
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
		<div id="container">
		  <h2 style="color:navy; text-align:center; ">Enquiry Management</h2>
			<table style="width:100%; border-collapse:collapse; border:3px solid;" border="1">
				<tr>
					<th>ID</th>
					<th>Name</th>
					<th>Address</th>
					<th>Contact Number</th>
					<th>Email Address</th>
					<th>Enquiry Text</th>
					<th>Delete</th>

				</tr>"""
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
cmd.execute("select * from enquiry order by id")
res=cmd.fetchall()
for row in res:
	print "<tr><td>",row[0],"</td>"
	print "<td>",row[1],"</td>"
	print "<td>",row[2],"</td>"
	print "<td>",row[3],"</td>"
	print "<td>",row[4],"</td>"
	print "<td>",row[5],"</td>"
	print "<td><a href='deleteenquiry.py?id=",row[0],"'>Delete</a></td></tr>"
print """</table>
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
