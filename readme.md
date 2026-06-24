# Sistema Experto de Fuerza (POO)

Sistema de consola para evaluar marcas de fuerza (Squat, Bench, Deadlift) y recomendar rutinas correctivas. Desarrollado con Python y MySQL.

## 🚀 Instalación

1. Base de Datos: Ejecuta el archivo `script_db.sql` en tu gestor MySQL (XAMPP/HeidiSQL).
2. Dependencias: Instala el conector necesario desde la terminal:
   pip install mysql-connector-python
3. Ejecución:
   python main.py

## 🏗️ Arquitectura del Proyecto

* main.py: Interfaz de usuario y flujo principal.
* objetos.py: Modelos de clases (Persona, Ejercicio).
* funciones.py: Lógica de negocio (Recomendador).
* persistencia.py: Gestión de base de datos (CRUD y Transacciones).

---
Proyecto final de Programación Orientada a Objetos