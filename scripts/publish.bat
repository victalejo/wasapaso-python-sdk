@echo off
REM Script para publicar el SDK de Wasapaso en PyPI (Windows)
REM Uso: scripts\publish.bat [testpypi|pypi]

setlocal

REM Determinar el repositorio destino
set REPOSITORY=%1
if "%REPOSITORY%"=="" set REPOSITORY=testpypi

if not "%REPOSITORY%"=="testpypi" if not "%REPOSITORY%"=="pypi" (
    echo [ERROR] Argumento invalido. Usa 'testpypi' o 'pypi'
    echo Uso: scripts\publish.bat [testpypi^|pypi]
    exit /b 1
)

echo [INFO] Publicando en %REPOSITORY%...

REM Verificar que estamos en el directorio correcto
if not exist "pyproject.toml" (
    echo [ERROR] pyproject.toml no encontrado. Ejecuta este script desde la raiz del proyecto.
    exit /b 1
)

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado
    exit /b 1
)

REM Instalar herramientas
echo [INFO] Instalando/actualizando herramientas de build...
python -m pip install --upgrade pip build twine
if errorlevel 1 (
    echo [ERROR] Error instalando herramientas
    exit /b 1
)

REM Limpiar builds anteriores
echo [INFO] Limpiando builds anteriores...
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build
if exist "*.egg-info" rmdir /s /q *.egg-info

REM Ejecutar tests
echo [INFO] Ejecutando tests...
pytest >nul 2>&1
if errorlevel 1 (
    echo [WARNING] Tests fallaron o pytest no encontrado
    set /p CONTINUE="Continuar de todas formas? (s/n): "
    if /i not "%CONTINUE%"=="s" (
        echo [INFO] Publicacion cancelada
        exit /b 0
    )
)

REM Build del paquete
echo [INFO] Building package...
python -m build
if errorlevel 1 (
    echo [ERROR] Build fallo
    exit /b 1
)

REM Verificar el build
echo [INFO] Verificando build...
twine check dist\*
if errorlevel 1 (
    echo [ERROR] Verificacion del build fallo
    exit /b 1
)

REM Listar archivos a publicar
echo [INFO] Archivos a publicar:
dir /b dist

REM Confirmar antes de publicar en producción
if "%REPOSITORY%"=="pypi" (
    echo [WARNING] Estas a punto de publicar en PyPI PRODUCCION
    set /p CONFIRM="Estas seguro? (yes/no): "
    if /i not "!CONFIRM!"=="yes" (
        echo [INFO] Publicacion cancelada
        exit /b 0
    )
)

REM Publicar
echo [INFO] Publicando en %REPOSITORY%...
if "%REPOSITORY%"=="testpypi" (
    twine upload --repository testpypi dist\*
) else (
    twine upload dist\*
)

if errorlevel 1 (
    echo [ERROR] Publicacion fallo
    exit /b 1
)

echo [INFO] Publicacion exitosa en %REPOSITORY%!

REM Mostrar comando de instalación
if "%REPOSITORY%"=="testpypi" (
    echo [INFO] Para instalar desde TestPyPI:
    echo pip install --index-url https://test.pypi.org/simple/ wasapaso
) else (
    echo [INFO] Para instalar:
    echo pip install wasapaso
)

endlocal
