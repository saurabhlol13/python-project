#!C:\Python27\python.exe

import cgi,MySQLdb,datetime

print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
problemdesc=data.getvalue('problemdesc')
indepartment=data.getvalue('indepartment')
concerndepartment=data.getvalue('concerndepartment')
raisedate=datetime.datetime.today().strftime('%d-%m-%y')
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query="insert into ticket(problemdesc,indepartment,concerndepartment,raisedate,status)values('"+problemdesc+"','"+indepartment+"','"+concerndepartment+"','"+raisedate+"','Pending')"
cmd.execute(query)
con.commit()
con.close()
print"<script>alert('Your Ticket is generated');window.location.href='userhome.py'</script>"
