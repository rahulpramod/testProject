from django.urls import path
from . import views

urlpatterns = [path('',views.home, name='home'), path('add',views.add, name = 'add'),
               path('register', views.register, name = 'register'),
               path('signup', views.signup, name = 'signup'),
               path('about', views.about, name = 'about'),
               path('gohome', views.gohome, name = 'gohome'),
               path('addLogs', views.addLogs, name = 'addLogs'),
               path('post_data', views.post_data, name = 'post_data'),
               path('showLogs', views.showLogs, name = 'showLogs')

               ]