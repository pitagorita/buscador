from flask import Flask, send_from_directory, request, jsonify
import pandas as pd

app = Flask(__name__, static_folder='static')

# Cargar la tabla de Excel
df = pd.read_excel('datos_trabajadores.xlsx')

# Ruta para la página principal
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# Ruta para el buscador
@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').lower()
    resultados = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
    return jsonify(resultados.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
