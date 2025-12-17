  # 💘 AI Crush Prediction

A fun AI-based web application that predicts whether your crush likes you
based on interaction patterns.

  ## 🚀 Features
- Neural Network (MLP) using TensorFlow
- Flask backend
- Interactive UI with hearts & confetti
- Binary classification (Like / Not Like)
-
**##Project Structure**
crush_prediction/
│
├─ templates/
│   ├─ index.html          ← Main neon intro page
│   └─ prediction.html     ← AI prediction page
│
├─ static/
│   ├─ style.css           ← All CSS (neon, hearts, forms)
│   └─ script.js           ← Hearts animation + cursor + clicks
│
├─ app.py                 ← Flask backend
├─ model.py               ← Your AI model (optional for training)

  ## 🧠 Model Inputs
- Texts first
- Reply speed
- Emoji usage
- Eye contact
- Shares personal things

  ## 🛠 Tech Stack
- Python
- TensorFlow / Keras
- Flask
- HTML, CSS, JavaScript

  ## ▶ How to Run
```bash
pip install -r requirements.txt
python app.py
