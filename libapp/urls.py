"""libsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
    url(r'^newitem/$',views.newitem, name='newitem'),
    url(r'^suggestions/$',views.suggestions, name='suggestions'),
    url(r'^searchlib/$', views.searchlib, name='searchlib'),
    url(r'^searchresult', views.searchresult, name='searchresult'),
    url(r'^user_login/$',views.user_login, name='user_login'),
    url(r'^user_logout/$',views.user_logout, name='user_logout'),
    url(r'^myitems/$', views.myitems, name='myitems'),
    url(r'^forgot_password/', views.forgot_password, name='forgot_password'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^helloworld$', views.helloworld, name='hello world')
]
