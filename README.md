# listado_estudiantes
# 🎓 Sistema de Gestión de Estudiantes (CLI)

Un sencillo programa de línea de comandos en Python para **registrar**, **consultar**, **actualizar** y **eliminar** estudiantes, junto con el cálculo de sus promedios.

---

## 📋 Contenido

* `main.py`: Código fuente con todas las funciones (registro, consulta, actualización, borrado, listado).
* `README.md`: Este archivo.

---

## ✨ Funcionalidades

* Registrar un nuevo estudiante con ID, nombre, edad y 4 notas.
* Consultar datos y promedio de un estudiante por ID.
* Actualizar notas de un estudiante existente.
* Eliminar un estudiante por ID.
* Mostrar todos los estudiantes con promedio incluido.
* Menú interactivo y validaciones básicas de entrada.
  ([geeksforgeeks.org][1], [github.com][2], [realpython.com][3], [docs.python-guide.org][4])

---

## 🔧 Requisitos

* Python 3.x instalado en tu sistema.
* No se requieren librerías externas.

---

## 🚀 Instalación y uso

1. Clona el repositorio o descarga `main.py` y `README.md`.
2. En la terminal, ejecuta:

   ```bash
   python main.py
   ```
3. Selecciona la opción deseada en el menú para interactuar con el programa.

---

## 🛠️ Estructura del código

* `students = {}`: Diccionario global que almacena los estudiantes.
* `register_student()`: Agrega un estudiante.
* `query_student()`: Consulta un estudiante.
* `update_grades()`: Actualiza las notas (con validación 0–5).
* `delete_student()`: Elimina un estudiante por ID.
* `view_all()`: Lista todos los estudiantes con promedio.
* `menu()`: Controla el menú principal.

---

## ⚠️ Observaciones y mejoras

* **Bug actual**: Se guarda solo la última nota en `register_student()` porque `students[id]["notas"] = grade` en lugar de `grades`.
* Otras funciones (como `Update_grades`) también usan mal `grade` en lugar de `nota`.
* En `menu()`, se referencia `check_student()`, pero la función correcta es `query_student()`.
* Estas inconsistencias impiden el funcionamiento correcto del sistema.
* 👉 **Sugerencia**: Realiza una revisión y prueba paso a paso de cada función antes de ensamblar el menú.

---

## 🧪 Ejemplos de uso

```text
===== MENÚ PRINCIPAL =====
1. Registrar estudiante
...
Seleccione una opción: 1

Ingrese el número de identificación del estudiante: 123
Ingrese el nombre del estudiante: Ana
Ingrese la edad del estudiante: 20
Ingrese la nota #1: 4.5
...
Estudiante registrado con éxito.
```

---

## 🏗️ Posibles mejoras

* Renombrar `grade` → `grades` y corregir asignaciones en `students[...]`.
* Revisar llamadas en el menú (`query_student()` en vez de `check_student()`).
* Almacenar los datos en un archivo (CSV/JSON) para persistencia.
* Incorporar validaciones adicionales y pruebas unitarias.
* Añadir opción para ver notas individuales al listar estudiantes.

---

## 📝 Contribuir

¿Ves un error o quieres mejorar este proyecto? ¡Bienvenido! Puedes:

1. Forkear el repositorio.
2. Corregir el código (bugs, estilo, validaciones).
3. Crear un PR con tu propuesta.

---

## 📄 Licencia

Proyecto libre para uso y modificación, sin restricciones.

---

## 📚 Recursos útiles (para escribir un buen README)

* Guías para crear README efectivos en proyectos Python o CLI: estructura clara y concisa, ejemplos de uso, cómo contribuir ([realpython.com][3], [github.com][5])
