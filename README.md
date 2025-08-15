# Chatbot Interactivo  

Un chatbot simple pero funcional desarrollado con **Flask** (Python) para el backend y **HTML/CSS/JS** para el frontend.  

##  **Funcionalidades**  
- Interfaz amigable con Bootstrap  
- Diseño responsivo  
- Base de conocimiento en CSV (`response.csv`)  
- Respuestas inteligentes basadas en coincidencias de preguntas  

##  **Estructura del Proyecto**  

chatbot-claseia/
├── backend/
│ ├── app.py # Servidor Flask
│ └── knowledge_base/
│ └── response.csv # Preguntas y respuestas
└── frontend/
├── templates/
│ └── chat.html # Interfaz del chat
└── static/
├── css/
│ └── styles.css # Estilos personalizados
└── js/
└── script.js # Lógica del frontend


##  **Requisitos**  
- Python 3.8+  
- Flask (`pip install flask`)  
- Pandas (`pip install pandas`)  

##  **Instalación**  
1. Clona el repositorio:  
   ```bash
   git clone https://github.com/tu-usuario/chatbot-claseia.git
   cd chatbot-claseia/backend

2. Instala las dependencias:
   pip install -r requirements.txt  # Si usas un archivo requirements.txt

3. Ejecuta el servidor Flask:
   python app.py

4. Abre tu navegador en:
 http://127.0.0.1:5000

### **Personalización**
- Modificar respuestas: Edita backend/knowledge_base/response.csv con nuevas preguntas y respuestas.

- Cambiar estilos: Modifica frontend/static/css/styles.css.

Mejorar lógica: Edita frontend/static/js/script.js.