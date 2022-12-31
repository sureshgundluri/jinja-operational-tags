from django.shortcuts import render

def operations(request):
    d={'a':123,'b':345,'c':6321}
    return render(request,'operations.html',context=d)