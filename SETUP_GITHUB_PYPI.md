# Guía Completa: Configuración de GitHub y Publicación en PyPI

Esta guía te llevará paso a paso para configurar el repositorio en GitHub y publicar el SDK en PyPI.

## Estado Actual ✅

- ✅ Repositorio Git inicializado
- ✅ Primer commit realizado (44 archivos, 4337 líneas)
- ✅ URLs actualizadas para usuario victalejo
- ✅ GitHub Actions configurado (.github/workflows/)
- ✅ Scripts de publicación creados
- ✅ Templates de issues/PRs configurados
- ✅ Código de conducta incluido

## Paso 1: Crear Repositorio en GitHub

### 1.1. Crear Repositorio

1. Ve a https://github.com/victalejo
2. Click en "New repository" o ve a https://github.com/new
3. Configura el repositorio:
   - **Owner**: victalejo
   - **Repository name**: `wasapaso-python-sdk`
   - **Description**: SDK oficial de Python para Wasapaso - Gestión de WhatsApp
   - **Visibility**: Public (recomendado) o Private
   - ⚠️ **NO** marcar "Initialize with README"
   - ⚠️ **NO** marcar ".gitignore"
   - ⚠️ **NO** marcar "license"
4. Click "Create repository"

### 1.2. Conectar Repositorio Local con GitHub

Copia la URL del repositorio (debería ser: https://github.com/victalejo/wasapaso-python-sdk.git)

Luego ejecuta en tu terminal:

```bash
cd "v:\API working\wasapaso\sdk-python"

# Agregar remote
git remote add origin https://github.com/victalejo/wasapaso-python-sdk.git

# Push inicial
git push -u origin main
```

Si usas autenticación con token, el comando será:
```bash
git push -u https://[TU_TOKEN]@github.com/victalejo/wasapaso-python-sdk.git main
```

### 1.3. Verificar en GitHub

Ve a https://github.com/victalejo/wasapaso-python-sdk y verifica que todos los archivos estén ahí.

## Paso 2: Configurar PyPI

### 2.1. Crear Cuenta en PyPI

**PyPI Producción:**
1. Ve a https://pypi.org/account/register/
2. Completa el formulario de registro
3. Verifica tu email
4. Habilita 2FA (recomendado)

**TestPyPI (para pruebas):**
1. Ve a https://test.pypi.org/account/register/
2. Completa el formulario (puede ser la misma info)
3. Verifica tu email

### 2.2. Verificar Disponibilidad del Nombre

1. Ve a https://pypi.org
2. Busca "wasapaso"
3. Si el nombre está disponible, ¡perfecto! Si no, deberás:
   - Cambiar el nombre en `pyproject.toml`
   - Usar algo como "wasapaso-sdk", "wasapaso-client", etc.

### 2.3. Generar API Tokens

**Para PyPI Producción:**
1. Inicia sesión en https://pypi.org
2. Ve a Account Settings: https://pypi.org/manage/account/
3. Scroll a "API tokens"
4. Click "Add API token"
   - Token name: `wasapaso-sdk`
   - Scope: "Entire account" (para el primer upload)
5. **COPIA EL TOKEN** (solo lo verás una vez)
6. Guárdalo en un lugar seguro

**Para TestPyPI:**
1. Repite el proceso en https://test.pypi.org/manage/account/

### 2.4. Configurar Credenciales Locales

Crea o edita el archivo `~/.pypirc`:

**En Windows**: `C:\Users\TuUsuario\.pypirc`
**En Linux/Mac**: `~/.pypirc`

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-TU_TOKEN_AQUI

[testpypi]
username = __token__
password = pypi-TU_TOKEN_TESTPYPI_AQUI
```

⚠️ **Importante**: Reemplaza `pypi-TU_TOKEN_AQUI` con tu token real.

## Paso 3: Configurar GitHub Actions (Opcional pero Recomendado)

Para que GitHub Actions publique automáticamente en PyPI:

### 3.1. Agregar Secrets en GitHub

1. Ve a tu repo: https://github.com/victalejo/wasapaso-python-sdk
2. Click en "Settings" > "Secrets and variables" > "Actions"
3. Click "New repository secret"
4. Agrega:
   - **Name**: `PYPI_API_TOKEN`
   - **Secret**: Tu token de PyPI
5. Click "Add secret"

Opcionalmente, agrega también:
- **Name**: `TEST_PYPI_API_TOKEN`
- **Secret**: Tu token de TestPyPI

## Paso 4: Primera Publicación (Local)

### 4.1. Instalar Herramientas

```bash
pip install build twine
```

### 4.2. Publicar en TestPyPI (Prueba)

**En Linux/Mac:**
```bash
cd "v:\API working\wasapaso\sdk-python"
chmod +x scripts/publish.sh
./scripts/publish.sh testpypi
```

**En Windows:**
```bash
cd "v:\API working\wasapaso\sdk-python"
scripts\publish.bat testpypi
```

**O manualmente:**
```bash
# Limpiar
rm -rf dist/ build/ *.egg-info

# Build
python -m build

# Verificar
twine check dist/*

# Upload a TestPyPI
twine upload --repository testpypi dist/*
```

### 4.3. Probar Instalación desde TestPyPI

```bash
pip install --index-url https://test.pypi.org/simple/ wasapaso
```

Prueba en Python:
```python
from wasapaso import WasapasoClient
print("Import exitoso!")
```

### 4.4. Publicar en PyPI Producción

Si todo funcionó en TestPyPI:

**Con script:**
```bash
./scripts/publish.sh pypi        # Linux/Mac
scripts\publish.bat pypi          # Windows
```

**Manual:**
```bash
twine upload dist/*
```

### 4.5. Verificar Publicación

```bash
pip install wasapaso
python -c "from wasapaso import WasapasoClient; print('✓ SDK instalado correctamente')"
```

Tu paquete estará disponible en: https://pypi.org/project/wasapaso/

## Paso 5: Crear Release en GitHub

### 5.1. Crear Tag

```bash
cd "v:\API working\wasapaso\sdk-python"
git tag -a v0.1.0 -m "Release v0.1.0 - Initial public release"
git push origin v0.1.0
```

### 5.2. Crear Release en GitHub

1. Ve a https://github.com/victalejo/wasapaso-python-sdk/releases
2. Click "Draft a new release"
3. Configura:
   - **Tag**: v0.1.0 (seleccionar el tag que creaste)
   - **Release title**: `v0.1.0 - Initial Release`
   - **Description**: Copia desde CHANGELOG.md o escribe:

```markdown
## 🎉 Primera Versión del SDK de Python para Wasapaso

SDK oficial de Python para la API de Wasapaso con soporte completo para gestión de sesiones de WhatsApp y mensajería.

### ✨ Características

- ✅ Soporte síncrono y asíncrono (async/await)
- ✅ Gestión completa de sesiones
- ✅ Envío de mensajes (texto, multimedia, ubicaciones)
- ✅ Type hints completos con Pydantic
- ✅ Tests comprehensivos
- ✅ Documentación completa

### 📦 Instalación

```bash
pip install wasapaso
```

### 📖 Documentación

- [README](https://github.com/victalejo/wasapaso-python-sdk#readme)
- [Ejemplos](https://github.com/victalejo/wasapaso-python-sdk/tree/main/examples)
- [Docs oficiales](https://docs.wasapaso.com/sdk/python)
```

4. Click "Publish release"

## Paso 6: Post-Publicación

### 6.1. Actualizar Documentación

- [ ] Agregar link del SDK en la documentación principal de Wasapaso
- [ ] Actualizar sitio web con información del SDK
- [ ] Crear post de blog anunciando el SDK

### 6.2. Promoción

- [ ] Anunciar en redes sociales
- [ ] Compartir en comunidades de Python
- [ ] Agregar a awesome lists relevantes

### 6.3. Configurar Protección de Ramas (Opcional)

1. Ve a Settings > Branches
2. Add branch protection rule para `main`
3. Configura:
   - [x] Require pull request reviews
   - [x] Require status checks to pass (CI)
   - [x] Require branches to be up to date

## Resumen de Comandos

```bash
# 1. Conectar con GitHub
cd "v:\API working\wasapaso\sdk-python"
git remote add origin https://github.com/victalejo/wasapaso-python-sdk.git
git push -u origin main

# 2. Instalar herramientas
pip install build twine

# 3. Publicar (opción con script)
scripts\publish.bat testpypi    # Prueba
scripts\publish.bat pypi         # Producción

# 4. Crear release
git tag -a v0.1.0 -m "Release v0.1.0"
git push origin v0.1.0
```

## Troubleshooting

### Error: "Repository not found"
- Verifica que la URL del repo sea correcta
- Verifica tus permisos en GitHub

### Error: "Package already exists"
- El nombre "wasapaso" ya está tomado en PyPI
- Cambia el nombre en `pyproject.toml`

### Error: "Invalid or expired token"
- Regenera tu token en PyPI
- Actualiza el archivo `~/.pypirc`

### Error en Git Push
Si necesitas autenticarte:
```bash
# Configurar credenciales
git config user.name "Tu Nombre"
git config user.email "tu@email.com"

# Usar token de GitHub
git push https://[TOKEN]@github.com/victalejo/wasapaso-python-sdk.git main
```

## Checklist Final

Antes de anunciar públicamente:

- [ ] Repositorio GitHub creado y código subido
- [ ] GitHub Actions funcionando
- [ ] Paquete publicado en PyPI
- [ ] Tests pasando
- [ ] Documentación revisada
- [ ] Release v0.1.0 creada en GitHub
- [ ] README actualizado con badges
- [ ] Ejemplos funcionando
- [ ] License incluida

## Recursos

- **GitHub Repo**: https://github.com/victalejo/wasapaso-python-sdk
- **PyPI Package**: https://pypi.org/project/wasapaso/
- **Documentación**: [README.md](README.md)
- **Guía de Contribución**: [CONTRIBUTING.md](CONTRIBUTING.md)
- **Guía de Publicación**: [PUBLISH.md](PUBLISH.md)

---

🎉 **¡Listo para compartir con el mundo!**
