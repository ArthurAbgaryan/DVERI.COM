from django.urls import path
from .views import index,detail_card
app_name = 'doors'
urlpatterns = [
    path('index/',index, name = 'index'),
    path('index/<int:category>/',index, name = 'index_1'),
    path('index/<int:category>/<int:category_next>/',index, name = 'index_2'),
    path('index/<int:category>/<int:category_next>/<int:category_next_2>/',index, name = 'index_3'),
    path('index/detail/<int:pk>/',detail_card, name = 'detail_card'),
]