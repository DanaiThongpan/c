from django.shortcuts import render

from .models import DB

# Create your views here.
def home(req):
    input = req.POST.get('c')
    db = DB.objects.filter(name__icontains=input)
    return render(req, 'home.html',{'db':db})