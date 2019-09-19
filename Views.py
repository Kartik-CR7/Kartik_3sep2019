from django.shortcuts import render # Renders the request to the url or Other page Specified
from django.db.models import Avg#if we want to import aggregrate function from models table
from django.db import connection
import socket#Imports the Host Ip Name and Address of Local Request PC
from .models import Like # To import tables from models
from .models import BT_Contact
from django.core.mail import send_mail
from django.core.mail import EmailMessage

# Create your views here.
def firstpage(req):
    cur = connection.cursor()
    cur.execute('''select count( distinct sess_response) as counts from Webapphomepage_like''')
    Rec1 = cur.fetchone()[0]
    return render(req,'firstpage.html',{"message": Rec1})


def like_request(request):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    id = request.POST.get("idno")#Everytime entry primary key to a database wih sequnece incremental by 1
    aref = Like(id = id,sess_response = host_ip)#posting values to database
    aref.save()# Saving  values to database
    #We can use Raw Query but its better to use cursor query by importing connections
    cur = connection.cursor()
    cur.execute('''select count( distinct sess_response) as counts from Webapphomepage_like''')
    Rec = cur.fetchone()[0]#For First location of RawQueryset
    # Rec = Like.objects.all().count()--- just to count all values of table like select count(*) from table
    return render(request,'firstpage.html',{"message": Rec})


def ContactUsPage(request):
    return render(request, 'ContactU.html')


def ContactUsSubmit(request):
    to = 'anshulkant02415@gmail.com'
    Contact_id = request.POST.get("idno")
    FirstName = request.POST.get("First_Name")
    LastName = request.POST.get("Last_Name")
    Emailid = request.POST.get("Emailid")
    Message = request.POST.get("Message")
    aref = BT_Contact(Contact_id=Contact_id, First_Name=FirstName, Last_Name=LastName, Emailid=Emailid, Message=Message)
    aref.save()
    email = EmailMessage((FirstName+'- Email_ID:'+Emailid),Message,Emailid,[to])
    email.send()
    return render(request, 'ContactU.html', {"message": "Thanks for your valuable feedback/Interest!"})
    # send_mail(FirstName, Message, Emailid, ['sharmakartik717@gmail.com'])
