#coding=utf-8
from django.db.models import Count

from postapp.models import postblog

from django.db import connection
def getrightinfo(request):
    rstic=postblog.objects.values('stic','stic__sname').annotate(c=Count('*')).order_by('-c')
    cursor=connection.cursor()
    cursor.execute('select timedata,count("*") as c from postapp_postblog group by DATE_FORMAT(timedata,"%Y-%m") order by c desc')
    r_timedata=cursor.fetchall()
    rpost_list=postblog.objects.order_by('-id')[:3]
    return {'rstic':rstic,'r_timedata':r_timedata,'rpost_list':rpost_list}