#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb,os

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>signin</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
     <link rel="stylesheet" href="./style/signin.css">
</head>
<body>
    <div class="container">
        <form enctype="multipart/form-data" method="post">
            <h2 class="reg-fo">REGISTER FORM</h2>
            <div class="form-group">
                <label for="Name">Name</label>
                <input type="text" class="form-control k" placeholder="Name" id="Name" name="name" required>
            </div>
            <div class="form-group">
                <label for="regno">Register Number</label>
                <input type="text" class="form-control k" placeholder="Reg num" id="regno" name="reg" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" class="form-control" placeholder="example@gmail.com" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="dob">DOB</label>
                <input type="date" class="form-control" id="dob" name="dob" required >
            </div>
            <label for="">Gender</label>
               <div class="radio">
                <label><input type="radio" name="optradio" id="male" value="Male" checked >Male</label>
            </div>
            <div class="radio">
                <label><input type="radio" name="optradio" id="female" value="Female">Female</label>
            </div>
            <div class="form-group">
                <label for="bd">Blood Group</label>
                <input type="text" class="form-control k" placeholder="A+, B+, AB+..." id="bd" name="bd" required>
            </div>
            <div class="form-group">
                <label for="aadhar">Aadhar</label>
                <input type="text" class="form-control" placeholder="1234567890" id="aadhar" name="aadhar" required>
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="text" class="form-control" placeholder="0987654321" id="phone" name="phn" required>
            </div>
            <div class="form-group">
                <label for="address">Address</label>
                <input type="text" class="form-control k" placeholder="xxx yyy zzz" id="address" name="address" required>
            </div>
            <div class="form-group">
                <label for="pincode">Pincode</label>
                <input type="text" class="form-control" placeholder="Pincode" id="pincode" name="pincode" required>
            </div>
            <div class="form-group">
                <label for="ug">UG Percentage</label>
                <input type="text" class="form-control" placeholder="100%" id="ug" name="per">
                <small class="form-muted">optional</small>
            </div>
            <div class="form-group">
                <label for="ug">Profile </label>
                <input type="file" class="form-control" id="ug" name="mk">
                <small class="form-muted">optional</small>
            </div>
            <button class="log-btn" name="upt"  type="submit">Submit</button>
           
        </form>
    </div>
    

    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
""")

p=cgi.FieldStorage()
name=p.getvalue("name")
reg=p.getvalue("reg")
email=p.getvalue("email")
dob=p.getvalue("dob")
gender=p.getvalue("optradio")
bloodgrp=p.getvalue("bd")
aadhar =p.getvalue("aadhar")
phone=p.getvalue("phn")
address=p.getvalue("address")
pincode=p.getvalue("pincode")
ugper=p.getvalue("per")
submit=p.getvalue("upt")


if submit != None:
    name1 = name.upper()
    regno = reg.upper()
    bld = bloodgrp.upper()
    add = address.upper()
    ugmark = p['mk']
    if ugmark.filename:
        hj = os.path.basename(ugmark.filename)
        open("media/" + hj, "wb").write(ugmark.file.read())
    o="""insert into register (name,regno,email,dob,gender,bloodgrp,aadhar,phone,address,pincode,ugper,ugmark) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """%(name1,regno,email,dob,gender,bld,aadhar,phone,add,pincode,ugper,hj)
    cur.execute(o)
    con.commit()
    print("""<script>
    alert("hi");
    </script>""")
