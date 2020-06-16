from django.contrib import admin
from .models import Product, Category, Services, Billboard, AboutUs


### Can be used to hide the add button - Billboard
''' ----- Commented because we want a image carousel instead ----
class BillboardAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and Billboard.objects.exists():
            retVal = False
        return retVal

'''

### AboutUs
class AboutUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        retVal = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if retVal and AboutUs.objects.exists():
            retVal = False
        return retVal



# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Billboard)
admin.site.register(AboutUs, AboutUsAdmin)