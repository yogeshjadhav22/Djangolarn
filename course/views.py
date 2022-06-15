from django.shortcuts import render
from datetime import datetime

def courseDjango(request):
    cname="Django"
    stu = {'std1':{'name':'yogesh','roll':102},
            'std2':{'name':'sonam','roll':102},
            'std3':{'name':'raj','roll':103},
            'std4':{'name':'anu','roll':104},
    }
    student ={'student':stu}
    list1 = ['yogesh','shelke','vishal','suraj','rushi']
    return render(request,"course/courseone.html",student)

def coursePython(request):
    cname="python"
    d =  datetime.now()
    details = {'cname':cname,'dt':d}

    return render(request,"course/coursetwo.html",details)
# Create your views here.
