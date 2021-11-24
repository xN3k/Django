from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'accounts/dashboard.html/')
def about(request):
    return HttpResponse('About Page')

def products(request):
    return HttpResponse('Product List')

