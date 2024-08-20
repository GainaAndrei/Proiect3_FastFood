from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('adauga/<int:id_produs>', views.adauga_in_cos, name='adauga_produs_in_cos'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkout/creste/<int:id_produs>/', views.creste_cantitate_cos, name='creste_cantitate_cos'),
    path('checkout/scade/<int:id_produs>/', views.scadere_cantitate_cos, name='scadere_cantitate_cos'),
    path('finalizare_comanda/', views.finalizare_comanda, name='finalizare_comanda'),
    path('comenzi/', views.comenzile_mele, name='comenzi'),
]
