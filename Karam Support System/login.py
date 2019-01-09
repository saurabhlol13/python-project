#!C:\Python27\python.exe

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
	<form action="logcode.py" method="post">
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
				<div id="left"></div>
				<div id="main">
					<div style="width:100%;height:800px;margin-top:50px">
				    <table align="center" cellpadding="5px">
						 <tr>
							<td colspan="2" style="font-size:30px; text-align:center; color:blue; ">Login Form</td>
						 </tr>
						 <tr>
							<td>User Id:</td>
							<td><input type="text" name="userid"/></td>
						</tr>
						<tr>
							<td>Password:</td>
							<td><input type="password" name="password"/></td>
						</tr>
						
						<tr>
							<td>&nbsp;</td>
							<td><input type="submit" value="Login"/></td>
						</tr>
					</table>
                   </div>
				</div>
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
				