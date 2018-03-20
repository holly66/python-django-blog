from django.conf.urls import url
from blog2 import views
urlpatterns = [
    url(r'^$', views.blog2_title, name="blog2_title"),
    url(r'(?P<article_id>\d)/$',views.blog2_article,name = "blog2_detail"),
]