from flask import Flask, request, jsonify, render_template
import pandas as pd
import os

# Configuración de paths absolutos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'frontend'))

app = Flask(__name__,
            template_folder=os.path.join(FRONTEND_DIR, 'templates'),
            static_folder=os.path.join(FRONTEND_DIR, 'static'))

# Configuración adicional para Windows
app.static_url_path = '/static'
app.static_folder = app.static_folder.replace('\\', '/')
app.template_folder = app.template_folder.replace('\\', '/')

# Cargar la base de conocimiento
KNOWLEDGE_PATH = os.path.join(BASE_DIR, "knowledge_base", "response.csv")
df = pd.read_csv(KNOWLEDGE_PATH)

# Verificación de paths (solo para debug)
print("\n--- Verificación de Paths ---")
print(f"Directorio backend: {BASE_DIR}")
print(f"Directorio frontend: {FRONTEND_DIR}")
print(f"Templates: {app.template_folder}")
print(f"Static: {app.static_folder}")
print(f"CSS existe: {os.path.exists(os.path.join(app.static_folder, 'css', 'styles.css'))}")
print(f"JS existe: {os.path.exists(os.path.join(app.static_folder, 'js', 'script.js'))}\n")

# Rutas
@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/api/chat", methods=['POST'])
def chat():
    user_message = request.json.get('message', "").lower()
    response = df[df['pregunta'].str.lower() == user_message]
    if not response.empty:
        return jsonify({"response": response.iloc[0]['respuesta']})
    return jsonify({"response": "No estoy seguro de entender. ¿Podrías expresarlo de otra manera? 😭"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)