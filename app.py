from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load trained model
model = tf.keras.models.load_model("crush_model.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prediction")
def prediction():
    return render_template("prediction.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    features = np.array([[
        data["texts_first"],
        data["reply_speed"],
        data["emoji_usage"],
        data["eye_contact"],
        data["shares_personal"]
    ]])

    probability = model.predict(features)[0][0]
    percent = round(probability * 100, 2)

    if percent > 70:
        msg = f"💖 Strong chance they like you! ({percent}%)"
    elif percent > 40:
        msg = f"💗 Mixed signals… maybe? ({percent}%)"
    else:
        msg = f"💔 Low chance 😭 ({percent}%)"

    return jsonify({"message": msg})

if __name__ == "__main__":
    app.run(debug=True)
