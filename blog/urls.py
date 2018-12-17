"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

from blog.settings import DEBUG, MEDIA_ROOT
from postapp import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^postapp/',include('postapp.urls')),
    url(r'^ckeditor/',include('ckeditor_uploader.urls')),
    url(r'^page/(\d+)',views.indexview),
    url(r'^post/(\d+)',views.detailview),
    url(r'^category/(\d+)',views.article_view),
    url(r'^archive/(\d+)/(\d+)',views.archive_view),
    url(r'^archive/',views.archive_view),
    url(r'^search/',include('haystack.urls')),
]
if DEBUG:
    urlpatterns.append(url(r'^media/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),)
