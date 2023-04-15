from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
# def hello_view(request):            #you can take any variable instead of request but request is recomended
#     return HttpResponse("<h1>This is a response from Django application</h1>")
# def morning_view(request):
#     return HttpResponse("<h1>Hello! Good Morning</h1>")
# def evening_view(request):
#     return HttpResponse("<h1>Hello! Good Evening</h1>")

def template_view(request):
    dt=datetime.now()
    my_dict={'date':dt}
    return render(request,'appname/results.html',context=my_dict)
def date_time_view(request):
    date=datetime.now()
    h=int(date.strftime('%H'))
    if h<12:
        msg="Hello! Good Morning."
    elif h>=12 and h<=16:
        msg="hello! Good Afternoon"
    elif h>16 and h<18:
        msg="Hello! good Evening"
    elif h>18 and h<21:
        msg="Hello!Good Evening"
    else:
        msg="Good Night"
    my_dict={'date':date,'msg':msg}
    return render(request,'appname/results.html',context=my_dict)
