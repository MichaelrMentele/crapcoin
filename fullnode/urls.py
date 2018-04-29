from django.urls import path, re_path
from fullnode import views

urlpatterns = [
    path('block/create', views.BlockCreateView.as_view(), name='transact'),
    path('block/<str:hash_id>', views.BlockView.as_view(), name='block_detail'),
    path('blockchain', views.BlockChainView.as_view(), name='blockchain'),
    path('blockchain/update', views.BlockChainView.as_view(), name='blockchain_update'),
    path('peer', views.PeerView.as_view(), name='peers'),
    path('api/peer/create', views.PeerApi.as_view(), name='api_peer_create'),
    path('api/peer', views.PeerApi.as_view(), name='api_peers'),
    path('sauron/requests', views.RequestView.as_view(), name='requests'),
    re_path(r'sauron/.*', views.RequestView.as_view()),
    re_path(r'.*', views.BlockChainView.as_view())
]
