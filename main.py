from flask import Flask

app = Flask(__name__)

@app.route("/api")
def api():
    return {"message": "Hello from API!"}

if __name__ == "__main__":
    app.run(debug=True)  # Not necessary in production, but useful for debugging locally