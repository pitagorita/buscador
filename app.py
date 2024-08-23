from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar la tabla de Excel al iniciar la app
df = pd.read_excel('datos_trabajadores.xlsx')

@app.route('/buscar', methods=['GET'])
def buscar():
    try:
        query = request.args.get('q', '').lower()
        resultados = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
        return jsonify(resultados.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
