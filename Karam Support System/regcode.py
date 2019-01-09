#!C:\Python27\python.exe
import cgi
import MySQLdb

print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
empid=data.getvalue('empid')
empname=data.getvalue('empname')
gender=data.getvalue('gender')
fathername=data.getvalue('fathername')
address1=data.getvalue('address1')
address2=data.getvalue('address2')
zipcode=data.getvalue('zipcode')
doj=data.getvalue('doj')
department=data.getvalue('department')
designation=data.getvalue('designation')
contactno=data.getvalue('contactno')
emailaddress=data.getvalue('email')
adharno=data.getvalue('adharno')
panno=data.getvalue('panno')
password=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query1="insert into empinfo values('"+empid+"','"+empname+"','"+gender+"','"+fathername+"','"+address1+"','"+address2+"','"+zipcode+"','"+doj+"','"+department+"','"+designation+"','"+contactno+"','"+emailaddress+"','"+adharno+"','"+panno+"','"+password+"','false')"
query2="insert into login values('"+empid+"','"+password+"','user')"
cmd.execute(query1)
cmd.execute(query2)
con.commit()
con.close()
print "<script>alert('Registration Successfully');window.location.href='index.py';</script>"


