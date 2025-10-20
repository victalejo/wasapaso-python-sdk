# Guía de Contribución

¡Gracias por tu interés en contribuir al SDK de Python de Wasapaso!

## Cómo Contribuir

### Reportar Bugs

Si encuentras un bug, por favor abre un issue en GitHub con:

- Descripción clara del problema
- Pasos para reproducir el bug
- Comportamiento esperado vs. comportamiento actual
- Versión de Python y del SDK
- Código de ejemplo que demuestre el problema

### Sugerir Mejoras

Las sugerencias de nuevas características son bienvenidas. Por favor:

- Abre un issue describiendo la funcionalidad propuesta
- Explica por qué esta mejora sería útil
- Proporciona ejemplos de uso si es posible

### Pull Requests

1. **Fork** el repositorio
2. **Crea una rama** para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. **Implementa** tus cambios
4. **Añade tests** para tu nueva funcionalidad
5. **Ejecuta los tests** para asegurar que todo funciona
6. **Formatea el código** con Black
7. **Commit** tus cambios (`git commit -am 'Añadir nueva característica'`)
8. **Push** a la rama (`git push origin feature/nueva-caracteristica`)
9. **Abre un Pull Request**

## Estándares de Código

### Style Guide

- Seguimos [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Usamos [Black](https://black.readthedocs.io/) para formatear código
- Usamos [mypy](https://mypy.readthedocs.io/) para type checking
- Longitud máxima de línea: 100 caracteres

### Type Hints

Todo el código nuevo debe incluir type hints:

```python
def send_message(session_id: str, to: str, message: str) -> Dict[str, Any]:
    ...
```

### Docstrings

Usa docstrings en estilo Google:

```python
def example_function(param1: str, param2: int) -> bool:
    """
    Breve descripción de la función.

    Args:
        param1: Descripción del primer parámetro
        param2: Descripción del segundo parámetro

    Returns:
        Descripción del valor de retorno

    Raises:
        ValueError: Descripción de cuándo se lanza esta excepción

    Example:
        >>> result = example_function("test", 42)
        >>> print(result)
        True
    """
    ...
```

## Testing

### Ejecutar Tests

```bash
# Todos los tests
pytest

# Con cobertura
pytest --cov=wasapaso --cov-report=html

# Tests específicos
pytest tests/test_client.py
```

### Escribir Tests

- Usa `pytest` para todos los tests
- Usa `respx` para mockear requests HTTP
- Usa `pytest-asyncio` para tests asíncronos
- Apunta a una cobertura >80%

Ejemplo:

```python
@respx.mock
def test_create_session(client):
    route = respx.post("https://api.wasapaso.com/api/v1/sessions").mock(
        return_value=httpx.Response(200, json=mock_response)
    )

    session = client.sessions.create({"name": "Test"})

    assert route.called
    assert session.name == "Test"
```

## Desarrollo Local

### Setup

```bash
# Clonar el repositorio
git clone https://github.com/wasapaso/sdk-python.git
cd sdk-python

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias de desarrollo
pip install -e ".[dev]"
```

### Herramientas de Desarrollo

```bash
# Formatear código
black wasapaso tests

# Type checking
mypy wasapaso

# Linting
ruff wasapaso tests

# Tests
pytest
```

## Proceso de Release

Solo para mantenedores:

1. Actualizar versión en `pyproject.toml`
2. Actualizar `CHANGELOG.md`
3. Crear tag: `git tag v0.1.0`
4. Push tag: `git push origin v0.1.0`
5. Build: `python -m build`
6. Upload a PyPI: `twine upload dist/*`

## Código de Conducta

Por favor, sé respetuoso y constructivo en todas las interacciones. Este proyecto sigue el [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/).

## Preguntas

Si tienes preguntas, puedes:

- Abrir un issue en GitHub
- Enviar un email a support@wasapaso.com
- Revisar la [documentación](https://docs.wasapaso.com/sdk/python)

¡Gracias por contribuir! 🎉
