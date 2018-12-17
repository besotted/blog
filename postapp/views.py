import math
from django.core.paginator import Paginator
from django.shortcuts import render
# Create your views here.
from postapp.models import postblog
def indexview(request,num=1):
    num = int(num)
    post_list = postblog.objects.all()
    post_page = Paginator(post_list,1)
    page_post_list=post_page.page(num)
    start = num - int(math.ceil(10.0 / 2))
    if start < 1:
        start = 1
    end = start + 9
    if end > post_page.num_pages:
        end = post_page.num_pages
    if end<10:
        start=1
    else:
        start=end-9
    page_list=range(start,end+1)
    return render(request, 'index.html', {'postpage': page_post_list, 'num': num,'pagelist':page_list})
def detailview(request,postid):
    postid=int(postid)
    post_obj=postblog.objects.get(id=postid)
    return render(request,'detail.html',{'post_obj':post_obj})


def article_view(request,num):
    num=int(num)
    a_post_list=postblog.objects.filter(id=num)
    return render(request,'article.html',{"a_post_list":a_post_list})


def archive_view(request,y=-1,m=-1):
    y=int(y)
    m=int(m)
    if y==-1 and m==-1:
        data_list=postblog.objects.all()
    else:
        data_list=postblog.objects.filter(timedata__year=y,timedata__month=m)
    return render(request,'article.html',{"a_post_list":data_list})