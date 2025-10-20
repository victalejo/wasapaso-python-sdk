# Guía de Publicación en PyPI

Esta guía explica cómo publicar el SDK de Wasapaso en PyPI.

## Prerrequisitos

1. **Cuenta en PyPI y TestPyPI**
   - Crear cuenta en [PyPI](https://pypi.org/account/register/)
   - Crear cuenta en [TestPyPI](https://test.pypi.org/account/register/)

2. **Instalar herramientas de build**
   ```bash
   pip install build twine
   ```

3. **Configurar credenciales**
   Crear archivo `~/.pypirc`:
   ```ini
   [distutils]
   index-servers =
       pypi
       testpypi

   [pypi]
   username = __token__
   password = pypi-tu-token-aqui

   [testpypi]
   username = __token__
   password = pypi-tu-token-testpypi-aqui
   ```

## Pasos para Publicar

### 1. Preparar el Release

```bash
# Asegurarse de estar en la rama main
git checkout main
git pull origin main

# Limpiar builds anteriores
rm -rf dist/ build/ *.egg-info
```

### 2. Actualizar Versión

Editar `pyproject.toml` y actualizar la versión:

```toml
[project]
version = "0.1.0"  # Actualizar según semantic versioning
```

### 3. Actualizar CHANGELOG

Editar `CHANGELOG.md` y documentar los cambios de esta versión.

### 4. Ejecutar Tests

```bash
# Ejecutar todos los tests
pytest

# Verificar cobertura
pytest --cov=wasapaso --cov-report=term-missing

# Type checking
mypy wasapaso

# Formateo
black --check wasapaso tests
```

### 5. Build del Paquete

```bash
# Limpiar dist anterior
rm -rf dist/

# Build
python -m build
```

Esto creará dos archivos en `dist/`:
- `wasapaso-0.1.0-py3-none-any.whl`
- `wasapaso-0.1.0.tar.gz`

### 6. Verificar el Build

```bash
# Verificar que el paquete esté bien formado
twine check dist/*
```

### 7. Publicar en TestPyPI (Opcional pero Recomendado)

```bash
# Subir a TestPyPI
twine upload --repository testpypi dist/*

# Probar instalación desde TestPyPI
pip install --index-url https://test.pypi.org/simple/ wasapaso
```

### 8. Publicar en PyPI

```bash
# Subir a PyPI (producción)
twine upload dist/*
```

### 9. Crear Tag en Git

```bash
# Crear tag
git tag -a v0.1.0 -m "Release version 0.1.0"

# Push tag
git push origin v0.1.0
```

### 10. Verificar Publicación

```bash
# Instalar desde PyPI
pip install wasapaso

# Verificar versión
python -c "import wasapaso; print(wasapaso.__version__)"
```

## Publicación Automatizada con GitHub Actions

Crear `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  pypi-publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build package
        run: python -m build

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

## Semantic Versioning

Seguimos [Semantic Versioning](https://semver.org/):

- **MAJOR** (1.0.0): Cambios incompatibles con versiones anteriores
- **MINOR** (0.1.0): Nueva funcionalidad compatible con versiones anteriores
- **PATCH** (0.0.1): Bug fixes compatibles con versiones anteriores

## Checklist Pre-Publicación

- [ ] Tests pasando (pytest)
- [ ] Type checking pasando (mypy)
- [ ] Código formateado (black)
- [ ] Versión actualizada en pyproject.toml
- [ ] CHANGELOG.md actualizado
- [ ] README.md actualizado si es necesario
- [ ] Build verificado con `twine check`
- [ ] Probado en TestPyPI
- [ ] Tag creado en git
- [ ] Release notes preparadas

## Rollback de una Release

Si necesitas retirar una versión:

```bash
# PyPI no permite eliminar versiones, pero puedes "yankar" una versión
# Contactar a PyPI support o usar la interfaz web
```

## Troubleshooting

### Error: "File already exists"

PyPI no permite re-subir la misma versión. Debes incrementar la versión.

### Error: "Invalid credentials"

Verifica tu token de PyPI en `~/.pypirc` o usa variables de entorno:

```bash
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=pypi-tu-token-aqui
twine upload dist/*
```

### Build contiene archivos no deseados

Verifica `MANIFEST.in` y `.gitignore` para excluir archivos innecesarios.

## Recursos

- [PyPI](https://pypi.org/)
- [TestPyPI](https://test.pypi.org/)
- [Packaging Guide](https://packaging.python.org/)
- [Twine Documentation](https://twine.readthedocs.io/)
