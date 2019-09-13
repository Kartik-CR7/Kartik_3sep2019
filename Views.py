from django.shortcuts import render # Renders the request to the url or Other page Specified
from django.db.models import Avg#if we want to import aggregrate function from models table
from django.db import connection
import socket#Imports the Host Ip Name and Address of Local Request PC
from .models import Like# To import tables from models

# Create your views here.
def firstpage(req):
    return render(req,'firstpage.html')


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

