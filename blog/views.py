from django.shortcuts import render

# Create your views here.

def frontpage(request):
    return render(request, "blog/frontpage.html")
    
