# 🌾 AgriTech Solutions — Smart Farming Platform

> An AI-powered agricultural intelligence platform that empowers farmers with cutting-edge tools for crop disease detection, yield prediction, crop recommendation, and health classification — all accessible through a clean, responsive web interface.

---

## 📌 Overview

AgriTech Solutions is a full-stack web application that combines **multiple trained ML/AI models** served via **Flask REST APIs** with a **Node.js/Express authentication backend** and a **multi-page HTML frontend**. Farmers land on a polished homepage, log in securely, and access four independent AI-powered services — each backed by its own trained model and Flask microservice.

---

## 🗂️ Project Structure

```
AgriTech-Platform/
│
├── public/                              # All frontend and backend logic
│   ├── index.html                       # Landing page with hero + service cards
│   ├── crop-recommendation.html         # Crop recommendation UI
│   ├── disease-detection.html           # Disease detection UI (image upload)
│   ├── health-classification.html       # Plant health classification UI
│   ├── yield-prediction.html            # Yield prediction UI
│   ├── style.css                        # Global stylesheet
│   │
│   ├── app.py                           # Flask API — Plant Disease Detection (PyTorch CNN)
│   ├── app_health.py                    # Flask API — Plant Health Classification
│   ├── app_reccomend.py                 # Flask API — Crop Recommendation
│   ├── app_yield.py                     # Flask API — Crop Yield Prediction (scikit-learn)
│   │
│   ├── CropReccomendation.ipynb         # Model training notebook — Crop Recommendation
│   ├── CropYieldPrediction.ipynb        # Model training notebook — Yield Prediction
│   ├── PlantDiseaseDetection.ipynb      # Model training notebook — Disease Detection
│   ├── PlantHealthClassification.ipynb  # Model training notebook — Health Classification
│   │
│   └── crop_yield_model.joblib          # Saved scikit-learn yield prediction pipeline
│
├── testimages/                          # Sample crop images for testing ML models
├── package.json                         # Node.js dependencies (auth backend)
└── .gitignore
```

---

## ✨ Features

### 🏠 Landing Page
- Full-screen hero section with animated headings and a CTA button
- Responsive service cards grid — each linking to its own feature page
- Smooth scroll, mobile hamburger menu, scroll-triggered fade-in animations
- Clean green-themed design built with vanilla HTML/CSS/JS

---

### 🔍 1. Plant Disease Detection
**Model:** PyTorch CNN (`trained_plant_disease_model_complete.pth`)  
**API:** `app.py` → Flask server on port `5000`, endpoint `POST /process`

- Upload a photo of a crop leaf via the web UI
- Image is preprocessed: resized to **224×224**, normalized to `[0.5, 0.5, 0.5]`, converted to tensor
- CNN performs **softmax classification** across **38 disease classes**
- Returns the predicted disease name, a detailed botanical description, and a list of treatment recommendations

**Supported crops and diseases (38 classes):**

| Crop | Diseases Detected |
|---|---|
| Apple | Scab, Black Rot, Cedar Apple Rust, Healthy |
| Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |
| Potato | Early Blight, Late Blight, Healthy |
| Grape | Black Rot, Black Measles (Esca), Leaf Blight, Healthy |
| Corn | Gray Leaf Spot, Common Rust, Northern Leaf Blight, Healthy |
| Cherry | Powdery Mildew, Healthy |
| Peach | Bacterial Spot, Healthy |
| Pepper | Bacterial Spot, Healthy |
| Strawberry | Leaf Scorch, Healthy |
| Citrus | Greening (HLB) |
| Blueberry, Raspberry, Soybean | Healthy |
| Squash | Powdery Mildew |

Each prediction returns:
- Causative organism and disease description
- 4–6 specific, actionable treatment steps

---

### 💚 2. Plant Health Classification
**Model:** Trained image classification model  
**API:** `app_health.py` → Flask server

- Upload a crop image to assess overall plant vitality
- Returns a health status classification
- Identifies struggling crops before visible symptoms become severe

---

### 🌱 3. Crop Recommendation
**Model:** Trained ML classifier  
**API:** `app_reccomend.py` → Flask server

- Input soil nutrients, pH, humidity, and climate parameters
- Model recommends the most suitable crop for the given conditions
- Helps optimise planting decisions based on actual field data

---

### 📊 4. Crop Yield Prediction
**Model:** scikit-learn pipeline (`crop_yield_model.joblib`)  
**API:** `app_yield.py` → Flask server, endpoint `POST /predict`

**Input parameters:**

| Parameter | Type | Example |
|---|---|---|
| Region | String | `North` |
| Soil Type | String | `Loamy` |
| Crop | String | `Wheat` |
| Rainfall (mm) | Float | `850.0` |
| Temperature (°C) | Float | `24.5` |
| Fertilizer Used | Boolean | `true` |
| Irrigation Used | Boolean | `false` |
| Weather Condition | String | `Sunny` |
| Days to Harvest | Integer | `120` |

**Output:** Predicted yield in kg/hectare (rounded to 2 decimal places)

The model uses a full sklearn pipeline with preprocessing (encoding + scaling) baked in — no manual feature transformation needed at inference time.

---

## 🛠️ Tech Stack

### ML / AI
| Technology | Usage |
|---|---|
| PyTorch | CNN for 38-class plant disease image classification |
| torchvision | Image preprocessing transforms (Resize, ToTensor, Normalize) |
| scikit-learn | Crop yield prediction pipeline (joblib-serialised) |
| Pillow (PIL) | Image loading and RGB conversion |
| Jupyter Notebooks | Model training, experimentation, evaluation |
| pandas / numpy | Data handling for yield prediction inference |

### Backend — ML APIs
| Technology | Usage |
|---|---|
| Flask | REST API framework for all 4 ML microservices |
| Flask-CORS | Cross-origin requests from frontend HTML pages |
| joblib | Deserialising the scikit-learn yield model |

### Backend — Auth & Data
| Technology | Usage |
|---|---|
| Node.js + Express 5 | Web server and routing |
| PostgreSQL + `pg` | Relational database for user accounts |
| Passport.js (local strategy) | Session-based authentication |
| bcryptjs | Secure password hashing |
| express-session | Persistent login sessions |
| dotenv | Environment variable management |

### Frontend
| Technology | Usage |
|---|---|
| HTML5 / CSS3 | Multi-page responsive UI |
| Vanilla JavaScript | Animations, scroll effects, mobile menu, API calls |
| Font Awesome 6 | Icons throughout the UI |

---

## ⚙️ Setup & Installation

### Prerequisites
- Python 3.8+
- Node.js v18+
- PostgreSQL

### 1. Clone the repository
```bash
git clone https://github.com/VedantKaulgekar/AgriTech-Platform.git
cd AgriTech-Platform
```

### 2. Install Node.js dependencies
```bash
npm install
```

### 3. Configure environment variables
Create a `.env` file in the root:
```env
DATABASE_URL=postgresql://username:password@localhost:5432/agritech
SESSION_SECRET=your_secret_key_here
PORT=3000
```

### 4. Install Python dependencies
```bash
pip install flask flask-cors torch torchvision pillow scikit-learn joblib pandas numpy
```

### 5. Start the Flask ML APIs
Each feature runs as its own Flask microservice. Open a separate terminal for each:

```bash
cd public

# Terminal 1 — Disease Detection (port 5000)
python app.py

# Terminal 2 — Health Classification
python app_health.py

# Terminal 3 — Crop Recommendation
python app_reccomend.py

# Terminal 4 — Yield Prediction
python app_yield.py
```

### 6. Start the Node.js server
```bash
node server.js
```

### 7. Open the app
Navigate to `http://localhost:3000` in your browser.

---

## 🧪 Testing the Models

Sample crop images are available in the `testimages/` folder. Test the disease detection API directly:

```bash
curl -X POST http://localhost:5000/process \
  -F "image=@testimages/sample_leaf.jpg"
```

Expected response:
```json
{
  "predicted_class": "Tomato Late blight",
  "description": "A destructive water mold disease (Phytophthora infestans) causing large, dark water-soaked lesions on leaves and stems...",
  "treatments": [
    "Apply fungicide at first sign",
    "Remove infected plants immediately",
    "Improve air circulation",
    "Water at base of plants",
    "Plant resistant varieties"
  ]
}
```

---

## 📓 Model Training

All four models were trained and evaluated in Jupyter notebooks inside `public/`:

| Notebook | Model Type | Task |
|---|---|---|
| `PlantDiseaseDetection.ipynb` | PyTorch CNN | 38-class image classification across 14 crops |
| `PlantHealthClassification.ipynb` | Image classification | Plant health status assessment |
| `CropReccomendation.ipynb` | ML classifier | Best crop for given soil/climate conditions |
| `CropYieldPrediction.ipynb` | scikit-learn regression | Yield prediction in kg/hectare |

---

## 👨‍💻 Author

**Vedant Kaulgekar**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/vedant-kaulgekar)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/VedantKaulgekar)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
