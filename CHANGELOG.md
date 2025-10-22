# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.1] - 2025-10-22

### Corregido
- **Modelos Pydantic**: Campos `sessionId` y `sessionName` ahora son opcionales en `QRCode` y `PairingCode`
- **Tests de integración**: Eliminado uso incorrecto de `pytest.config.getoption()` que causaba errores

### Agregado
- **Suite de pruebas completa**: 120+ tests (80 unitarios, 40+ de integración)
- **Configuración de tests**: Archivo `.env.test` para API key de pruebas
- **Fixtures globales**: `conftest.py` con fixtures reutilizables
- **Tests de integración**:
  - `test_integration_client.py`: 12 tests para cliente y conexión
  - `test_integration_sessions.py`: 18 tests para operaciones con sesiones
  - `test_integration_messages.py`: 10 tests para mensajes
- **Tests unitarios expandidos**:
  - `test_client.py`: Agregados 7 tests (health_check, get_status, etc.)
  - `test_sessions.py`: Agregados 14 tests (update, QR, pairing, async)
  - `test_messages.py`: Agregados 8 tests (get, reply, base64, async)
  - `test_error_handling.py`: Nuevo archivo con 18 tests de manejo de errores
- **Documentación**: TEST_SUMMARY.md con resumen completo de pruebas
- **Cleanup automático**: Fixture para eliminar sesiones creadas durante tests

### Mejorado
- **Cobertura de tests**: 69% de cobertura total
- **Tests async**: Cobertura completa de métodos asíncronos
- **Manejo de errores**: Tests exhaustivos para todos los códigos HTTP
- **Validación con API real**: Tests de integración confirman funcionamiento con API de producción

## [0.1.0] - 2024-01-01

### Añadido
- Lanzamiento inicial del SDK de Python para Wasapaso
- Soporte completo para gestión de sesiones de WhatsApp
- Soporte completo para envío y gestión de mensajes
- Soporte asíncrono con async/await
- Type hints completos con Pydantic
- Manejo de errores con excepciones específicas
- Suite completa de tests con pytest
- Documentación completa en README.md
- Ejemplos de uso básicos y avanzados

### Características de Sesiones
- Crear, listar, obtener, actualizar y eliminar sesiones
- Iniciar y detener sesiones
- Obtener código QR para autenticación
- Solicitar código de emparejamiento
- Soporte para webhooks personalizados
- Metadata personalizada

### Características de Mensajes
- Enviar mensajes de texto
- Enviar mensajes multimedia (imágenes, videos, audio, archivos)
- Enviar ubicaciones
- Listar y obtener mensajes
- Marcar mensajes como leídos
- Reaccionar a mensajes
- Eliminar mensajes

### Soporte Técnico
- Python 3.8+
- Soporte síncrono y asíncrono
- Type hints completos
- Validación con Pydantic 2.0+
- Cliente HTTP con httpx
