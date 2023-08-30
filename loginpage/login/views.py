from django.shortcuts import render
import mysql.connector as sql

mail=''
pwd=''

# Create your views here.
def loginaction(request):
    global gender,mail,pwd
    
    if request.method == "POST":
        m = sql.connect(host="localhost",user="root",password="123",database="project")
        cursor=m.cursor()
        d = request.POST    
        for key,value in d.items():
            if key=="email":
                mail=value
                
            if key=="password":
                pwd=value
                
        c = "select from users where email='{}'and password='{}'".format(mail,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,'welcome.html')
        
    return render(request,'login.html')