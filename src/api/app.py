from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)