#!C:\Python27\python.exe
import cgi,MySQLdb
print"Content-Type:text/html\n\n"
id=cgi.FieldStorage().getvalue('id')
con=MySQLdb.connect("127.0.0.1","root","","kssdb",3306)
cmd=con.cursor()
cmd.execute("delete from enquiry where id='"+id+"'")
con.commit()
con.close()
print"<script>alert('Enquiry is Deleted');window.location.href='enquirymgmt.py';</script>"