from django.contrib import admin

# Register your models here.
from .models import User
from .models import KuaituAdminCityOperation, KuaituBike
admin.site.register(User)
admin.site.register(KuaituAdminCityOperation)
admin.site.register(KuaituBike)
