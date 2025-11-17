📊 Salary Predictor Web App

A simple and interactive Salary Prediction web application built using FastAPI, HTML/CSS, and a scikit-learn Machine Learning model.
This app predicts salary based on experience level, company size, job role, and employment type.

🚀 Live Demo:
https://huggingface.co/spaces/ananya2299/SalaryPredictor

✨ Features
1. Predict salary using a trained Linear Regression model
2. Clean and simple UI (HTML + CSS)
3. FastAPI backend for fast inference
4. Python + scikit-learn model served via .sav file
5. Fully deployed on Hugging Face Spaces
6. Model
The app uses a Linear Regression model trained on encoded input features:

-Experience Level
-Company Size
-Employment Type
-Job Title (One-Hot Encoded)

Training and preprocessing steps ensure compatibility with the inference pipeline.
Model file included:
lin_regress.sav

🏗️ Project Structure
- main.py               # FastAPI backend
- index.html            # Frontend UI
- requirements.txt      # Python dependencies
- Dockerfile            # Container setup for HF Space
- space.yaml            # Hugging Face Space configuration
- lin_regress.sav       # ML model
- .gitignore

⚙️ Installation (Local Development)

Clone the repo:
git clone https://github.com/ananya2299/SalaryPredictor.git
cd salary-predictor

Install dependencies:
pip install -r requirements.txt

Run the server:
uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000

🐳 Docker (Optional)

Build the image: docker build -t salary-predictor .
Run: docker run -p 7860:7860 salary-predictor

🌐 Deployment (Hugging Face Spaces)

This project is fully configured for HuggingFace deployment using:
- Dockerfile
- space.yaml


Just upload the repo to HuggingFace or connect with GitHub and it deploys automatically.
