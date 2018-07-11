from django.shortcuts import render

# Create your views here.
from .models import User,KuaituAdminCityOperation,KuaituBike,Account,UserLogin
import json
from django.db.models import Sum
import datetime


def total_bike_bail():
    bike_bail=Account.objects.aggregate(Sum('bike_bail'))
    total_bail=bike_bail['bike_bail__sum']/100
    return total_bail


def count_mon_user():
    gtime = datetime.datetime.now().strftime("%Y-%m")
    start=gtime+"-1"
    end=gtime+"-31"

    month_user=User.objects.raw('select id,create_time,count(*) as sum_total from user where create_time> %s and create_time<%s',[start,end])
    total=0
    for obj in month_user:
        total=obj.sum_total
    return total


def gender_user():
    gender_user=User.objects.raw('select id ,gender,count(*) as sum_gender from user group by gender')
    gender_list=[]
    sum_count=[]
    for i in gender_user:
        gender_list.append(i.gender)
        sum_count.append(i.sum_gender)
    for i in range(len(gender_list)):
        if gender_list[i]==1:
            gender_list[i]='男性'
        if gender_list[i]==2:
            gender_list[i]='女性'
        if gender_list[i]==0:
            gender_list[i]='未知'
    print(gender_list)
    return gender_list,sum_count


def platform_user():
    platform_user = User.objects.raw('select id ,platform,count(*) as sum_platform from user group by platform')
    platform_list=[]
    sum_count=[]
    for i in platform_user:
        platform_list.append(i.platform)
        sum_count.append(i.sum_platform)
    for i in range(len(platform_list)):
        if platform_list[i]==1:
            platform_list[i]='安卓'
        if platform_list[i]==2:
            platform_list[i]='iOS'
        if platform_list[i]==0:
            platform_list[i]='默认'
    print(platform_list)
    return platform_list,sum_count

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
    total_bail=total_bike_bail()

    #计算当月增加用户
    month_user_sum=count_mon_user()

    #计算用户性别
    gender,gender_count=gender_user()

    #计算平台用户
    platform,platform_count=platform_user()


    month,month_count=get_user_count()


    return render(
        request,
        'dashboard.html',
        context={'city_list': json.dumps(city_list),'user_count_list': json.dumps(user_count_list),'user_count': total_user,
                 'totalbike':total_bike,'totalcity':total_citys,'total_bail':total_bail,'month_user_sum':month_user_sum,'gender':json.dumps(gender),'gender_count':json.dumps(gender_count)
                ,'platform':json.dumps(platform),'platform_count':json.dumps(platform_count),'month':json.dumps(month),'month_count':json.dumps(month_count)
                 },
    )

def test(request):
    return render(
        request,
        'first.html',

    )

def dau(request):
    print("dskdsg")
    print(request.POST)
    return render(request,'dashboard.html')


def get_user_count():
    mon_user_register=User.objects.raw('SELECT id,DATE_FORMAT(create_time,%s) as createtime ,count(*) as shumu from user GROUP BY createtime ORDER BY create_time',["%m-%Y"])
    month=[]
    count=[]
    for obj in mon_user_register:
        #print(obj['shumu'])
        month.append(obj.createtime)
        count.append(obj.shumu)

    return month,count



