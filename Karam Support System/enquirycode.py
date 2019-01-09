#!C:\Python27\python.exe
import cgi
import MySQLdb
print "Content-Type:text/html\n\n"
data=cgi.FieldStorage()
name=data.getvalue('name')
address=data.getvalue('address')
contactno=data.getvalue('contactno')
emailaddress=data.getvalue('emailaddress')
enquirytext=data.getvalue('enquirytext')

con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
query="insert into enquiry(name,address,contactno,emailaddress,enquirytext) values('"+name+"','"+address+"','"+contactno+"','"+emailaddress+"','"+enquirytext+"')"
cmd.execute(query)
con.commit()
con.close()
print"<script>alert('Your Enquiry is Submitted');window.location.href='index.py'</script>"