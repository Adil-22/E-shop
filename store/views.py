from http.client import HTTPResponse
from django.shortcuts import render
from .models.product import Product
from .models.category import Category
# Create your views here.


def index(request):
    product=Product.objects.all()
    category=Category.objects.all()
    categoryID =request.GET.get('category')
    if categoryID:
        product=Product.objects.filter(category=categoryID)
    else:
        product=Product.objects.all()

    data={'product':product, 'category':category}
    return render(request,'index.html',data)

def signup(request):
    if request.method=='GET':
      return render(request,'signup.html')
    else:
        Full_name = request.POST.get('Full_name')
        Phone_no = request.POST.get('Phone_no')
        email= request.POST.get('email')
        password= request.POST.get('password')

        signup= SignUp(Full_name=Full_name, Phone_no=Phone_no,email=email,password=password)
        signup.save()
        return HTTPResponse('form successfully submitted') 

    

