from django.urls import path
from .views import index, passport_birth_certificate_support,service_work_abroad,service_study_abroad,service_visa_assistance,service_flight_reservation,hotel_reservation
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('', index, name='home' ),
    path('service-work-abroad/', service_work_abroad, name='service-work-abroad' ),
    path('service-study-abroad/', service_study_abroad, name='service_study_abroad' ),
    path('service-visa-assistance/', service_visa_assistance, name='service_visa_assistance' ),
    path('service-flight-reservation/', service_flight_reservation, name='service_flight_reservation' ),
    path('hotel-reservation/', hotel_reservation, name='service_hotel_reservation'),
     path('passport-birth-certificate-support/', passport_birth_certificate_support, name='service_passport_birth_certificate'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)