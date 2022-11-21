from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('best-way-to-make-money-with-sports-betting', views.make_money_with_sports_betting, name='make_money_with_sports_betting'),
    path('landing-page',views.landing_page,name='landing_page'),
    path('over-under-strategy',views.over_under,name='over_under'),
]