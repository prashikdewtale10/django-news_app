from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , views.Sports,name="index"),
    path('newsapi/' , views.Index,name="index"),
    path('bitcoin/' , views.Bitocoin,name="bitcoin"),
    path('business/' , views.Business,name="business"),

]
