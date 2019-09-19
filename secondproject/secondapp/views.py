from django.shortcuts import render
from .models import studentdetails


# Create your views here.
def indexpage(req):
    return render(req,'index.html')

def newpage(request):
    id = request.POST.get("idno1")
    FirstName = request.POST.get("First_Name")
    LastName = request.POST.get("Last_Name")
    Emailid = request.POST.get("Emailid")
    aref = studentdetails(id = id ,First_Name = FirstName,Last_Name=LastName,Emailid= Emailid)
    aref.save()
    return render(request,'index.html',{"message": "Registered!"})
