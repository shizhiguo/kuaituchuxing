from django.http import HttpResponse
from .models import User,KuaituAdminCityOperation,KuaituBike,Account,UserLogin
import json
import struct
import base64
import requests
import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, fromstring

tablename = 'catalina-out'
cfname = 'user'
baseurl = 'http://10.10.0.83:20550'
content = '<?xml version="1.0" encoding="UTF-8"?>'
content += '<TableSchema name="' + tablename + '">'
content += '  <ColumnSchema name="' + cfname + '" />'
content += '</TableSchema>'

def dau_count(request):
    platform=request.GET.get('platform')
    date_start=request.GET.get('start_date')
    date_end = request.GET.get('end_date')
    count,day=process(date_start,date_end,platform)
    data={
        'dau':count,
        'day':day
    }
    print(data)
    return HttpResponse(json.dumps(data), content_type='application/json')


def process(start,end,platform):
    days=get_day(start,end)
    dau_list = []
    day_list=[]
    for i in range(len(days)):
        month_day=days[i]
        dau_list.append(get_info_list(month_day,platform))
        day_list.append(month_day)
    return dau_list,day_list







def get_day(start,end):
    date_list = []
    start = datetime.datetime.strptime(start,"%Y-%m-%d")
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    while start <= end:
        date_str = start.strftime("%m-%d")
        date_list.append(date_str)
        start += datetime.timedelta(days=1)
    return date_list

def get_info_list(day,platform):
    request = requests.get(baseurl + "/" + tablename + "/"+day+"*" , headers={"Accept": "text/xml"})
    root = fromstring(request.text)
    login_count = 0
    for row in root:
        if platform=='3':
            login_count = login_count + 1
        else:
            for cell in row:
                columnname = base64.b64decode(cell.get('column'))
                columnname = bytes.decode(columnname)
                if columnname==cfname+":"+"platform":
                    message=base64.b64decode(cell.text)
                    if bytes.decode(message)==platform:
                        login_count = login_count + 1
    return login_count



def encode(n):
    data = struct.pack("i", n)
    s = base64.b64encode(data)
    return s


# Method for decoding ints with base64 encoding
def decode(s):
    data = base64.b64decode(s)
    n = struct.unpack("i", data)
    return n[0]