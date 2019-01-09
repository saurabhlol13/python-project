#!C:\Python27\python.exe
import MySQLdb
print"Content-Type:text/html\n\n"
print """
<html>
<head>
	<title>Karam Support System</title>
	<link href="css/generalstyle.css" rel="stylesheet" type="text/css"/>
	<link href="css/menu.css" rel="stylesheet" type="text/css"/>
	<script src="js/slider.js" type="text/javascript"></script>
</head>
<body onload="moveslider()">
	<form>
		<div id="wrapper">
			<div id="menu">	
				<ul>
				<li><a href="index.py">Home</a></li>
				<li><a href="aboutus.py">About Us</a></li>
				<li><a href="registration.py">Registration</a></li>
				<li><a href="login.py">Login</a></li>
				<li><a href="enquiry.py">Enquiry</a></li>
				</ul>
			</div>
			<div id="header">
				<div id="logo">
				   <img src="images/logo.jpeg" height='150px' width='150px' />
				</div>
				<div id="banner">
					<img src="images/banner.png" height="150px" width="850px" />
				</div>
			</div>
			<div id="slider">
				<img id="slide" height="250px" width="1000px"/>		
			</div>
			<div id="container">
				<div id="left">
					<marquee direction="up" behaviour="alternate" height="500">
				
				"""
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
cmd.execute("select* from notification order by id desc")
res=cmd.fetchall()
for row in res:
	print"<p><b>Notification</p>"
	print"<p>",row[1],"</p>"
	print"<p><b>Posted Date</b></p>"
	print"<p>",row[2],"</p>"
	print"<hr/>"
		
				
print"""  	     </marquee></div>
				<div id="main"></div>
			</div>
            <div id="footer">
            	<div id="lfooter">
				  Copyright &copy; to Karam Support System
				</div>
            	<div id="rfooter">
				 Developed By:Saurabh Kasaudhan
				</div>
				 
            </div>
		</div>
	</form>
</body>
</html>

"""