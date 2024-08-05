#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
print("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/login.css">
    <style>
    .log-btn {
    width: 80%;
    margin-left: 30px;
    margin-top: 10px;
    padding-top: 10px;
    padding-bottom: 10px;
    border-radius: 10px;
    border: none;
    background-image: linear-gradient(to right, skyblue, blueviolet, rgb(214, 122, 223));
    font-size: 16px;
    color: white;
}
</style>
</head>

<body>
    <div class="container">
        <form enctype="multipart/form-data" method="post">
            <h2 class="heado">LOG IN</h2>
            <div class="form-group"><label for="username">Username / Email</label>
            <input type="text" placeholder="Username / Email" class="form-control" id="username" name="uname">
                <small class="form-muted">Username must be Capsletter</small>
            
        </div>
        <div class="form-group">
            <label for="password" >Password</label>
            <input type="password" placeholder="Password" class="form-control" id="password" name="pwd">
                <small class="form-muted">Password must be yyyy-mm-dd</small>
        </div>
        <div class="text-muted">
           <p class="mk"><a href="" class="forget">Forgot Password?</a> or <a href="./signin.py" class="creates">Create Account</a> </p> 
        </div>
        <button class="log-btn" id="ko" type="submit" name="upt">Login</button>
       
        </form>
    </div>
    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    <script>
    document.getElementById("ko").addEventListener("click",function(event){
    event.preventDefault()});
    </script>
</body>

</html>""")

p=cgi.FieldStorage()
name=p.getvalue("uname")
pwd=p.getvalue("pwd")
submit=p.getvalue("upt")
if submit != None:
    o="""select id,ugmark from register where (name='%s' and dob='%s') or (email='%s' and dob='%s') or (name='%s' and password='%s') or (email='%s' and password='%s')"""% (name,pwd,name,pwd,name,pwd,name,pwd)
    cur.execute(o)
    hot=cur.fetchone()
    print("""<script>
       alert("hi");
       location.href="demo.py?poiuytrewq=%s&asdfghjkl=%s"
       </script>"""%(hot[0],hot[1]))


