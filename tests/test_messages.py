"""Tests para el recurso de mensajes."""

import pytest
import respx
import httpx
from wasapaso import WasapasoClient


@pytest.fixture
def client():
    """Fixture del cliente de Wasapaso."""
    return WasapasoClient(api_key="wsk_test_key_1234567890abcdef")


@pytest.fixture
def mock_message_response():
    """Fixture con respuesta simulada de mensaje."""
    return {
        "success": True,
        "message": "Message sent successfully",
        "data": {
            "sessionId": "64abc123",
            "to": "1234567890@c.us",
            "type": "text",
            "messageId": "msg_xyz789",
            "timestamp": "2024-01-01T00:00:00.000Z",
            "result": {}
        }
    }


@respx.mock
def test_send_text_message(client, mock_message_response):
    """Test de envío de mensaje de texto."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/text").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = client.messages.send_text(
        session_id="64abc123",
        to="1234567890",
        message="Test message"
    )

    assert route.called
    assert result["success"] is True
    assert result["data"]["messageId"] == "msg_xyz789"


@respx.mock
def test_send_media_message(client, mock_message_response):
    """Test de envío de mensaje multimedia."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/media").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = client.messages.send_media(
        session_id="64abc123",
        to="1234567890",
        media_type="image",
        media_url="https://example.com/image.jpg",
        caption="Test image"
    )

    assert route.called
    assert result["success"] is True


@respx.mock
def test_send_location_message(client, mock_message_response):
    """Test de envío de ubicación."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/send").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = client.messages.send_location(
        session_id="64abc123",
        to="1234567890",
        latitude=40.7128,
        longitude=-74.0060,
        title="New York"
    )

    assert route.called
    assert result["success"] is True


@respx.mock
def test_list_messages(client):
    """Test de listado de mensajes."""
    list_response = {
        "success": True,
        "data": [
            {
                "id": "msg1",
                "sessionId": "64abc123",
                "messageId": "msg_id_1",
                "from": "1234567890@c.us",
                "to": "0987654321@c.us",
                "body": "Test message",
                "type": "text",
                "timestamp": "2024-01-01T00:00:00.000Z",
                "fromMe": False
            }
        ],
        "pagination": {
            "limit": 50,
            "offset": 0,
            "total": 1,
            "hasMore": False
        }
    }

    route = respx.get("https://api.wasapaso.com/api/v1/messages").mock(
        return_value=httpx.Response(200, json=list_response)
    )

    messages = client.messages.list(session_id="64abc123")

    assert route.called
    assert len(messages.data) == 1
    assert messages.data[0].body == "Test message"


@respx.mock
def test_mark_message_as_read(client):
    """Test de marcar mensaje como leído."""
    read_response = {
        "success": True,
        "message": "Message marked as read"
    }

    route = respx.post("https://api.wasapaso.com/api/v1/messages/msg123/read").mock(
        return_value=httpx.Response(200, json=read_response)
    )

    result = client.messages.mark_as_read("msg123")

    assert route.called
    assert result["success"] is True


@respx.mock
def test_react_to_message(client):
    """Test de reacción a un mensaje."""
    react_response = {
        "success": True,
        "message": "Reaction sent successfully"
    }

    route = respx.post("https://api.wasapaso.com/api/v1/messages/msg123/react").mock(
        return_value=httpx.Response(200, json=react_response)
    )

    result = client.messages.react("msg123", "👍")

    assert route.called
    assert result["success"] is True


@respx.mock
def test_delete_message(client):
    """Test de eliminación de mensaje."""
    delete_response = {
        "success": True,
        "message": "Message deleted successfully"
    }

    route = respx.delete("https://api.wasapaso.com/api/v1/messages/msg123").mock(
        return_value=httpx.Response(200, json=delete_response)
    )

    result = client.messages.delete("msg123", delete_for_everyone=True)

    assert route.called
    assert result["success"] is True


@pytest.mark.asyncio
@respx.mock
async def test_send_text_message_async(client, mock_message_response):
    """Test asíncrono de envío de mensaje de texto."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/text").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = await client.messages.send_text_async(
        session_id="64abc123",
        to="1234567890",
        message="Test async message"
    )

    assert route.called
    assert result["success"] is True


@respx.mock
def test_get_message(client):
    """Test de obtención de mensaje específico."""
    from wasapaso.models.message import Message

    message_response = {
        "success": True,
        "data": {
            "id": "msg123",
            "sessionId": "64abc123",
            "messageId": "msg_id_123",
            "from": "1234567890@c.us",
            "to": "0987654321@c.us",
            "body": "Test message content",
            "type": "text",
            "timestamp": "2024-01-01T00:00:00.000Z",
            "fromMe": False
        }
    }

    route = respx.get("https://api.wasapaso.com/api/v1/messages/msg123").mock(
        return_value=httpx.Response(200, json=message_response)
    )

    message = client.messages.get("msg123")

    assert route.called
    assert isinstance(message, Message)
    assert message.id == "msg123"
    assert message.body == "Test message content"


@pytest.mark.asyncio
@respx.mock
async def test_get_message_async(client):
    """Test asíncrono de obtención de mensaje."""
    from wasapaso.models.message import Message

    message_response = {
        "success": True,
        "data": {
            "id": "msg456",
            "sessionId": "64abc123",
            "messageId": "msg_id_456",
            "from": "5551234567@c.us",
            "to": "5557654321@c.us",
            "body": "Async test message",
            "type": "text",
            "timestamp": "2024-01-01T00:00:00.000Z",
            "fromMe": True
        }
    }

    route = respx.get("https://api.wasapaso.com/api/v1/messages/msg456").mock(
        return_value=httpx.Response(200, json=message_response)
    )

    message = await client.messages.get_async("msg456")

    assert route.called
    assert isinstance(message, Message)
    assert message.body == "Async test message"


@pytest.mark.asyncio
@respx.mock
async def test_send_media_message_async(client, mock_message_response):
    """Test asíncrono de envío de mensaje multimedia."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/media").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = await client.messages.send_media_async(
        session_id="64abc123",
        to="1234567890",
        media_type="image",
        media_url="https://example.com/test.jpg",
        caption="Async test image"
    )

    assert route.called
    assert result["success"] is True


@pytest.mark.asyncio
@respx.mock
async def test_send_location_message_async(client, mock_message_response):
    """Test asíncrono de envío de ubicación."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/send").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = await client.messages.send_location_async(
        session_id="64abc123",
        to="1234567890",
        latitude=51.5074,
        longitude=-0.1278,
        title="London"
    )

    assert route.called
    assert result["success"] is True


@pytest.mark.asyncio
@respx.mock
async def test_list_messages_async(client):
    """Test asíncrono de listado de mensajes."""
    list_response = {
        "success": True,
        "data": [
            {
                "id": "msg1",
                "sessionId": "64abc123",
                "messageId": "msg_id_1",
                "from": "1111111111@c.us",
                "to": "2222222222@c.us",
                "body": "Async test message",
                "type": "text",
                "timestamp": "2024-01-01T00:00:00.000Z",
                "fromMe": True
            }
        ],
        "pagination": {
            "limit": 50,
            "offset": 0,
            "total": 1,
            "hasMore": False
        }
    }

    route = respx.get("https://api.wasapaso.com/api/v1/messages").mock(
        return_value=httpx.Response(200, json=list_response)
    )

    messages = await client.messages.list_async(session_id="64abc123")

    assert route.called
    assert len(messages.data) == 1


@pytest.mark.asyncio
@respx.mock
async def test_mark_message_as_read_async(client):
    """Test asíncrono de marcar mensaje como leído."""
    read_response = {
        "success": True,
        "message": "Message marked as read"
    }

    route = respx.post("https://api.wasapaso.com/api/v1/messages/msg789/read").mock(
        return_value=httpx.Response(200, json=read_response)
    )

    result = await client.messages.mark_as_read_async("msg789")

    assert route.called
    assert result["success"] is True


@pytest.mark.asyncio
@respx.mock
async def test_react_to_message_async(client):
    """Test asíncrono de reacción a un mensaje."""
    react_response = {
        "success": True,
        "message": "Reaction sent successfully"
    }

    route = respx.post("https://api.wasapaso.com/api/v1/messages/msg789/react").mock(
        return_value=httpx.Response(200, json=react_response)
    )

    result = await client.messages.react_async("msg789", "❤️")

    assert route.called
    assert result["success"] is True


@pytest.mark.asyncio
@respx.mock
async def test_delete_message_async(client):
    """Test asíncrono de eliminación de mensaje."""
    delete_response = {
        "success": True,
        "message": "Message deleted successfully"
    }

    route = respx.delete("https://api.wasapaso.com/api/v1/messages/msg789").mock(
        return_value=httpx.Response(200, json=delete_response)
    )

    result = await client.messages.delete_async("msg789", delete_for_everyone=False)

    assert route.called
    assert result["success"] is True


@respx.mock
def test_send_text_with_reply(client, mock_message_response):
    """Test de envío de mensaje con respuesta."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/text").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = client.messages.send_text(
        session_id="64abc123",
        to="1234567890",
        message="Reply message",
        reply_to="msg_original_123"
    )

    assert route.called
    assert result["success"] is True


@respx.mock
def test_send_media_with_base64(client, mock_message_response):
    """Test de envío de media con datos en base64."""
    route = respx.post("https://api.wasapaso.com/api/v1/messages/media").mock(
        return_value=httpx.Response(200, json=mock_message_response)
    )

    result = client.messages.send_media(
        session_id="64abc123",
        to="1234567890",
        media_type="image",
        media_data="base64_encoded_image_data_here",
        mimetype="image/png",
        caption="Image from base64"
    )

    assert route.called
    assert result["success"] is True
