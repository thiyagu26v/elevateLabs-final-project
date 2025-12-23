# Product Recommendation System (Full Stack)

A machine learning-powered application that suggests products based on description similarity.

## 🛠 Tech Stack
- **Backend**: Django, Django REST Framework, Scikit-learn, Pandas.
- **Frontend**: React (Vite), Axios.

## 📂 Project Structure
- `backend/`: Django API and recommendation engine.
- `frontend/`: React UI dashboard.
- `Report.md`: Detailed project report.

## 🚀 Getting Started

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev -- --port 3001
```

## 🧠 Recommendation Engine
Uses **TF-IDF Vectorization** and **Cosine Similarity** to calculate content-based recommendations from a curated product dataset.
