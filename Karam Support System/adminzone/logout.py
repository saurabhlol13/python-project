#!C:\Python27\python.exe

print "Content-Type:text/html\n\n"
print """
<html>
<head>
<title>Logout</title>
<script>
function logout()
{
window.history.forward();
window.setTimeout("window.location.href='../index.py';",1000);
}
</script>
</head>
<body bgcolor="cyan" onload="logout()">
</body>
</html>
"""