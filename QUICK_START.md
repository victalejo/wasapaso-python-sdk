# Guía de Inicio Rápido - Wasapaso Python SDK

## Estructura del Proyecto

```
sdk-python/
├── wasapaso/                    # Código fuente del SDK
│   ├── __init__.py             # Exportaciones principales
│   ├── client.py               # Cliente principal WasapasoClient
│   ├── _http_client.py         # Cliente HTTP base
│   ├── exceptions.py           # Excepciones personalizadas
│   ├── models/                 # Modelos de datos con Pydantic
│   │   ├── __init__.py
│   │   ├── session.py          # Modelos de sesiones
│   │   ├── message.py          # Modelos de mensajes
│   │   └── api_key.py          # Modelos de API keys
│   └── resources/              # Recursos de la API
│       ├── __init__.py
│       ├── base.py             # Recurso base
│       ├── sessions.py         # Gestión de sesiones
│       └── messages.py         # Gestión de mensajes
├── tests/                       # Tests con pytest
│   ├── test_client.py
│   ├── test_sessions.py
│   ├── test_messages.py
│   └── test_exceptions.py
├── examples/                    # Ejemplos de uso
│   ├── basic_usage.py
│   ├── async_example.py
│   └── send_message.py
├── .github/workflows/           # GitHub Actions
│   ├── ci.yml                  # CI/CD pipeline
│   └── publish.yml             # Publicación automática
├── pyproject.toml              # Configuración del proyecto
├── setup.py                    # Setup script
├── requirements.txt            # Dependencias
├── requirements-dev.txt        # Dependencias de desarrollo
├── README.md                   # Documentación principal
├── LICENSE                     # Licencia MIT
├── CHANGELOG.md               # Historial de cambios
├── CONTRIBUTING.md            # Guía de contribución
├── PUBLISH.md                 # Guía de publicación
└── pytest.ini                 # Configuración de pytest
```

## Instalación Local para Desarrollo

```bash
cd sdk-python

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate

# Instalar en modo desarrollo con dependencias
pip install -e ".[dev]"
```

## Ejecutar Tests

```bash
# Todos los tests
pytest

# Con cobertura detallada
pytest --cov=wasapaso --cov-report=html

# Ver reporte de cobertura
# Abre: htmlcov/index.html en tu navegador
```

## Uso Básico del SDK

```python
from wasapaso import WasapasoClient

# Inicializar cliente
client = WasapasoClient(api_key="wsk_your_api_key_here")

# Crear sesión
session = client.sessions.create({"name": "Mi Sesión"})

# Iniciar sesión
client.sessions.start(session.id)

# Enviar mensaje
result = client.messages.send_text(
    session_id=session.id,
    to="1234567890",
    message="Hola desde Wasapaso!"
)
```

## Publicar en PyPI

### 1. Primera Vez - Configurar Credenciales

```bash
# Instalar herramientas
pip install build twine

# Crear cuenta en PyPI.org y obtener API token
# Guardar en ~/.pypirc (ver PUBLISH.md para formato completo)
```

### 2. Build del Paquete

```bash
# Limpiar builds anteriores
rm -rf dist/ build/ *.egg-info

# Build
python -m build

# Verificar
twine check dist/*
```

### 3. Publicar en TestPyPI (Prueba)

```bash
twine upload --repository testpypi dist/*

# Probar instalación
pip install --index-url https://test.pypi.org/simple/ wasapaso
```

### 4. Publicar en PyPI (Producción)

```bash
twine upload dist/*
```

### 5. Verificar Publicación

```bash
pip install wasapaso

python -c "import wasapaso; print(wasapaso.__version__)"
```

## Comandos Útiles

```bash
# Formatear código
black wasapaso tests

# Type checking
mypy wasapaso

# Linting
ruff wasapaso tests

# Limpiar archivos generados
rm -rf dist/ build/ *.egg-info .pytest_cache/ .mypy_cache/ htmlcov/
```

## Actualizar Versión

1. Editar `pyproject.toml`:
   ```toml
   [project]
   version = "0.2.0"  # Nueva versión
   ```

2. Actualizar `CHANGELOG.md` con los cambios

3. Crear tag en git:
   ```bash
   git tag -a v0.2.0 -m "Release v0.2.0"
   git push origin v0.2.0
   ```

4. Rebuild y publicar:
   ```bash
   python -m build
   twine upload dist/*
   ```

## Recursos Importantes

- **Documentación**: README.md
- **Ejemplos**: carpeta `examples/`
- **Tests**: carpeta `tests/`
- **Publicación**: PUBLISH.md
- **Contribuir**: CONTRIBUTING.md

## Características Principales

✅ **Soporte Asíncrono**: Todos los métodos tienen versión `_async`
✅ **Type Hints**: Completamente tipado con Pydantic
✅ **Testing**: Suite completa de tests con >80% cobertura
✅ **Documentación**: Ejemplos y docstrings detallados
✅ **CI/CD**: GitHub Actions configurado
✅ **Manejo de Errores**: Excepciones específicas por tipo de error

## Próximos Pasos

1. **Actualizar URL base**: Cambiar en `client.py` la URL por defecto a tu servidor
2. **Probar con API real**: Ejecutar ejemplos con tu API key
3. **Ajustar metadata**: Actualizar info en `pyproject.toml`
4. **Publicar**: Seguir guía en PUBLISH.md
5. **Promover**: Añadir a documentación oficial de Wasapaso

## Soporte

- GitHub Issues: Para reportar bugs
- Email: support@wasapaso.com
- Documentación: https://docs.wasapaso.com

---

🎉 **¡SDK completado y listo para publicar!**
