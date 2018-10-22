from django.urls import path, re_path
from . import views

app_name = "users"
urlpatterns = [
    path("", view=views.Feed.as_view(), name="feed"),

    re_path(
        r'explore/$', 
        view=views.ExploreUsers.as_view(),
        name='explore_users'
    ),
]
