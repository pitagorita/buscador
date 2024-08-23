from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

df = pd.read_excel('datos_trabajadores.xlsx')

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '').lower()
    resultados = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
    return jsonify(resultados.to_dict(orient='records'))

@app.route('/')
def index():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
