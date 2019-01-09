#!C:\Python27\python.exe

import cgi,Cookie,os,MySQLdb,datetime
if 'HTTP_COOKIE' in os.environ:
	cookie_string=os.environ.get('HTTP_COOKIE')
	c=Cookie.SimpleCookie()
	c.load(cookie_string)
	try:
		uid=c['userid'].value
	except KeyError:
		print"<h1>Cookie is expired or not set</h1>"

print c['userid']
print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
feedbacktext=data.getvalue('feedbacktext')
userid=uid
feedbackdt=datetime.datetime.today().strftime('%d-%m-%y')
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query="select empname from empinfo where empid='"+userid+"'"
cmd.execute(query)
name=''

res=cmd.fetchone()
if res:
	name=res[0]

query="insert into feedback(name,feedbacktext,feedbackdt)values('"+name+"','"+feedbacktext+"','"+feedbackdt+"')"
cmd.execute(query)
con.commit()
con.close()
print"<script>alert('Your Feedback is submitted');window.location.href='userhome.py'</script>"