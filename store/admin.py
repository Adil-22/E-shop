from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.signup import SignUp

class ProductAdmin(admin.ModelAdmin):
    list_display= ( 'product_name', 'category','product_price', 'product_detail', 'product_image')
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display= ('category_name',)
admin.site.register(Category,CategoryAdmin)

class SignUpAdmin(admin.ModelAdmin):
    list_display=('Full_name','Phone_no','email','password')
admin.site.register(SignUp,SignUpAdmin)    


