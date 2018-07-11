from django.contrib import admin

# Register your models here.
from .models import User
from .models import KuaituAdminCityOperation, KuaituBike, Account,UserLogin
admin.site.register(User)
admin.site.register(KuaituAdminCityOperation)
admin.site.register(KuaituBike)
admin.site.register(Account)
admin.site.register(UserLogin)
