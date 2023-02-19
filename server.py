import base64
import whisper
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__, template_folder=".")
socketio = SocketIO(app)

model = whisper.load_model("base.en")

@socketio.on("audio_data")
def handle_audio_data(data):
    decode = base64.b64decode(data)

    with open(f"audio.wav", "wb") as f:
        f.write(decode)
        f.close()

    result = model.transcribe("audio.wav")
    emit("transcription", result["text"])


@app.route("/")
def index():
    return render_template("index.html")

    
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)