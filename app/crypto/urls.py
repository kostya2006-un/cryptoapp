from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from crypto.views import IndexView,CurrencyListView,PortfolioView

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('currency_list/',CurrencyListView.as_view(),name = 'currency_list'),
    path('profile/',PortfolioView.as_view(),name = 'profile')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)