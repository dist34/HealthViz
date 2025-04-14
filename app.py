import requests
from flask import Flask, render_template, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

app = Flask(__name__)

# Load the pre-trained X-ray model
model = tf.keras.models.load_model('models/image_model.h5')

# Function to preprocess the X-ray image
def prepare_image(img_path):
    img = Image.open(img_path)
    img = img.resize((224, 224))  # Resize to match model input
    img = np.array(img) / 255.0  # Normalize pixel values
    if img.shape[-1] == 1:  # If grayscale, convert to RGB
        img = np.repeat(img, 3, axis=-1)
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# X-ray Prediction Route
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"})
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"})

    file_path = "data/temp_xray.jpg"
    file.save(file_path)
    img = prepare_image(file_path)
    prediction = model.predict(img)

    class_labels = {0: 'COVID', 1: 'NORMAL', 2: 'PNEUMONIA'}
    predicted_class = class_labels[np.argmax(prediction)]

    return render_template('index.html', prediction=predicted_class)

# BMI Calculator Route
@app.route('/bmi', methods=['POST'])
def calculate_bmi():
    height = float(request.form['height']) / 100  # Convert from cm to meters
    weight = float(request.form['weight'])
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        advice = "You are underweight. A balanced diet with adequate nutrition is recommended."
    elif 18.5 <= bmi < 24.9:
        advice = "You have a healthy weight. Maintain a balanced diet and regular exercise."
    elif 25 <= bmi < 29.9:
        advice = "You are overweight. Consider adopting a healthy eating and exercise routine."
    else:
        advice = "You are obese. It's advisable to consult a healthcare provider for personalized advice."

    return render_template('index.html', bmi=round(bmi, 2), advice=advice)


# Nutrition Information Route
@app.route('/nutrition', methods=['POST'])
def get_nutrition():
    food_item = request.form['food_item']
    url = "https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": "f93cb381",
        "x-app-key": "16e257ddf6e13138fb0505b89b343be7",
        "Content-Type": "application/json"
    }
    data = {"query": food_item}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if result['foods']:
            food = result['foods'][0]
            nutrition_info = {
                'name': food['food_name'].capitalize(),
                'calories': food['nf_calories'],
                'fat': food['nf_total_fat'],
                'protein': food['nf_protein'],
                'carbs': food['nf_total_carbohydrate']
            }
            return render_template('index.html', nutrition_info=nutrition_info)
        else:
            error = "No nutritional data found for this item."
            return render_template('index.html', error=error)
    else:
        error = "Error fetching nutrition data."
        return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
