"""Configuración global de pytest y fixtures compartidos."""

import os
from pathlib import Path
from typing import Generator, Optional

import pytest
from wasapaso import WasapasoClient


# Cargar variables de entorno desde .env.test
def load_test_env():
    """Carga variables de entorno desde .env.test si existe."""
    env_file = Path(__file__).parent / ".env.test"
    if env_file.exists():
        with open(env_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ[key.strip()] = value.strip()


# Cargar env antes de ejecutar tests
load_test_env()


@pytest.fixture
def api_key() -> str:
    """
    Fixture que retorna la API key para tests.

    Para tests unitarios (mocks): usa una API key de prueba.
    Para tests de integración: usa la API key real desde .env.test.
    """
    return "wsk_test_key_1234567890abcdef"


@pytest.fixture
def real_api_key() -> Optional[str]:
    """
    Fixture que retorna la API key REAL para tests de integración.

    Returns:
        La API key desde las variables de entorno, o None si no está configurada.
    """
    return os.getenv("WASAPASO_API_KEY")


@pytest.fixture
def base_url() -> str:
    """Fixture que retorna la URL base de la API."""
    return os.getenv("WASAPASO_BASE_URL", "https://api.wasapaso.com")


@pytest.fixture
def client(api_key: str, base_url: str) -> WasapasoClient:
    """
    Fixture que crea un cliente de Wasapaso para tests unitarios.

    Este cliente usa una API key de prueba y está pensado para usarse
    con mocks (respx).
    """
    return WasapasoClient(api_key=api_key, base_url=base_url)


@pytest.fixture
def real_client(real_api_key: Optional[str], base_url: str) -> Optional[WasapasoClient]:
    """
    Fixture que crea un cliente con API key REAL para tests de integración.

    Returns:
        Cliente de Wasapaso configurado con la API key real,
        o None si no hay API key configurada.
    """
    if not real_api_key:
        pytest.skip("No hay API key configurada para tests de integración")

    return WasapasoClient(api_key=real_api_key, base_url=base_url)


@pytest.fixture
def session_ids_to_cleanup() -> Generator[list[str], None, None]:
    """
    Fixture que mantiene track de IDs de sesiones creadas durante tests
    para limpiarlas al final.

    Uso:
        def test_example(real_client, session_ids_to_cleanup):
            session = real_client.sessions.create({"name": "Test"})
            session_ids_to_cleanup.append(session.id)
            # ... tu test ...
            # La sesión será eliminada automáticamente al finalizar
    """
    session_ids: list[str] = []
    yield session_ids

    # Cleanup después del test
    if session_ids and os.getenv("WASAPASO_API_KEY"):
        try:
            client = WasapasoClient(
                api_key=os.getenv("WASAPASO_API_KEY"),
                base_url=os.getenv("WASAPASO_BASE_URL", "https://api.wasapaso.com")
            )
            for session_id in session_ids:
                try:
                    client.sessions.delete(session_id)
                except Exception:
                    # Ignorar errores de cleanup
                    pass
        except Exception:
            pass


@pytest.fixture
def mock_session_response():
    """Fixture con respuesta simulada de sesión para tests unitarios."""
    return {
        "success": True,
        "message": "Session created successfully",
        "data": {
            "id": "64abc123def456",
            "name": "Test Session",
            "sessionName": "session_user123_1234567890",
            "status": "STOPPED",
            "messageCount": 0,
            "isPaid": False,
            "metadata": {},
            "customWebhook": None,
            "webhookEvents": [],
            "createdAt": "2024-01-01T00:00:00.000Z",
            "updatedAt": "2024-01-01T00:00:00.000Z"
        }
    }


@pytest.fixture
def mock_message_response():
    """Fixture con respuesta simulada de mensaje para tests unitarios."""
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


# Marcadores personalizados para pytest
def pytest_configure(config):
    """Configuración personalizada de pytest."""
    config.addinivalue_line(
        "markers", "integration: marca tests de integración que usan la API real"
    )
    config.addinivalue_line(
        "markers", "unit: marca tests unitarios que usan mocks"
    )


# Hook para mostrar información útil al inicio de los tests
def pytest_report_header(config):
    """Muestra información al inicio de la ejecución de tests."""
    api_key = os.getenv("WASAPASO_API_KEY")
    has_real_key = bool(api_key and api_key.startswith("wsk_"))

    return [
        f"Wasapaso SDK Tests",
        f"API Key configurada: {'Sí' if has_real_key else 'No'}",
        f"Base URL: {os.getenv('WASAPASO_BASE_URL', 'https://api.wasapaso.com')}",
        "",
        "Para ejecutar solo tests unitarios: pytest -m unit",
        "Para ejecutar solo tests de integración: pytest -m integration",
    ]
