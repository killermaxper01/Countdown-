from flask import Flask, render_template
import os

app = Flask(__name__)

# API key from environment variable (IMPORTANT for security)
API_KEY = "AIzaSyAxC1aZ0zXjFVGg"

MODEL = "gemini-2.5-flash-native-audio-preview-12-2025"

@app.route("/")
def index():
    return render_template(
        "index.html",
        api_key=API_KEY,
        model=MODEL
    )

if __name__ == "__main__":
    app.run(debug=True)