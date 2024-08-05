#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb, os
import itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
o = """select regno,name from register"""
cur.execute(o)
hot = cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SEM MARKS</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    .ty{
   text-align:center;
   background-image:linear-gradient(blue,green);
   color:transparent;
   background-clip: text;
   }
    nav{
    width:100%;
    }
    .mm{
    overflow-x: scroll;
   }
       #menus{
    position: absolute;
    /* background-image: linear-gradient(to right,gray,white); */
    background-color: lightgray;
    margin-top: 0%;
   }
   .uli{
    position: absolute;
    background-color: aqua;
    text-align: center;
   }
   .uli>ul>li{
    list-style-type: none;
   }
   .ol>li>a{
    color:black;
    text-decoration: none;
   }
   .ol>li>a:hover{
    color: lightgoldenrodyellow;
   }
   .ol>li{
    padding: 10px;
    margin-left: 10px;
    font-weight: bold;
    font-size: 18px;
    list-style-type: none;
   }
  
    </style>
</head>

<body>
    <nav>
        <div>
            <a href="#"><i class="jj glyphicon glyphicon-menu-hamburger" data-toggle="collapse"
                data-target="#menus"></i></a>&nbsp;&nbsp;
            <a href=""><h2 class="brand">EASC</h2></a>
        </div>
    </nav>
    <div id="menus" class="collapse col-md-4 col-sm-6 col-xs-10">
            <div class="row">
                <div class="col-md-2 col-xs-3" style="padding-top: 5px;">
                    <img src="./media/0ff34f3d1e08b2495e995ab7e6cfaeb7.jpg" alt="userprofile" class="img-circle" width="50px"
                        height="50px" name="pics">
                </div>
                <div class="col-md-8 col-xs-6">
                    <h3 name="uname">Username</h3>
                </div>
            </div>
            <ul class="ol">
                <li><a href="">INTERNAL 1</a></li>
                <li><a href="">INTERNAL 2 </a></li>
                <li><a href="">INTERNAL 3 </a></li>
                <li><a href="">INTERNAL CONVERT</a></li>
                <li><a href="./model.html">MODEL</a></li>
               
                <li class="dropdown"><a  class="dropdown-toggle" data-toggle="dropdown" href="">SEM-INTERNAL <span class="caret"></span></a>
                <ul class="dropdown-menu">
                    <li><a href="">MACHINE LEARNING</a></li>
                    <li><a href="">ADVANCED JAVA </a></li>
                    <li><a href="">WEB TECHNOLOGY</a></li>
                </ul></li>
                <li><a href="">PRACTICAL</a></li>
                <li class="dropdown"><a  class="dropdown-toggle" data-toggle="dropdown" href="">SEM-MARK <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="">MACHINE LEARNING</a></li>
                        <li><a href="">ADVANCED JAVA </a></li>
                        <li><a href="">WEB TECHNOLOGY</a></li>
                    </ul></li>
                
            </ul>
        </div>
    <div class="hg">
    <h1 class="ty">SEM MARKSHEET</h1>
    </div>

    <div class="container">
      <form enctype = "multipart/form-data" method = "post">   
<div class="mm">
    <table class="table table-hover table-striped table-bordered">
         <tr>
            <th colspan="2"></th>
            <th colspan="3">INTERNAL</th>
            <th colspan="3">EXTERNAL</th>
            
        </tr>
             
        <tr>
            <th>ROLL NO</th>
            <th>NAME</th>
            <th> MACHINE LEARNING</th>
            <th>WEB TECH</th>
            <th>JAVA ADVANCE</th>
            <th> MACHINE LEARNING</th>
            <th>WEB TECH</th>
            <th>JAVA ADVANCE</th>
        </tr>
        """)
p = """select regno,name from register"""
cur.execute(p)
hot = cur.fetchall()
y="""select total from webinter"""
cur.execute(y)
now=cur.fetchall()
c="""select total from javainter"""
cur.execute(c)
wow=cur.fetchall()
d="""select total from seminnt"""
cur.execute(d)
cow=cur.fetchall()

for (i,k,x,y) in itertools.zip_longest(hot,cow,now,wow):
    c=list(k)
    for h in c:
        pass
    d = list(x)
    for f in d:
        pass
    g = list(y)
    for r in g:
        pass
    print("""
        <tr>
           <td>%s</td>
           <td>%s</td>
           <td>%s</td>
           <td>%s</td>
           <td>%s</td>
           <td><input type="text" name="ml" class="mani" required ></td>
           <td><input type="text" name="wb" class="mani" required ></td>
           <td><input type="text" name="java" class="mani" required  ></td>
        </tr>""" % (i[0], i[1],h,f,r))
print("""
    </table>
    </div>
    <a href=""><button class="btn btn-success btn-lg" name="upt">submit</button></a>
""")
pr = cgi.FieldStorage()

ml = pr.getvalue("ml")
wb = pr.getvalue("wb")
java = pr.getvalue("java")
submit = pr.getvalue("upt")

if submit != None:
    for (i,k,h,g,x,y,z) in itertools.zip_longest(hot,cow,now,wow, ml, wb, java):
        c = list(k)
        for u in c:
            pass
        f=list(h)
        for j in f:
            pass
        w=list(g)
        for s in w:
            pass
        b=int(x)
        mls=u+b
        kj = int(y)
        wds=j+kj
        gk=int(z)
        javas=s+gk
        jl = """insert into semmark (regno,name,mli,wdi,javai,eml,ewd,ejava,ml,wd,java) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s') """%(i[0],i[1],u,j,s,x,y,z,mls,wds,javas)
        cur.execute(jl)
        con.commit()
        print("""<script>
              alert("marks insert successfully ");
              </script>""")


print("""
</form>
</div>
  <script>
      document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".mani")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (/[^0-9]/.test(values)||(values && (Number(values) < 0 || Number(values) > 75))){
                    alert("Marks upto 75. Invailed characters are not allowed ")
                    input.value=""
                }else{
                     console.log(inputValue)
                   }
            })
        })
    })


</script>

    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
</body>
</html>""")