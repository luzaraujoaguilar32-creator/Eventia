import stripe
from fastapi import APIRouter, Request, HTTPException
from backend.config import settings

router = APIRouter()

@router.post("/stripe/webhook")
async def stripe_webhook(request: Request):
    payload = await request.body()
    signature = request.headers.get("stripe-signature")
    try:
        event = stripe.Webhook.construct_event(
            payload, signature, settings.stripe_webhook_secret
        )
    except Exception as exc:
        raise HTTPException(status_code=400, detail="Webhook no válido.") from exc

    # TODO: procesar eventos relevantes (checkout.session.completed,
    # customer.subscription.updated/deleted) y actualizar PostgreSQL.
    return {"received": True, "event_type": event["type"]}
