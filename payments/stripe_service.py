\"\"\"Operaciones de Stripe. Completar con Price ID del entorno de pruebas.\"\"\"
import stripe
from backend.config import settings

stripe.api_key = settings.stripe_secret_key

def create_checkout_session(user_id: str, customer_email: str):
    if not settings.stripe_price_id_premium:
        raise RuntimeError("Falta STRIPE_PRICE_ID_PREMIUM en la configuración.")
    return stripe.checkout.Session.create(
        mode="subscription",
        line_items=[{"price": settings.stripe_price_id_premium, "quantity": 1}],
        customer_email=customer_email,
        client_reference_id=user_id,
        success_url=f"{settings.frontend_url}/?payment=success",
        cancel_url=f"{settings.frontend_url}/?payment=cancel",
    )
