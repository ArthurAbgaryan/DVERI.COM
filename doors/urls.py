from django.urls import path
from .views import index,detail_card,contacts,measure,search,test_filter,ajax_change_color,description_door,test_ajax_post_post,test_ajax_post
#index_category_mobile

app_name = 'doors'
urlpatterns = [
    path('index/',index, name = 'index'),
    path('index/<int:category>/',index, name = 'index_1'),
    path('index/<int:category>/<int:category_next>/',index, name = 'index_2'),
    path('index/<int:category>/<int:category_next>/<int:category_next_2>/',index, name = 'index_3'),
    #path('index/index_mobile/', index_category_mobile, name = 'index_mobile'),
    # path('index/detail/<int:pk>/<int:des>/description/',detail_card, name = 'l_description'),
    path('index/detail/<int:pk>/<int:des>/description/',description_door, name = 'ajax_description'),
    path('index/detail/<int:pk>/',detail_card, name = 'detail_card'),
    path('index/detail/<int:pk>/<int:detail_color_id>/',detail_card, name = 'detail_card_with_color_id'),
    path('index/detail/<int:pk>/<str:detail_size>/',detail_card, name = 'detail_card_with_size'),
    path('search/',search,name = 'search'),
    path('contacts/',contacts, name= 'contacts'),
    path('measure/',measure, name = 'measure'),
    path('test_filter/',test_filter, name = 'test_filter'),
    path('detail_color_ajax/<int:pk>/<int:detail_color_id>/', ajax_change_color, name="ajax_change_color"),

    path('test_ajax_post/', test_ajax_post, name='ajax_test_post'),
    path('test_ajax_post_post/', test_ajax_post_post, name='ajax_test_post'),

]
#
# detail_obj.color_id
# <int:detail_color_id>/