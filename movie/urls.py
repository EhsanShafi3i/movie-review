from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path('signup/',signup, name='signup'),
    path("movie/<int:movie_id>",detail,name="detail"),
    path("<int:movie_id>/create",createreview,name="createreview"),
    path("review/<int:review_id>/",updatereview,name="updatereview"),
    path("review/<int:review_id>/delete",deletereview,name="deletereview"),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)