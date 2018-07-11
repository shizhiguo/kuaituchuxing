from django.http import HttpResponse
from .models import User,KuaituAdminCityOperation,KuaituBike,Account,UserLogin
import json
def get_user_month(request):
    gender = int(request.GET.get('gender'))
    platform=int(request.GET.get('platform'))
    str=""
    if gender==3 and platform==3:
        user_count = User.objects.raw(
            'SELECT id,DATE_FORMAT(create_time,%s) as createtime ,count(*) as shumu from user  GROUP BY createtime ORDER BY create_time',
            ["%m-%Y"])
    if gender==3 and platform !=3:
        user_count = User.objects.raw(
            'SELECT id,DATE_FORMAT(create_time,%s) as createtime ,count(*) as shumu from user where platform=%s GROUP BY createtime ORDER BY create_time',
            ["%m-%Y",platform])
    if gender !=3 and platform==3:
        user_count = User.objects.raw(
            'SELECT id,DATE_FORMAT(create_time,%s) as createtime ,count(*) as shumu from user where gender=%s GROUP BY createtime ORDER BY create_time',
            ["%m-%Y", gender])
    if gender != 3 and platform != 3:
        user_count = User.objects.raw(
            'SELECT id,DATE_FORMAT(create_time,%s) as createtime ,count(*) as shumu from user where gender= %s and platform=%s GROUP BY createtime ORDER BY create_time',
            ["%m-%Y", gender, platform])
    month=[]
    count=[]
    for obj in user_count:
        month.append(obj.createtime)
        count.append(obj.shumu)
    data={'month':month,
          'count':count}

    return HttpResponse(json.dumps(data), content_type='application/json')