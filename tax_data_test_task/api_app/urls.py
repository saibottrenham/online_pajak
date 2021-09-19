from django.urls import path
from .views import TaxDataCommercialRelScoring, ThirdPartyVerification
urlpatterns = [
    path('third-party/', ThirdPartyVerification.as_view()),
    path('commercial-rel-scoring/', TaxDataCommercialRelScoring.as_view()),
]
