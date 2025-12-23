# LinkedIn Job Scraper (Full Stack)

This is a professional full-stack application that automates job listing extraction from LinkedIn and provides a dashboard for data visualization.

## 🛠 Tech Stack
- **Backend**: Django, Django REST Framework, Selenium, BeautifulSoup4, Pandas.
- **Frontend**: React (Vite), Axios, Chart.js.

## 📂 Project Structure
- `backend/`: Django API and scraping logic.
- `frontend/`: React dashboard.
- `Report.md`: Detailed project report.

## 🚀 Getting Started

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8000
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev -- --port 3000
```

## 📊 Features
- Automated scraping using Selenium.
- Data cleaning and deduplication with Pandas.
- Interactive dashboard with job frequency charts.
