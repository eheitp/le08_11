
from django.urls import path, include

from TPDHT11 import views, api

urlpatterns = [

    path('data/', views.data, name = 'Data'),
    path('', views.home, name = 'Home'),
    path('csv/', views.exp_csv, name = 'exp-csv'),
    path('home/', views.EditorChartView1.as_view(), name = 'DB'),
    path('charts/', views.EditorChartView.as_view(), name = 'CH'),
    path('charts/1', views.Dater, name = 'CH'),
    ##api
    path('api/list', api.Dlist, name='DHT11List'),

    # genericViews
    path('api/post', api.Dhtviews.as_view(), name='DHT_post'),
]