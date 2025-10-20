"""Ejemplos de envío de diferentes tipos de mensajes."""

from wasapaso import WasapasoClient

# Inicializar cliente
client = WasapasoClient(api_key="wsk_your_api_key_here")

# ID de sesión existente (debe estar en estado WORKING)
SESSION_ID = "your_session_id_here"
RECIPIENT = "1234567890"  # Número del destinatario

print("=== Ejemplos de Envío de Mensajes ===\n")

# 1. Mensaje de texto simple
print("1. Enviando mensaje de texto...")
result = client.messages.send_text(
    session_id=SESSION_ID,
    to=RECIPIENT,
    message="¡Hola! Este es un mensaje de prueba."
)
print(f"✓ Mensaje enviado: {result['data']['messageId']}\n")

# 2. Mensaje de texto respondiendo a otro mensaje
print("2. Enviando respuesta a un mensaje...")
result = client.messages.send_text(
    session_id=SESSION_ID,
    to=RECIPIENT,
    message="Esta es una respuesta",
    reply_to="message_id_here"  # ID del mensaje al que responde
)
print(f"✓ Respuesta enviada: {result['data']['messageId']}\n")

# 3. Enviar imagen con caption
print("3. Enviando imagen...")
result = client.messages.send_media(
    session_id=SESSION_ID,
    to=RECIPIENT,
    media_type="image",
    media_url="https://picsum.photos/400/300",
    mimetype="image/jpeg",
    caption="Esta es una imagen de ejemplo"
)
print(f"✓ Imagen enviada: {result['data']['messageId']}\n")

# 4. Enviar video
print("4. Enviando video...")
result = client.messages.send_media(
    session_id=SESSION_ID,
    to=RECIPIENT,
    media_type="video",
    media_url="https://example.com/video.mp4",
    mimetype="video/mp4",
    caption="Video de demostración"
)
print(f"✓ Video enviado: {result['data']['messageId']}\n")

# 5. Enviar archivo PDF
print("5. Enviando archivo PDF...")
result = client.messages.send_media(
    session_id=SESSION_ID,
    to=RECIPIENT,
    media_type="file",
    media_url="https://example.com/document.pdf",
    mimetype="application/pdf",
    filename="documento.pdf",
    caption="Aquí está el documento solicitado"
)
print(f"✓ Archivo enviado: {result['data']['messageId']}\n")

# 6. Enviar ubicación
print("6. Enviando ubicación...")
result = client.messages.send_location(
    session_id=SESSION_ID,
    to=RECIPIENT,
    latitude=40.7128,
    longitude=-74.0060,
    title="Nueva York, NY"
)
print(f"✓ Ubicación enviada: {result['data']['messageId']}\n")

# 7. Obtener historial de mensajes
print("7. Obteniendo historial de mensajes...")
messages = client.messages.list(
    session_id=SESSION_ID,
    chat_id=f"{RECIPIENT}@c.us",
    limit=10
)
print(f"✓ Total de mensajes: {messages.pagination['total']}")
for msg in messages.data[:3]:  # Mostrar solo los primeros 3
    print(f"   - {msg.from_}: {msg.body}")
print()

# 8. Marcar mensaje como leído
print("8. Marcando mensaje como leído...")
# Obtener el último mensaje
if messages.data:
    last_message = messages.data[0]
    result = client.messages.mark_as_read(last_message.id)
    print(f"✓ Mensaje marcado como leído\n")

# 9. Reaccionar a un mensaje
print("9. Reaccionando a un mensaje...")
if messages.data:
    result = client.messages.react(
        message_id=messages.data[0].id,
        reaction="👍"
    )
    print(f"✓ Reacción enviada\n")

print("✓ Todos los ejemplos completados!")
