from django.urls import path
from .views import index,detail_card,search,contacts,measure
app_name = 'doors'
urlpatterns = [
    path('index/',index, name = 'index'),
    path('index/<int:category>/',index, name = 'index_1'),
    path('index/<int:category>/<int:category_next>/',index, name = 'index_2'),
    path('index/<int:category>/<int:category_next>/<int:category_next_2>/',index, name = 'index_3'),
    path('index/detail/<int:pk>/<int:des>/description/',detail_card, name = 'l_description'),
    path('index/detail/<int:pk>/',detail_card, name = 'detail_card'),
    path('index/detail/<int:pk>/<int:detail_color_id>/',detail_card, name = 'detail_card_with_color_id'),
    path('index/detail/<int:pk>/<str:detail_size>/',detail_card, name = 'detail_card_with_size'),
    path('search/',search,name = 'search'),
    path('contacts/',contacts, name= 'contacts'),
    path('measure/',measure, name = 'measure'),


]
#
# detail_obj.color_id
# <int:detail_color_id>/