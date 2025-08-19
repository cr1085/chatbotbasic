# 🤖 Chatbot Interactivo
- Un chatbot simple y funcional, diseñado para fines educativos, que 
- muestra cómo conectar un backend de Python/Flask con un frontend de 
- HTML, CSS y JavaScript.

# Características Principales
- **Backend con Flask:** Servidor ligero y eficiente para manejar la lógica del chatbot.

- **Frontend Amigable:** Interfaz moderna y responsiva construida con HTML, CSS y JavaScript, con el soporte de Bootstrap.

- **Base de Conocimiento:** Utiliza un archivo .csv simple (response.csv) como base de datos para almacenar y gestionar preguntas y respuestas.

- **Lógica de Coincidencias:** Responde de manera inteligente analizando la similitud de las preguntas del usuario con su base de datos.

- **Fácil de Personalizar:** Permite a los usuarios añadir nuevas respuestas y modificar el diseño sin necesidad de conocimientos avanzados.

# 📁 Estructura del Proyecto
**La organización del código está pensada para ser intuitiva y fácil de navegar:**

- chatbot-claseia/
- ├── backend/
- │   ├── app.py                      # 🧠 Lógica principal del servidor Flask
- │   └── knowledge_base/
- │       └── response.csv            # 📚 Base de datos de preguntas y respuestas
- ├── frontend/
- │   ├── static/
- │   │   ├── css/
- │   │   │   └── styles.css          # 🎨 Estilos del chatbot
- │   │   └── js/
- │   │       └── script.js           # ⚙️ Lógica interactiva del frontend
- │   └── templates/
- │       └── chat.html               # 🖥️ Estructura visual de la interfaz
- ├── README.md                       # 📝 Este documento
- └── requirements.txt                # 📦 Dependencias del proyecto

## **Guía de Instalación y Uso**
### **Sigue estos pasos para descargar, configurar y ejecutar el chatbot en tu máquina.**

- **Paso 1:** Requisitos Previos
- **Asegúrate de tener instalado Python 3.8 o superior. Para verificarlo, abre tu terminal y ejecuta:**
  `bash
   python --version
   Paso 2: Descargar el Código
   Clona este repositorio desde GitHub usando git:
  `bash
  git clone https://github.com/tu-usuario/chatbot-claseia.git
  cd chatbot-claseia
- **Paso 3: Instalar Dependencias**
  Navega a la carpeta del backend e instala las bibliotecas necesarias.
 `bash
  cd backend
  pip install -r requirements.txt
- **Nota: He añadido el archivo requirements.txt a la estructura para simplificar la instalación. Si no lo tienes, puedes crearlo y pegar el siguiente contenido:**

- Flask
- pandas

# **Paso 4: Ejecutar el Chatbot**
Desde la carpeta backend, ejecuta el servidor Flask.

Bash

python app.py
Verás un mensaje en la terminal que indica que el servidor se está ejecutando en una dirección local.

Paso 5: Interactuar con el Chatbot
Abre tu navegador web y visita la siguiente dirección para acceder a la interfaz:

http://127.0.0.1:5000
¡Ahora ya puedes empezar a chatear con tu bot!

🛠️ Personalización del Proyecto
Este chatbot está diseñado para que lo modifiques y aprendas. Aquí tienes algunas ideas:

Añadir Nuevas Respuestas: Abre el archivo backend/knowledge_base/response.csv y agrega nuevas filas con preguntas y sus respuestas correspondientes. No olvides reiniciar el servidor (Ctrl+C y python app.py) para que los cambios surtan efecto.

Modificar el Diseño: Edita el archivo frontend/static/css/styles.css para cambiar colores, fuentes o cualquier otro elemento visual.

Mejorar la Lógica: ¿Quieres que el chatbot sea más inteligente? Explora el código en backend/app.py para modificar cómo procesa las preguntas y busca las respuestas.
