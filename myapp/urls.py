# # # from django.urls import path
# # # from . import views


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
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tasks/', views.items_view, name='tasks'),
    path('booking/', views.booking, name='booking'),
    path('results/<int:item_id>/', views.results, name='results'),
    path('travel_page/<int:item_id>/', views.travel_page, name='travel_page'),
    path('proceed_item/<int:item_id>/', views.proceed_item, name='proceed_item'),
    path('complete_item/<int:item_id>/', views.complete_item, name='complete_item'),
    path('survey',views.survey,name='survey'),
    path('test_credentials',views.test_credentials,name='test_credentials'),
    path('report',views.report,name='report'),
    path('about',views.about,name='about'),
    path('extension',views.extension,name='extension'),
    path('study',views.study,name='study'),
    path('experiment',views.experiment,name='experiment'),
    path('long_term',views.long_term,name='long_term'),
    

]
