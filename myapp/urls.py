# # # from django.urls import path
# # # from . import views

# # # urlpatterns = [
# # #     path('', views.index, name='index'),
# # # ]

# # from django.urls import path
# # from .views import home, items_view, complete_item

# # urlpatterns = [
# #     path('', home, name='home'),
# #     path('items/', items_view, name='items'),
# #     path('complete/', complete_item, name='complete_item'),
# # ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('items/', views.items_view, name='items'),
#     path('proceed/<int:item_id>/', views.proceed_item, name='proceed_item'),
#     path('complete/', views.complete_item, name='complete_item'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.items_view, name='tasks'),
    path('booking/', views.booking, name='booking'),
    path('results/<int:item_id>/', views.results, name='results'),
    path('travel_page/<int:item_id>/', views.travel_page, name='travel_page'),
    path('proceed_item/<int:item_id>/', views.proceed_item, name='proceed_item'),
    path('complete_item/<int:item_id>/', views.complete_item, name='complete_item'),

]
