from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Configuração da pasta de uploads
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/catalogo')
def catalogo():
    # Retorna o PDF do catálogo
    return send_from_directory(app.config['UPLOAD_FOLDER'], 'catalogo.pdf')

if __name__ == '__main__':
    app.run(debug=True)