from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head><title>Simple Calculator</title></head>
    <body>
        <h1>Simple Addition Calculator</h1>
        <form action="/add" method="get">
            <label>Number 1: <input type="number" name="a" value="5"></label><br>
            <label>Number 2: <input type="number" name="b" value="3"></label><br>
            <input type="submit" value="Add">
        </form>
    </body>
    </html>
    '''

@app.route('/add')
def add():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = a + b
        return jsonify({'a': a, 'b': b, 'result': result})
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
