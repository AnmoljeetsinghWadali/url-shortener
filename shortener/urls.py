
from django.urls import path
from . import views
from django.views.generic import RedirectView

urlpatterns = [
path("",RedirectView.as_view(url="/shorten/")),
    path('shorten/',views.get_form,name="urlForm"),
     path('<short_url>/',views.redirect_short_url,name="redirect")
   
]