import re
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Configure o caminho para o Tesseract se necessário

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    expression = data['expression']
    
    # Filtrar apenas números e operadores
    filtered_expression = re.sub(r'[^0-9+\-*/().]', '', expression)

    try:
        # Avaliar a expressão
        result = eval(filtered_expression)
    except Exception as e:
        result = "Erro"

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
