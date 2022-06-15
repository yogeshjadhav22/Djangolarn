from django.shortcuts import render

def feeDjango(request):
    return render(request,'fees/feesone.html',{'pay':300})

def feePython(request):
    payfee={'pay':200}
    return render(request,'fees/feestwo.html',payfee)
# Create your views here.
