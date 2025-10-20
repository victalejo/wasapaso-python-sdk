"""Ejemplo básico de uso del SDK de Wasapaso."""

from wasapaso import WasapasoClient

# Inicializar el cliente con tu API key
client = WasapasoClient(api_key="wsk_your_api_key_here")

# 1. Verificar el estado de la API
print("=== Health Check ===")
health = client.health_check()
print(f"API Status: {health['message']}")
print()

# 2. Obtener información de tu API key
print("=== API Key Info ===")
status = client.get_status()
print(f"API Key Name: {status['apiKey']['name']}")
print(f"Permissions: {status['apiKey']['permissions']}")
print()

# 3. Crear una nueva sesión
print("=== Creating Session ===")
session = client.sessions.create({
    "name": "Mi Primera Sesión",
    "webhookUrl": "https://myapp.com/webhook",  # Opcional
})
print(f"Session created: {session.id}")
print(f"Session status: {session.status}")
print()

# 4. Listar todas las sesiones
print("=== Listing Sessions ===")
sessions = client.sessions.list(limit=10)
print(f"Total sessions: {sessions.pagination['total']}")
for s in sessions.data:
    print(f"  - {s.name} ({s.status})")
print()

# 5. Iniciar la sesión
print("=== Starting Session ===")
session = client.sessions.start(session.id)
print(f"Session status: {session.status}")
print()

# 6. Obtener código QR para autenticar (si está en estado SCAN_QR_CODE)
if session.status == "SCAN_QR_CODE":
    print("=== Getting QR Code ===")
    qr = client.sessions.get_qr(session.id)
    print(f"QR Code available for session: {qr.session_id}")
    print("Scan this QR with WhatsApp to authenticate")
    print()

# 7. Enviar un mensaje de texto (cuando la sesión esté WORKING)
if session.status == "WORKING":
    print("=== Sending Text Message ===")
    result = client.messages.send_text(
        session_id=session.id,
        to="1234567890",  # Reemplazar con número real
        message="¡Hola desde Wasapaso SDK!"
    )
    print(f"Message sent! ID: {result['data']['messageId']}")
    print()

# 8. Enviar una imagen
if session.status == "WORKING":
    print("=== Sending Image ===")
    result = client.messages.send_media(
        session_id=session.id,
        to="1234567890",
        media_type="image",
        media_url="https://picsum.photos/200",
        caption="Imagen de ejemplo"
    )
    print(f"Image sent! ID: {result['data']['messageId']}")
    print()

# 9. Listar mensajes de la sesión
print("=== Listing Messages ===")
messages = client.messages.list(session_id=session.id, limit=5)
print(f"Total messages: {messages.pagination['total']}")
for msg in messages.data:
    print(f"  - From: {msg.from_} | Body: {msg.body}")
print()

# 10. Detener la sesión
print("=== Stopping Session ===")
session = client.sessions.stop(session.id)
print(f"Session stopped: {session.status}")
print()

print("✓ Example completed!")
