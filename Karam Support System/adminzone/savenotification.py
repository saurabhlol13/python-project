#!C:\Python27\python.exe

import cgi,MySQLdb,datetime
print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
notificationtext=data.getvalue('notificationtext')
posteddate=datetime.datetime.today().strftime('%d-%m-%Y')
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query="insert into notification(notificationtext,posteddate) values('"+notificationtext+"','"+posteddate+"')"
cmd.execute(query)
con.commit()
con.close()
print "<script>alert('Notification is Saved');window.location.href='adminhome.py';</script>"