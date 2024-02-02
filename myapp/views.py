from django.shortcuts import render  
from django.shortcuts import redirect

 

from myapp.models import Employess
# Create your views here.
def index(request):
    emp = Employess.objects.all()
    context = {
        'emp': emp,
    }
    return render(request,'index.html', context)


def ADD(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        emp = Employess(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        emp.save()
        return redirect("index")
    return render( request,'index.html')

def EDIT(request ):
    emp = Employess.objects.all()
    context = {
        "emp": emp,
    }
    return render(request,'index.html', context)