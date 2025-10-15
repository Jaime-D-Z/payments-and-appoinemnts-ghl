from django.urls import path
# Ya no es necesario importar PaymentSuccessView aquí, pero la dejamos para no romper nada si se usa
from .views import PaymentCreateView, mp_webhook, PaymentSuccessView 

urlpatterns = [
    # Día 1: Crea el link de pago
    path('create/', PaymentCreateView.as_view(), name='create_payment_link'), 
    
    # Día 2: Recibe la notificación de pago de Mercado Pago (Webhook)
    path('webhooks/mp/', mp_webhook, name='mercadopago_webhook'),
    
    # --- RUTA ELIMINADA DE AQUÍ ---
    # path('payment-success/', PaymentSuccessView.as_view(), name='payment-success'), # ¡ELIMINAR O COMENTAR!
    # ------------------------------
]
