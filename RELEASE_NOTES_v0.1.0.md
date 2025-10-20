# Release v0.1.0 - Primera Versión Oficial

## 🎉 Primera Versión del SDK de Python para Wasapaso

SDK oficial de Python para la API de Wasapaso con soporte completo para gestión de sesiones de WhatsApp y mensajería.

---

## ✨ Características Principales

### Gestión de Sesiones
- ✅ Crear, listar, obtener, actualizar y eliminar sesiones
- ✅ Iniciar y detener sesiones de WhatsApp
- ✅ Obtener códigos QR para autenticación
- ✅ Solicitar códigos de emparejamiento por teléfono
- ✅ Configurar webhooks personalizados
- ✅ Metadata personalizada por sesión

### Gestión de Mensajes
- ✅ Enviar mensajes de texto
- ✅ Enviar archivos multimedia (imágenes, videos, audio, archivos)
- ✅ Enviar ubicaciones geográficas
- ✅ Listar y obtener historial de mensajes
- ✅ Marcar mensajes como leídos
- ✅ Reaccionar a mensajes con emojis
- ✅ Eliminar mensajes

### Características Técnicas
- ✅ **Soporte asíncrono completo** con async/await
- ✅ **Type hints completos** con Pydantic 2.0
- ✅ **Cliente HTTP optimizado** con httpx
- ✅ **Validación automática** de datos
- ✅ **Manejo robusto de errores** con excepciones específicas
- ✅ **Tests comprehensivos** con pytest
- ✅ **Documentación completa** con docstrings y ejemplos

---

## 📦 Instalación

El paquete está disponible en PyPI:

```bash
pip install wasapaso
```

---

## 🚀 Inicio Rápido

### Uso Básico (Síncrono)

```python
from wasapaso import WasapasoClient

# Inicializar el cliente
client = WasapasoClient(api_key="wsk_your_api_key_here")

# Crear una sesión
session = client.sessions.create({"name": "Mi Primera Sesión"})

# Iniciar la sesión
client.sessions.start(session.id)

# Enviar un mensaje
result = client.messages.send_text(
    session_id=session.id,
    to="1234567890",
    message="¡Hola desde Wasapaso!"
)
```

### Uso Asíncrono

```python
import asyncio
from wasapaso import WasapasoClient

async def main():
    client = WasapasoClient(api_key="wsk_your_api_key_here")

    # Crear sesión de forma asíncrona
    session = await client.sessions.create_async({"name": "Sesión Async"})

    # Enviar mensaje de forma asíncrona
    result = await client.messages.send_text_async(
        session_id=session.id,
        to="1234567890",
        message="¡Hola async!"
    )

asyncio.run(main())
```

---

## 📚 Documentación

- **README**: [Documentación completa](https://github.com/victalejo/wasapaso-python-sdk#readme)
- **Ejemplos**: [Carpeta de ejemplos](https://github.com/victalejo/wasapaso-python-sdk/tree/main/examples)
- **Guía de contribución**: [CONTRIBUTING.md](https://github.com/victalejo/wasapaso-python-sdk/blob/main/CONTRIBUTING.md)
- **PyPI**: https://pypi.org/project/wasapaso/

---

## 🔗 Links Importantes

- **Repositorio GitHub**: https://github.com/victalejo/wasapaso-python-sdk
- **Paquete PyPI**: https://pypi.org/project/wasapaso/
- **Issues/Bugs**: https://github.com/victalejo/wasapaso-python-sdk/issues
- **Documentación oficial Wasapaso**: https://docs.wasapaso.com

---

## 📊 Estadísticas

- **Líneas de código**: ~2,500+
- **Tests**: 20+ casos de prueba
- **Cobertura**: Configurado para >80%
- **Archivos**: 45 archivos Python
- **Ejemplos**: 3 ejemplos completos
- **Documentación**: 10+ guías

---

## 🛠️ Requisitos

- **Python**: 3.8+
- **Dependencias**:
  - httpx >= 0.25.0
  - pydantic >= 2.0.0
  - typing-extensions >= 4.5.0

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Por favor lee la [guía de contribución](https://github.com/victalejo/wasapaso-python-sdk/blob/main/CONTRIBUTING.md) antes de enviar un pull request.

---

## 📝 Licencia

MIT License - ver [LICENSE](https://github.com/victalejo/wasapaso-python-sdk/blob/main/LICENSE) para más detalles.

---

## 🙏 Agradecimientos

Gracias a todos los que hicieron posible esta primera versión del SDK.

---

**Desarrollado con ❤️ para la comunidad de Wasapaso**
