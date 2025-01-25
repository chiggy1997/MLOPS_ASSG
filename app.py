from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is running inside Docker!"

if __name__ == "__main__":
    app.run(host="localhost", port=5000)