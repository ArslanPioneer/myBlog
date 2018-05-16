from django.conf.urls import url

from . import views

#告诉Django这个urls.py是属于myBlog应用的,这种技术叫做视图函数命名空间
app_name='myBlog'
urlpatterns=[
    #主页
    url(r'^$',views.index,name='index'),
    #文章详情页
    url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    #归档
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
    #分类
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category')
]

