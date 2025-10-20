"""Ejemplo de uso asíncrono del SDK de Wasapaso."""

import asyncio
from wasapaso import WasapasoClient


async def main():
    """Ejemplo principal asíncrono."""
    # Inicializar el cliente
    client = WasapasoClient(api_key="wsk_your_api_key_here")

    # 1. Health check
    print("=== Health Check ===")
    health = await client.health_check_async()
    print(f"API Status: {health['message']}")
    print()

    # 2. Crear sesión de forma asíncrona
    print("=== Creating Session (Async) ===")
    session = await client.sessions.create_async({
        "name": "Sesión Asíncrona",
    })
    print(f"Session created: {session.id}")
    print()

    # 3. Iniciar sesión
    print("=== Starting Session ===")
    session = await client.sessions.start_async(session.id)
    print(f"Session status: {session.status}")
    print()

    # 4. Listar sesiones de forma asíncrona
    print("=== Listing Sessions (Async) ===")
    sessions = await client.sessions.list_async()
    print(f"Total sessions: {sessions.pagination['total']}")
    print()

    # 5. Enviar múltiples mensajes en paralelo (si la sesión está WORKING)
    if session.status == "WORKING":
        print("=== Sending Multiple Messages in Parallel ===")

        # Crear tareas para enviar mensajes en paralelo
        tasks = [
            client.messages.send_text_async(
                session_id=session.id,
                to="1234567890",
                message=f"Mensaje {i} enviado de forma asíncrona"
            )
            for i in range(1, 4)
        ]

        # Ejecutar todas las tareas en paralelo
        results = await asyncio.gather(*tasks)

        for i, result in enumerate(results, 1):
            print(f"Message {i} sent! ID: {result['data']['messageId']}")
        print()

    # 6. Enviar imagen de forma asíncrona
    if session.status == "WORKING":
        print("=== Sending Image (Async) ===")
        result = await client.messages.send_media_async(
            session_id=session.id,
            to="1234567890",
            media_type="image",
            media_url="https://picsum.photos/300",
            caption="Imagen enviada de forma asíncrona"
        )
        print(f"Image sent! ID: {result['data']['messageId']}")
        print()

    # 7. Obtener mensajes de forma asíncrona
    print("=== Listing Messages (Async) ===")
    messages = await client.messages.list_async(session_id=session.id, limit=10)
    print(f"Total messages: {messages.pagination['total']}")
    print()

    # 8. Detener sesión
    print("=== Stopping Session ===")
    session = await client.sessions.stop_async(session.id)
    print(f"Session stopped: {session.status}")
    print()

    print("✓ Async example completed!")


# Ejecutar el ejemplo asíncrono
if __name__ == "__main__":
    asyncio.run(main())
