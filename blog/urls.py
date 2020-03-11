

from django.urls import path,include
from .views import index
from django.views.generic import TemplateView

urlpatterns = [
     path('',index,name='index'),
    path('about/', TemplateView.as_view(template_name="blog/about.html")),

]