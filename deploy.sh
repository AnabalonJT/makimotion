#!/bin/bash

# Script de despliegue para Render
echo "🚀 Iniciando despliegue de MakiMotion..."

# Instalar dependencias
echo "📦 Instalando dependencias..."
pip install -r requirements.txt

# Ejecutar migraciones
echo "🗄️  Ejecutando migraciones..."
python manage.py migrate

# Crear superusuario
echo "👤 Creando superusuario..."
python manage.py create_superuser

# Recopilar archivos estáticos
echo "📁 Recopilando archivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Despliegue completado!"
