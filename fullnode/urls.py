from django.urls import path, re_path
from fullnode import views

urlpatterns = [
    path('block/<str:hash_id>', views.BlockView.as_view(), name='block_detail'),
    path('blockchain', views.BlockChainView.as_view(), name='blockchain'),
    path('sauron/requests', views.RequestView.as_view()),
    re_path(r'sauron/.*', views.RequestView.as_view()),
    re_path(r'.*', views.BlockChainView.as_view())
]
