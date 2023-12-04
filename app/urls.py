from django.urls import path
from.import views

urlpatterns = [
    path('', views.form),
    path('regester',views.registaration),
    path('sucses',views.sucsesregestration),
    path('logout',views.logout),
    path('log',views.login)
]