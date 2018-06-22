from django.shortcuts import render

# Create your views here.
from .models import User,KuaituAdminCityOperation,KuaituBike
import json

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    users_table=User.objects.all()
    total_user=users_table.count()

    city_table=KuaituAdminCityOperation.objects.all()
    total_citys=city_table.count()

    bike_table=KuaituBike.objects.all()
    total_bike=bike_table.count()
    city_code_name=city_table.values_list('area_code','city_name')
    city_list=[]
    user_count_list=[]
    for i in range(len(city_code_name)):
        city_user_count=users_table.filter(area_code=city_code_name[i][0]).count()
        city_list.append(city_code_name[i][1])
        user_count_list.append(city_user_count)





    #num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #num_authors = Author.objects.count()  # The 'all()' is implied by default.

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'dashboard.html',
        context={'city_list': json.dumps(city_list),'user_count_list': json.dumps(user_count_list),'user_count': total_user,
                 'totalbike':total_bike,'totalcity':total_citys},
    )