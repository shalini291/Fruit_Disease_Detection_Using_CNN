🍎 Fruit Disease Detection Using CNN
📌 Project Overview

This project implements a Convolutional Neural Network (CNN) model to detect and classify diseases in fruits from images. Users can upload fruit images and the system will predict whether the fruit is healthy or diseased based on learned visual patterns from the training dataset.

🧠 Key Features

✔️ Detect fruit diseases using deep learning
✔️ Simple and user-friendly interface
✔️ Powered by a CNN model trained on fruit image data
✔️ Backend logic written in Python (Flask)
✔️ Static dataset and model integration

🗂️ Repository Structure
Fruit_Disease_Detection_Using_CNN/
├── .idea/
├── static/              # Frontend static assets (images, CSS, JS)
├── templates/           # HTML files for prediction UI
├── app.py               # Main Flask application file
├── create.py            # Utility for dataset/model preparation
├── resnet.py            # CNN model architecture and training logic
├── database.sql         # Database schema for storing data (if used)
└── README.md            # Project documentation

🛠️ Technologies Used

Python – Backend development

Flask – Web server framework

CNN (Convolutional Neural Network) – Deep learning model for image classification

HTML/CSS/JS – Frontend templates

SQL – (Optional) database for storing results

📥 Requirements

Before running the project, you need:

✔ Python 3.x
✔ Flask
✔ TensorFlow / Keras
✔ OpenCV / Pillow
✔ Other ML libraries (NumPy, scikit-learn, etc.)

Install dependencies:

pip install -r requirements.txt


If you don’t have a requirements.txt file yet, you can manually install:

pip install flask tensorflow numpy pillow

🚀 How to Run Locally

Clone the repo:

git clone https://github.com/shalini291/Fruit_Disease_Detection_Using_CNN.git


Navigate into project directory:

cd Fruit_Disease_Detection_Using_CNN


Install dependencies (as shown above)

Start the Flask app:

python app.py


Open your browser and visit:

http://localhost:5000/

🧪 How It Works

User uploads a fruit image through the web UI

Flask backend preprocesses the image

Image fed into the CNN model

The model predicts healthy or diseased fruit

Results shown back on the webpage

📁 Dataset & Model Training

The CNN model was trained on labeled images of healthy and diseased fruits using typical deep learning approaches:

Image preprocessing

Train/validation split

CNN layers + pooling + dropout

Softmax classification

Data augmentation techniques (rotation, flip, scaling) can be used to improve accuracy. 
GitHub

🔮 Future Enhancements

✅ Add more fruit categories
✅ Improve model accuracy with larger datasets
✅ Add image upload error handling
✅ Deploy web app online (Heroku / Render / Fly.io)
✅ Add live camera capture for prediction
