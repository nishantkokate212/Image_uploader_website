from django.urls import path
from posts import views2

urlpatterns = [
    path("",views2.index,name='index'),
    path("home/",views2.home,name='home'),
    path("upload/",views2.upload,name="upload"),
    path("upload_photo/",views2.upload_photo, name="upload_photo"),
    path("sign_up/",views2.sign_up, name="sign_up"),
    path("log_in/",views2.log_in, name="log_in"),
    path("log_out/",views2.log_out, name="log_out"),
    path("footer/",views2.footer, name="footer"),

    
    # path('home', HomePageView.as_view(),name="home"),
    # path("post/",CreatePostView.as_view(),name="add_post"),
]
