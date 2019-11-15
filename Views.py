from django.shortcuts import render # Renders the request to the url or Other page Specified
from django.db.models import Avg#if we want to import aggregrate function from models table
from django.db import connection
import socket#Imports the Host Ip Name and Address of Local Request PC
from .models import Like # To import tables from models
from .models import BT_Contact
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.conf import settings
# Create your views here.
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
def firstpage(req):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    cur = connection.cursor()
    cur.execute("select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then (select count(distinct sess_response) from MilieWebapp_like) when (count(1) over(partition by sess_response))% 2 = 0 then (select count(distinct sess_response) from MilieWebapp_like)-1 else 0 end as Result from MilieWebapp_like where sess_response ='" + host_ip + "'")
    Rec1 = cur.fetchone()[0]
    # if Rec1 is None :
    #     Rec1 = 0
    # else :
    #     Rec1 = cur.fetchone()
    # cur1 = connection.cursor()
    # cur1.execute("select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then 'Y' else 'N' end as Result from MilieWebapp_like where sess_response ='" + host_ip + "'")
    # FLag_is_liked = cur1.fetchone()[0]
    return render(req,'MilieWebapp/firstpage.html',{"message": Rec1})
# ,{"flag": FLag_is_liked}


def like_request(request):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    id = request.POST.get("idno")#Everytime entry primary key to a database wih sequnece incremental by 1
    aref = Like(id = id,sess_response = host_ip)#posting values to database
    aref.save()# Saving  values to database
    #We can use Raw Query but its better to use cursor query by importing connections
    cur = connection.cursor()
    cur.execute("select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then (select count(distinct sess_response) from MilieWebapp_like) when (count(1) over(partition by sess_response))% 2 = 0 then (select count(distinct sess_response) from MilieWebapp_like)-1 else 0 end as Result from MilieWebapp_like where sess_response ='"+ host_ip + "'")
    # cur.execute("select distinct case when (count(1) over(partition by sess_response))%2<> 0 then (select count(distinct sess_response) from MilieWebapp_like) else (select count(distinct sess_response) from MilieWebapp_like)- 1 end from MilieWebapp_like  where sess_response ="+str(host_ip))
    Rec = cur.fetchone()[0]#For First location of RawQueryset
    # Rec = Like.objects.all().count()--- just to count all values of table like select count(*) from table
    print (Rec)
    # cur1 = connection.cursor()
    # cur1.execute("select distinct case when (count(1) over(partition by sess_response))% 2 <> 0 then 'Y' else 'N' end as Result from MilieWebapp_like where sess_response ='" + host_ip + "'")
    # FLag_is_liked = cur1.fetchone()[0]
    return JsonResponse({"message": Rec})
    # , {"Flag": FLag_is_liked}
    #return jsonify({"message": Rec})
    # return render(request,'firstpage.html',{"message": Rec})


def ContactUsPage(request):
    return render(request, 'ContactU.html')


def ContactUsSubmit(request):
    Contact_id = request.POST.get("idno")
    FirstName = request.POST.get("First_Name")
    LastName = request.POST.get("Last_Name")
    Emailid = request.POST.get("Emailid")
    Message = request.POST.get("Message")
    aref = BT_Contact(Contact_id=Contact_id, First_Name=FirstName, Last_Name=LastName, Emailid=Emailid, Message=Message)
    aref.save()
    to = Emailid
    # try:
    # validate_email(Emailid)
    # return (request, 'ContactU.html', {"Alert": "Email Is Correct"})
    email = EmailMessage((FirstName+' '+LastName+'- Email_ID:'+ Emailid),Message,'DONOTREPLY <sharmakartik717@gmail.com>',[to])
    email.send()
    return render(request, 'ContactU.html', {"message": "Thanks for your valuable feedback/Interest!"})
    # send_mail(FirstName, Message, Emailid, ['sharmakartik717@gmail.com'])
