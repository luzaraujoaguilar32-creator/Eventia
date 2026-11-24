# Suscripciones con Stripe
- Planes: Free y Premium.
- El backend crea Checkout Session usando el Price ID de prueba.
- Stripe procesa el pago.
- Stripe envía el webhook firmado.
- El backend verifica la firma y actualiza `subscriptions` en PostgreSQL.
- La aplicación consulta el estado persistido para habilitar funciones.

El alcance inicial cubre suscripciones de Eventia, no anticipos ni pagos de reservaciones de eventos. Usar exclusivamente el modo de prueba durante el desarrollo.
