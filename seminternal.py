#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb,itertools

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML SEM INTERNAL</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    
        .kl{
            margin-top: 30px;
        }
        .kk{
            background-image: linear-gradient(rgb(44, 44, 117),rgb(151, 151, 53),red);
            color: transparent;
            background-clip: text;
            text-align:center;
        }
        .jk{
        margin-left:30px;
        margin-bottom:30px;}
        .mm{
        display:flex;
        overflow-x:scroll;
        }
        button{
        display:block;
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
     <h1 class="kk">SEM-INTERNAL MARKSHEET</h1>
     <h3 class="jk">MACHINE LEAARNING</h3>
    <div class="container ">
    <form enctype = "multipart/form-data" method = "post"> 
    <div class="mm">
    <table class="table table-responsive table-hover table-striped table-bordered ">
        <tr>
            <th>ROLL NO</th>
            <th>NAME</th>
        </tr>""")
p = """select regno,name from register """
cur.execute(p)
hot = cur.fetchall()
regno=hot[0]
name=hot[1]

u="""select ml from intercal"""
cur.execute(u)
now=cur.fetchall()

o="""select mli from model"""
cur.execute(o)
wow=cur.fetchall()
for x in hot:
    print("""
    <tr>
     <td>%s</td>
     <td>%s</td>
    </tr>
    """%(x[0],x[1]))
print("""</table>
<table class="table table-responsive table-hover table-striped table-bordered ">
<tr>
<th>INTERNAL</th>
</tr>

""")
for y in now:
    print("""
    </tr>
        <td>%s</td>
        </tr>
        """ % (y[0]))
print("""    
        
    </table>
    
    <table class="table table-responsive table-hover table-striped table-bordered ">
<tr>
<th>MODEL</th>
<th>ATTENDANCE</th>
<th>ASS/SEMINOR</th>
</tr>

""")
for y in wow:
    print("""
    </tr>
        <td>%s</td>
        <td><input type="text" name="att" class="mani" required></td>
        <td><input type="text" name="sem" class="mani" required></td>
        </tr>
        """ % (y[0]))
print("""  
</table>
</div>
<div class="kl">
    <a href=""><button class="btn btn-primary btn-lg" name="upt">submit</button></a>
    """)
hi=cgi.FieldStorage()
sem=hi.getvalue("sem")
att=hi.getvalue("att")
sumbit=hi.getvalue("upt")
o="""select regno,name from seminnt """
cur.execute(o)
cow=cur.fetchall()
if sumbit != None:
    for (i,x,y,z,k,v) in itertools.zip_longest(hot,now,wow,sem,att,cow):
        a=list(i)
        b=list(x)
        for d in b:
            pass
        c=list(y)
        for e in c:
            pass
        iny=float(d)
        moe=float(e)
        sem=int(z)
        att=int(k)
        t=iny+moe+sem+att
        n=round(t)
        if v[0] != a[1]:
            tr="""INSERT INTO seminnt(name,regno,internal,model,sem,attendance, total) values ('%s','%s','%s','%s','%s','%s','%s')"""%\
               (a[0],a[1],d,e,z,k,n)
            cur.execute(tr)
            con.commit()
            print("""
            <script>
            alert("hi")
            </script>
            """)
        if v[0]==a[1]:
            ui = """update seminnt set internal='%s',model='%s',sem='%s',attendance='%s' where regno='%s'""" % (
             a[0])
            cur.execute(ui)
            con.commit()
            print("""<script>
                              alert("marks update successfully ");
                              </script>""")


print("""
</div>
</form>
</div>




    <script src="./js/jquery.min.js"></script>
    <script src="./js/bootstrap.min.js"></script>
    <script>
    document.addEventListener("DOMContentLoaded",function(){
        const inputs=document.querySelectorAll(".mani")
        inputs.forEach(input =>{
            input.addEventListener("input",function(){
                let values=input.value;
                if (/[^0-9]/.test(values)||(values && (Number(values) < 0 || Number(values) > 5))){
                    alert("Marks upto 5. Invailed characters are not allowed ")
                    input.value=""
                }
            })
        })
    })
    </script>
</body>
</html>


""")