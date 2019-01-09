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
	<form action="regcode.py" method="post">
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
							<td colspan="2" style="font-size:30px; text-align:center; color:blue; ">Registration Form</td>
						 </tr>
						 <tr>
							<td>Employee Id:</td>
							<td><input type="text" name="empid" required /></td>
						</tr>
						<tr>
							<td>Employee Name:</td>
							<td><input type="text" name="empname" required /></td>
						</tr>
						<tr>
							<td>Gender</td>
							<td><input type="radio" name="gender" value="male" required />Male
							    <input type="radio" name="gender" value="female" required />Female</td>
						</tr>
						<tr>
							<td>Father Name:</td>
							<td><input type="text" name="fathername"  required /></td>
						</tr>
						<tr>
							<td>Address1:</td>
							<td><textarea name="address1"  required></textarea></td>
						</tr>
						<tr>
							<td>Address2:</td>
							<td><textarea name="address2" ></textarea></td>
						</tr>
						<tr>
							<td>Zipcode:</td>
							<td><input type="number" name="zipcode" required /></td>
						</tr>
						<tr>
							<td>DOJ:</td>
							<td><input type="date" name="doj" required /></td>
						</tr>
						<tr>
							<td>Department:</td>
							<td>
								<select name="department"  required>
									<option>--Select Department---</option>
									<option>Production</option>
									<option>Management</option>
									<option>HR</option>
									<option>Marketing</option>
									<option>Sales</option>
								</select>
							</td>
						</tr>
						<tr>
							<td>Designation:</td>
							<td><input type="text" name="designation"  required /></td>
						</tr>
						<tr>
							<td>Contact Number:</td>
							<td><input type="text" name="contactno"  required /></td>
						</tr>
						<tr>
							<td>Email Address:</td>
							<td><input type="email" name="email"  required /></td>
						</tr>
						<tr>
							<td>Adhar Number:</td>
							<td><input type="text" name="adharno"  required /></td>
						</tr>
						<tr>
							<td>Pan Number:</td>
							<td><input type="text" name="panno"/></td>
						</tr>
						<tr>
							<td>Password:</td>
							<td><input type="password" name="password"  required /></td>
						</tr>
						
						<tr>
							<td>&nbsp;</td>
							<td><input type="submit" value="Register"/></td>
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
				