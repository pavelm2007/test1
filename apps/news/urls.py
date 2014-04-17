from django.conf.urls import *

from .views import *

urlpatterns = patterns('',

                       url(r'^(?P<pk>\d+)/$', NewDetail.as_view(), name='detail'),
                       url(r'post_like/', PostLike.as_view(), name='post_like'),
                       url(r'^$', NewsList.as_view(), name='index'),
)
