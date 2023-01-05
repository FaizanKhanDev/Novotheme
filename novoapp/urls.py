from django.urls import path
from novoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.homePage),
    path('aboutus/',views.aboutus,name='aboutus'),
    path('contact/',views.contactus,name='contactus'),
    path('services/',views.services,name='services'),
    path('blog/',views.blog,name='blog'),
    path('thankyou/',views.thanks,name='thanks'),
    path('porfolio',views.portfolio,name='portfolio')
    
    


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)