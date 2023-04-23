
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('login_user', views.login_user, name="login"),
    path('logout_user', views.logout_user, name="logout"),
    path('create_user', views.create_user, name="create_user"),
    path('edit_profile', views.UserEditView.as_view(), name="edit_profile"),
    path('delivery', views.delivery, name="delivery"),
    path('booking', views.booking, name="booking"),
    path('collection', views.collection, name="collection"),
]
