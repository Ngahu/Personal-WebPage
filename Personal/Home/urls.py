from django.conf.urls import url

from Home.views import HomePage




urlpatterns = [
    url(r'^$',HomePage.as_view()),
    #url(r'^create/', post_create, name='create'),
    #url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    #url(r'^update/', post_update, name='update'),
    #url(r'^delete/', post_delete, name='delete'),
]