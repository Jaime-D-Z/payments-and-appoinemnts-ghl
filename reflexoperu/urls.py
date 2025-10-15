from django.contrib import admin
from django.urls import path, include
# Importa la vista de éxito directamente al archivo principal
from apps.payments.views import PaymentSuccessView 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # --- RUTAS DE API ---
    path('api/appointments/', include('apps.appointments.urls')), 
    path('api/payments/', include('apps.payments.urls')), # Aquí solo quedan: create/ y webhooks/mp/
    # -------------------
    
    # --- RUTAS DE REDIRECCIÓN DE USUARIO (NIVEL RAIZ) ---
    # Mercado Pago dirige aquí: /payment-success/
    path('payment-success/', PaymentSuccessView.as_view(), name='payment-success'),
    # Asegúrate de agregar las de pending y failure también para evitar futuros 404s
    # path('payment-pending/', PaymentPendingView.as_view(), name='payment-pending'),
    # path('payment-failure/', PaymentFailureView.as_view(), name='payment-failure'),
    # ----------------------------------------------------
]
