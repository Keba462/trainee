"""
URL configuration for trainee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import RedirectView
from trainee.views.administration_view import AdministrationView
from trainee.views.home_view import HomeView
from trainee_subject.admin_site import trainee_subject_admin

app_name ='trainee'

urlpatterns = [

    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),


    path('admin/', admin.site.urls),
    path('admin/',trainee_subject_admin.urls),
    path('administration/', AdministrationView.as_view(),
         name='administration_url'),

    path('admin/trainee_subject/',RedirectView.as_view(url='admin/trainee_subject/'),
         name='trainee_subject_models_url'),
   


    path('edc_base/', include('edc_base.urls')),
    path('edc_consent/', include('edc_consent.urls')),
    path('edc_device/', include('edc_device.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_visit_schedule/', include('edc_visit_schedule.urls')),
    path('edc_registration/', include('edc_registration.urls')),
    path('trainee_subject/', include('trainee_subject.urls')),
    path('subject/', include('trainee_dashboard.urls')),

    path('home/', HomeView.as_view(), name='home_url'),
    path('', HomeView.as_view(), name='home_url'),

]
