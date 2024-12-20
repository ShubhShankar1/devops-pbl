from flask import Flask, jsonify

app = Flask(__name__)

# Sample project
@app.route("/")
def home():
    return jsonify({"message": "Welcome to the CI demo Flask app!"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(debug=True)
