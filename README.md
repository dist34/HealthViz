# 🩺 HealthViz — Smart Healthcare Assistant  
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Project-Active-success)

> 🌿 An AI-powered web app that helps users analyze **X-ray images**, calculate **BMI**, and check **nutritional values** of food — all in one place.

---

## 🌟 Features

### 🧠 X-Ray Image Disease Detection (COVID-19 & Pneumonia)
- Upload chest X-ray images.
- The deep learning model classifies the image into:
  - 🦠 **COVID-19**
  - 🫁 **Pneumonia**
  - 💪 **Normal**
- Built using a **TensorFlow/Keras CNN** model trained on medical datasets.

---

### ⚖️ BMI Calculator
- Input your **height (cm)** and **weight (kg)**.
- Instantly calculate your **Body Mass Index (BMI)**.
- Receive **personalized advice** based on BMI range:
  - Underweight 🥗  
  - Normal 💪  
  - Overweight 🍔  
  - Obese ⚠️  

---

### 🥦 Nutritional Value Displayer
- Enter any **food item** (e.g., *2 chapatis and dal*).
- Fetches real-time nutritional info using the **Nutritionix API**:
  - 🍚 **Calories**
  - 🧈 **Fat**
  - 🥩 **Protein**
  - 🍞 **Carbohydrates**

---

## 🧩 Tech Stack

| Category | Technology |
|-----------|-------------|
| **Frontend** | HTML, CSS |
| **Backend** | Flask (Python) |
| **Machine Learning** | TensorFlow / Keras |
| **API** | Nutritionix API |
| **Model Input Size** | 224 × 224 (RGB) |
| **Deployment** | Flask local server / Render / Heroku |

---

## ⚙️ Installation & Setup

### 🪜 Step 1: Create a Virtual Environment
```
python -m venv venv
```

### 🧩 Step 2: Activate the Virtual Environment
**On Windows:**
```
venv\Scripts\activate
```
**On Mac/Linux:**
```
source venv/bin/activate
```

### 📦 Step 3: Install Dependencies
```
pip install -r requirements.txt
```

### 🚀 Step 4: Run the Application
```
python app.py
```

### 🌐 Step 5: Open in Browser
Open the application in your browser:
```
http://127.0.0.1:5000
```

## 🧠 Model Information

| Attribute | Details |
|------------|----------|
| Input | X-ray image resized to 224 × 224 |
| Framework | TensorFlow / Keras |
| Labels | 0 → COVID<br>1 → NORMAL<br>2 → PNEUMONIA |
| Preprocessing Steps | Image normalization, RGB conversion (for grayscale images), resizing to 224×224 |

