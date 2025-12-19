from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/health")
def health():
    return jsonify(status="ok")

@app.get("/hello/<name>")
def hello(name: str):
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(debug=True, port=5000)
