#!C:/Users/ELCOT/AppData/Local/Programs/Python/Python311/python.exe
print("content-type:text/html \r\n\r\n")
import pymysql
import cgi, cgitb

cgitb.enable()
con = pymysql.connect(host="localhost", user="root", password="", database="std_mark")
cur = con.cursor()
p="""select rego,name,mli,wdi,javai from internal  """
cur.execute(p)
pri = cur.fetchall()
o="""select regno,name,mli,wdi,javai from internal2 """
cur.execute(o)
pr = cur.fetchall()

ug="""select regno,name,mli,wdi,javai from internal3 """
cur.execute(ug)
prl = cur.fetchall()
print("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal MARKS</title>
    <link rel="stylesheet" href="./css/bootstrap.min.css">
    <link rel="stylesheet" href="./style/internal.css">
    <style>
    th,td{
    text-align:center;}
    .mr{
    margin-left:0px;
    padding:0%;
    
    }
    .mr2{
    margin-left:0px;
    padding:0%;
    width:200px;
    }
     .mr3{
    margin-left:0px;
    padding:0%;
    width:200px;
    }
    .lk{
    width: 300px;}
    .dd{
    display:inline;
    margin-left:30px;
    }
    form{
    margin-top:30px;
    margin-left:30px;}
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
    <h1 class="ty">ALL INTERNAL MARKSHEET</h1>
    </div>
    <div class="mk">
      <form enctype = "multipart/form-data" method = "post">   


<div class="mr col-md-4 col-sm-4">
     <table class="table"  border="1px">
            <tr>
                <th colspan="2"></th>
           
                    <th colspan="3">internal 1</th>   
            </tr>
            <tr>
                <th>regno</th>
                <th style="width: 300px;">name</th>
                <th>ml</th>
                <th>wb</th>
                <th>java</th>
            </tr>
            """)
for i in pri:
    print("""
            <tr>
                <td>%s</td>
                <td class="lk">%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
            </tr>
        """%(i[0],i[1],i[2],i[3],i[4]))
print("""</table>
</div>
<div class="mr2 col-md-4 col-sm-4">

     <table  border="1px" class="table">
            <tr>   
             <th colspan="3">internal 2</th>   
            </tr>
            <tr> 
                <th>ml</th>
                <th>wb</th>
                <th>java</th>
            </tr>""")
for i in pr:
    print("""
                <tr>
                    
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
            """ % (i[2], i[3], i[4]))

print("""
</table>
</div>
<div class="mr3 col-md-4 col-sm-4">

     <table  border="1px" class="table">
            <tr>   
             <th colspan="3">internal 3</th>   
            </tr>
            <tr> 
                <th>ml</th>
                <th>wb</th>
                <th>java</th>
            </tr>""")
for i in prl:
    print("""
                <tr>
                    
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
            """ % (i[2], i[3], i[4]))
print("""
</table>
</div>
<div class="dd">
     <button name="btnh" class="btn btn-primary btn-lg">convert</button>
     </div>
     </form >
     </body>
     </html>""")
po=cgi.FieldStorage()
btn=po.getvalue("btnh")
if btn !=None:
    y="""INSERT into intercal(regno,name,ml,wb,java) SELECT internal.rego,internal.name,(greatest(internal.mli,internal2.mli)+greatest(least(internal.mli,internal2.mli),internal3.mli)) AS ml,(greatest(internal.wdi,internal2.wdi)+greatest(least(internal.wdi,internal2.wdi),internal3.wdi)) AS wb,(greatest(internal.javai,internal2.javai)+greatest(least(internal.javai,internal2.javai),internal3.javai)) AS java from  internal internal join internal2 internal2 on internal.rego=internal2.regno and internal.name=internal2.name JOIN internal3 internal3 on internal.rego=internal3.regno and internal.name=internal3.name"""
    cur.execute(y)
    con.commit()
    print("""<script>
                      alert("marks insert successfully ");
                      </script>""")
