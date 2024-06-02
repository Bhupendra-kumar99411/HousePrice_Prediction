from django.shortcuts import render
from django.shortcuts import redirect,render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .import testmodel

# Create your views here.
def index(request):
    if request.method == "POST":
        bath= request.POST.get('bath')
        balcony = request.POST.get('balcony')
        total_sqft_int = request.POST.get('total_sqft_int')
        bhk = request.POST.get('bhk')
        price_per_sqft = request.POST.get('price_per_sqft')
        availability = request.POST.get('availability')
        area_type = request.POST.get('area_type')
        location = request.POST.get('location')
        aa = testmodel.ml_model(bath,balcony,total_sqft_int,bhk,price_per_sqft,area_type,availability,location)
        aa = round(aa*100)/100
        d = {'aa' : aa}
        return render(request, 'index.html', d)
    else:
        return render(request,'index.html')