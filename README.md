# Calculadora Web con Flask y Docker

Esta es una aplicación web simple de calculadora desarrollada con Flask, contenerizada con Docker e implementada con pruebas unitarias en Python.

## 📦 Requisitos

- Python 3.8+
- Docker
- Docker Composev

## 🚀 Cómo ejecutar localmente

```bash
\_CREAR ENTORNO VIRTUAL\_

py -m venv venv

\_ACTIVAR ENTORNO VIRTUALIZADO\_

.\venv\Scripts\activate

\_INSTALAR DEPENDENCIAS\_

pip install werkzeug==2.0.3

pip install coverage

\_EJECUTAR APLICACION\_

python app.py

en el terminal mostrara un enlace 
http://localhost:5000

\_EJECUTAR PRUEBAS UNITARIAS\_

python -m unittest tests/test_app.py

\_GENERAR REPORTE\_

coverage run -m unittest discover -s tests

\_VER REPORTE EN CONSOLA\_

coverage report

\_GENERAR REPORTE EN HTML\_

coverage html

\_ABRIR REPORTE EN WEB\_ 

htmlcov/index.html

\_APLICAR DOCKER\_

Construir la imagen:

docker build -t calculadora-app .

Ejecutar el contenedor:

docker run -p 5000:5000 calculadora-app

enlace: http://localhost:5000
