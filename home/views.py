#task1 12345
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from  home.models import profile
import os
from django.core.files.storage import FileSystemStorage
# Create your views here.
def loginn(request):
    if request.method=='POST':
        namee=request.POST['namey']
        pass1=request.POST['passwordd']
        userr=authenticate(username=namee,password=pass1)
        if userr is not None:
            myprof=profile.objects.filter(uname=namee).first()
            cont={'myprof':myprof}
            login(request,userr)
            return render(request,f"{myprof.work}.html",cont)
        else:
            return HttpResponse("WRONG CRENDITALS")
            #return render(request,'login.html') 
            # return redirect('fakd_login')            
    
    return render(request,'login.html')    

def signup(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        emaill=request.POST['email']
        namee=request.POST['name']
        uploaded_file = request.FILES['document']
        # print(uploaded_file)
        # savefile= FileSystemStorage() 
        # name = savefile.save( namee,uploaded_file)# this is the name of file
        # #know where to save the file
        # print(name)
        # d = os.getcwd() #current directory of the project
        # file_directory = d+'\files\\'+name
        
        pass1=request.POST['password']
        pass2=request.POST['cnfpassword']
        add=request.POST['add']
        d=request.POST.get('btnradio1','off')
        p=request.POST.get('btnradio2','off')
        if pass1!=pass2:
           return HttpResponse("PASSWORD AND CONFRIM PASSWORD DONOT MATCH")
        myuser=User.objects.create_user(namee,emaill,pass1)
        myuser.save()
        if d=="on":
            work="doctor"
            myprof=profile(fname=fname,lname=lname,email=emaill,uname=namee,password=pass1,img=uploaded_file,address=add,work=work)
        else:
            work1="patient"
            myprof=profile(fname=fname,lname=lname,email=emaill,uname=namee,password=pass1,img=uploaded_file,address=add,work=work1)   
        myprof.save()       
        return render(request,'login.html') 
        
    return render(request,'signup.html')

def logoutt(request):
    logout(request)
    return render(request,'login.html') 
   