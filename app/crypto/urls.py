from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from crypto.views import IndexView,CurrencyListView,PortfolioView,Portfolio_Curr_Delete,Detail_Curr_View

urlpatterns = [
    path('',IndexView.as_view(),name = 'index'),
    path('currency_list/',CurrencyListView.as_view(),name = 'currency_list'),
    path('profile/',PortfolioView.as_view(),name = 'profile'),
    path('delete/<int:pk>/',Portfolio_Curr_Delete.as_view(),name = 'currency_delete'),
    path('detail_curr/<int:pk>/',Detail_Curr_View.as_view(),name = 'currency_detail')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)