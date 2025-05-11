# Calculadora Web con Flask y Docker

Esta es una aplicación web simple de calculadora desarrollada con Flask, contenerizada con Docker e implementada con pruebas unitarias en Python.

## 📦 Requisitos

- Python 3.8+
- Docker
- Docker Composev

## 🚀 Cómo ejecutar localmente

```bash
CREAR ENTORNO VIRTUAL

py -m venv venv

ACTIVAR ENTORNO VIRTUALIZADO

.\venv\Scripts\activate

INSTALAR DEPENDECIAS

pip install werkzeug==2.0.3

pip install coverage

EJECUTAR APLICACION

python app.py

en el terminal mostrara un enlace 
http://localhost:5000

EJECUTAR PRUEBAS UNITARIAS

python -m unittest tests/test_app.py

GENERAR REPORTE

coverage run -m unittest discover -s tests

VER REPORTE EN CONSOLA

coverage report

GENERAR REPORTE EN HTML

coverage html

ABRIR REPORTE EN WEB 

htmlcov/index.html

APLICAR DOCKER

Construir la imagen:

docker build -t calculadora-app .

Ejecutar el contenedor:

docker run -p 5000:5000 calculadora-app

enlace: http://localhost:5000
