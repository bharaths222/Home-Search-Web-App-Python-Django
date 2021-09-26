from django.conf.urls import url

from property import views
from search.views import SearchPostListView

app_name = 'search'


urlpatterns =[
     path('',SearchPostListView.as_view(), name='search-query'),
     # url(r'^$',SearchPostListView.as_view(),name='search-query'),
#      url(r'^/(?P<pk>\d+)/$',ProductDetailView.as_view(),name='product-details'),
     
]