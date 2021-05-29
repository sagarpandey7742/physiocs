from django.urls import path, include
from users.views import APILoginView, APILogoutView, APIPasswordUpdateView
from . import views

urlpatterns = [
    path('login/', APILoginView.as_view(), name='api_login'),
    path('logout/', APILogoutView.as_view(), name='api_logout'),
    path('update_password/', APIPasswordUpdateView.as_view(), name='api_update_password'),
    path('results', views.results, name="results"),
    path('getUserDetails', views.getUserDetails, name='getUserDetails'),
    path('getUserType', views.getUserType, name='getUserType'),
    path('getTestSchedule', views.getTestSchedule, name="getTestSchedule"),
    path('getTestHistory', views.getTestHistory, name="getTestHistory"),
    path('getPrediction', views.getPrediction, name="getPrediction"),
    path('getTests', views.getTests, name="getTests"),
    path('saveTest', views.saveTest, name="saveTest"),
    path('scheduleTest', views.scheduleTest, name="scheduleTest"),
    path('getUserPerfromedTests', views.getUserPerfromedTests, name="getUserPerfromedTests"),
    path('getPatientsForPhysio', views.getPatientsForPhysio, name="getPatientsForPhysio"),
    path('saveUserTest', views.saveUserTest, name='saveUserTest'),

    
]