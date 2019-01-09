#!C:\Python27\python.exe

import cgi
import MySQLdb
print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
userid=data.getvalue('userid')
password=data.getvalue('password')
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query="select usertype from login where userid='"+userid+"' and password='"+password+"'"
cmd.execute(query)
res=cmd.fetchone()
if res:
	if res[0]=='user':
		print "<script>window.location.href='userzone/userhome.py?userid="+userid+"';</script>"
	elif res[0]=='admin':
		print "<script>window.location.href='adminzone/adminhome.py?adminid="+userid+"';</script>"
else:
	print "<script>alert('Invalid User');window.location.href='login.py';</script>"