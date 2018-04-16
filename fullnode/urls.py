from django.urls import path
from . import views

urlpatterns = [
    path('block/<str:hash_id>', views.BlockView),
    path('blockchain/', views.BlockChainView)
]
