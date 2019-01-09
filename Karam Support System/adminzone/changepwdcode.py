#!C:\Python27\python.exe
import cgi,Cookie,os,MySQLdb
if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	try:
		uid=c['adminid'].value
	except KeyError:
		print"<h1>Cookie is expired or not set</h1>"
print"Content-Type:text/html\n\n"
data=cgi.FieldStorage()
oldpassword=data.getvalue('oldpassword')
newpassword=data.getvalue('newpassword')
confirmpassword=data.getvalue('confirmpassword')
userid=uid
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query1="update login set password='"+newpassword+"'where userid='"+userid+"' and password='"+oldpassword+"'"
cmd.execute(query1)
con.commit()
con.close()
print"<script>alert('Password Changed');window.location.href='changepassword.py';</script>"