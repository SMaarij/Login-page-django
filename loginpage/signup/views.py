from django.shortcuts import render
import mysql.connector as sql

first_name=''
last_name=''
gender=''
mail=''
pwd=''

# Create your views here.
def signaction(request):
    global first_name,last_name,gender,mail,pwd
    
    if request.method == "POST":
        m = sql.connect(host="localhost",user="root",password="123",database="project")
        cursor=m.cursor()
        d = request.POST    
        for key,value in d.items():
            if key=="first_name":
                first_name=value
                
            elif key=="last_name":
                last_name=value
                
            elif key=="gender":
                gender=value
                
            if key=="email":
                mail=value
                
            if key=="password":
                pwd=value
                
        cursor.execute("SELECT * FROM users WHERE email = %s", (mail,))
        existing_user = cursor.fetchone()

        if existing_user:
            # Email already exists, handle the error (e.g., display an error message)
            error_message = "Email address already exists."
            return render(request, 'signup.html', {'error_message': error_message})  
        
                
        c = "insert into users Values('{}','{}','{}','{}','{}')".format(first_name,last_name,gender,mail,pwd)
        cursor.execute(c)
        m.commit()
        
    return render(request,'signup.html')