#!/bin/bash
# Script para publicar el SDK de Wasapaso en PyPI
# Uso: ./scripts/publish.sh [testpypi|pypi]

set -e  # Exit on error

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Función para imprimir mensajes
print_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Determinar el repositorio destino
REPOSITORY=${1:-testpypi}

if [ "$REPOSITORY" != "testpypi" ] && [ "$REPOSITORY" != "pypi" ]; then
    print_error "Argumento inválido. Usa 'testpypi' o 'pypi'"
    echo "Uso: ./scripts/publish.sh [testpypi|pypi]"
    exit 1
fi

print_info "Publicando en $REPOSITORY..."

# Verificar que estamos en el directorio correcto
if [ ! -f "pyproject.toml" ]; then
    print_error "pyproject.toml no encontrado. Ejecuta este script desde la raíz del proyecto."
    exit 1
fi

# Verificar que las herramientas estén instaladas
if ! command -v python &> /dev/null; then
    print_error "Python no está instalado"
    exit 1
fi

print_info "Instalando/actualizando herramientas de build..."
python -m pip install --upgrade pip build twine

# Limpiar builds anteriores
print_info "Limpiando builds anteriores..."
rm -rf dist/ build/ *.egg-info

# Ejecutar tests
print_info "Ejecutando tests..."
if command -v pytest &> /dev/null; then
    pytest || {
        print_error "Tests fallaron. Abortando publicación."
        exit 1
    }
else
    print_warning "pytest no encontrado. Saltando tests..."
fi

# Build del paquete
print_info "Building package..."
python -m build

# Verificar el build
print_info "Verificando build..."
twine check dist/* || {
    print_error "Verificación del build falló"
    exit 1
}

# Listar archivos a publicar
print_info "Archivos a publicar:"
ls -lh dist/

# Confirmar antes de publicar
if [ "$REPOSITORY" = "pypi" ]; then
    print_warning "Estás a punto de publicar en PyPI PRODUCCIÓN"
    read -p "¿Estás seguro? (yes/no): " CONFIRM
    if [ "$CONFIRM" != "yes" ]; then
        print_info "Publicación cancelada"
        exit 0
    fi
fi

# Publicar
print_info "Publicando en $REPOSITORY..."
if [ "$REPOSITORY" = "testpypi" ]; then
    twine upload --repository testpypi dist/*
else
    twine upload dist/*
fi

print_info "✓ Publicación exitosa en $REPOSITORY!"

# Mostrar comando de instalación
if [ "$REPOSITORY" = "testpypi" ]; then
    print_info "Para instalar desde TestPyPI:"
    echo "pip install --index-url https://test.pypi.org/simple/ wasapaso"
else
    print_info "Para instalar:"
    echo "pip install wasapaso"
fi
