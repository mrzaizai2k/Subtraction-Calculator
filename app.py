from flask import Flask, jsonify, request
from subtract import subtract
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/subtract')
def api_subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = subtract(a, b)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
