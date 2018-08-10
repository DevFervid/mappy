from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'must'

urlpatterns = [
    # path('', views.IndexView.as_view()),
    # path('<int:item_id>/', views.DetailView.as_view()),
    # path('<int:pk>/', views.post_detail, name='post_detail'),
    # path('create', views.create_item, name='create_item'),
]

urlpatterns = [
	url(r'^$', views.item_list, name='item_list'),
	url(r'^(?P<category_slug>[-\w]+)/$', views.item_list, name='item_list_by_category'),
	url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.item_detail, name='item_detail'),
]
