# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/),
y este proyecto adhiere a [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
