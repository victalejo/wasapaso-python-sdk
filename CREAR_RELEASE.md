# Instrucciones para Crear el Release v0.1.0

## Paso 1: Ir a la Página de Releases

Abre este link en tu navegador:
**https://github.com/victalejo/wasapaso-python-sdk/releases/new**

## Paso 2: Configurar el Release

### Tag
- **Choose a tag**: Seleccionar `v0.1.0` del dropdown (ya existe)

### Release Title
Copiar y pegar:
```
v0.1.0 - Initial Release
```

### Description
Copiar y pegar TODO el siguiente contenido:

---

## 🎉 Primera Versión del SDK de Python para Wasapaso

SDK oficial de Python para la API de Wasapaso con soporte completo para gestión de sesiones de WhatsApp y mensajería.

### ✨ Características Principales

#### Gestión de Sesiones
- ✅ Crear, listar, obtener, actualizar y eliminar sesiones
- ✅ Iniciar y detener sesiones de WhatsApp
- ✅ Obtener códigos QR para autenticación
- ✅ Solicitar códigos de emparejamiento por teléfono
- ✅ Configurar webhooks personalizados
- ✅ Metadata personalizada por sesión

#### Gestión de Mensajes
- ✅ Enviar mensajes de texto
- ✅ Enviar archivos multimedia (imágenes, videos, audio, archivos)
- ✅ Enviar ubicaciones geográficas
- ✅ Listar y obtener historial de mensajes
- ✅ Marcar mensajes como leídos
- ✅ Reaccionar a mensajes con emojis
- ✅ Eliminar mensajes

#### Características Técnicas
- ✅ **Soporte asíncrono completo** con async/await
- ✅ **Type hints completos** con Pydantic 2.0
- ✅ **Cliente HTTP optimizado** con httpx
- ✅ **Validación automática** de datos
- ✅ **Manejo robusto de errores** con excepciones específicas
- ✅ **Tests comprehensivos** con pytest (20+ casos)
- ✅ **Documentación completa** con docstrings y ejemplos

---

## 📦 Instalación

El paquete está disponible en PyPI:

```bash
pip install wasapaso
```

**Link PyPI**: https://pypi.org/project/wasapaso/

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
- **Guía de inicio rápido**: [QUICK_START.md](https://github.com/victalejo/wasapaso-python-sdk/blob/main/QUICK_START.md)

---

## 📊 Estadísticas

- **Líneas de código**: ~2,500+
- **Tests**: 20+ casos de prueba
- **Cobertura**: Configurado para >80%
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

## 🔗 Links

- **GitHub**: https://github.com/victalejo/wasapaso-python-sdk
- **PyPI**: https://pypi.org/project/wasapaso/
- **Issues**: https://github.com/victalejo/wasapaso-python-sdk/issues
- **Documentación Wasapaso**: https://docs.wasapaso.com

---

**Desarrollado con ❤️ para la comunidad de Wasapaso**

---

## Paso 3: Publicar

1. Asegúrate de marcar ✅ **"Set as the latest release"**
2. Click en el botón verde **"Publish release"**

## ✅ ¡Listo!

Tu release estará visible en:
https://github.com/victalejo/wasapaso-python-sdk/releases/tag/v0.1.0

---

**Nota**: También puedes adjuntar los archivos de distribución (opcional):
- `dist/wasapaso-0.1.0-py3-none-any.whl`
- `dist/wasapaso-0.1.0.tar.gz`
