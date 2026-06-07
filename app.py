from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_pdf():

    if "pdf" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["pdf"]

    if file.filename == "":
        return jsonify({"error": "No selected file"})

    filename = secure_filename(file.filename)

    path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(path)

    return jsonify({
        "success": True,
        "filename": filename
    })

@app.route("/chat", methods=["POST"])
def chat():

    data = request.json

    question = data.get("question")

    return jsonify({
        "answer": f"You asked: {question}. AI integration coming next."
    })

if __name__ == "__main__":
    app.run(debug=True)
