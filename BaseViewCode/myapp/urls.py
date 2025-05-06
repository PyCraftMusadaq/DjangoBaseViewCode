from django.urls import path 
from . import views 

urlpatterns = [
    path("",views.MyDefaultView.as_view(),name="home1"), 
    path("success/<int:pk>/",views.MyDefaultView.as_view(),name="success"),
    path("myclassiew1/",views.MyclassView1.as_view(),name="myclassiew1"),
    path("myclassiew2/",views.MyclassView2.as_view(),name="myclassiew2"),
    path("home/<int:pk>/",views.HomePageView.as_view(extra_context={'course':"Python"}),name="home"),
    path("profile/<int:id>/",views.ProfilePageView.as_view(),name="profile"),
    path("<int:pk>/",views.SingleStudentView.as_view(),name="profile"),
    path("student/<int:pk>/",views.StudentDetailView.as_view(),name="studentdetail"),
]
