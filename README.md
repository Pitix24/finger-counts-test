# Reconocimiento de Dedos con OpenCV, Flask y MediaPipe

Aplicación web interactiva que detecta manos y cuenta los dedos levantados en tiempo real usando la cámara web.

## Características
- Detección de una o dos manos en tiempo real.
- Dibuja el esqueleto de la mano (landmarks).
- Cuenta cuántos dedos están levantados.
- Muestra el resultado numéricamente en la página web.

## Tecnologías
- Python
- OpenCV
- MediaPipe
- Flask
- HTML/JavaScript

## Instalación y uso

1. **Clona el repositorio:**
bash git clone https://github.com/tu_usuario/tu_repositorio.git cd tu_repositorio

2. **Crea y activa un entorno virtual:**

bash python -m venv venv

#### Windows:
venv\Scripts\activate

#### Linux/Mac:
source venv/bin/activate

3. **Instala las dependencias:**

4. **Ejecuta la aplicación:**
   Luego abre tu navegador en [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Uso de ramas de prueba

Puedes crear una rama para pruebas con:
bash git checkout -b prueba

---

## 3. **Sube tu proyecto a GitHub**

### Si ya tienes el repositorio creado en GitHub:

1. **Inicializa git (si no lo hiciste antes):**
bash git init

2. **Agrega los archivos y haz commit:**
bash git add . git commit -m "Proyecto inicial: reconocimiento de dedos"

3. **Agrega el remoto de GitHub:**
bash git remote add origin https://github.com/tu_usuario/tu_repositorio.git

4. **Sube tu rama principal (main):**
bash git branch -M main git push -u origin main

---

## 4. **Recomendación: requirements.txt**

Si no tienes el archivo `requirements.txt`, créalo con:

bash pip freeze > requirements.txt
