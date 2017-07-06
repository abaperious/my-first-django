# howdy/urls.py
from django.conf.urls import url
from howdy import views

urlpatterns = [
    # url(r'^$', views.HomePageView.as_view()),
    url(r'^$', views.post_list, name="post_list"),
    url(r'^about/$', views.AboutPageView.as_view()), # Add this /about/ route
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
