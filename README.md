# Elevate Labs Internship Projects - Phase 1

This repository contains two full-stack projects completed as part of the Elevate Labs Internship program.

## 🚀 Projects Overview

| Project | Description | Tech Stack |
| :--- | :--- | :--- |
| **LinkedIn Job Scraper** | Automates job listing extraction from LinkedIn with a visual dashboard. | Django, DRF, Selenium, React |
| **Product Recommendation System** | Machine learning-powered product suggestion engine. | Django, DRF, Scikit-learn, React |

---

## 📂 Repository Structure

```text
.
├── linkedin_job_scraper/           # Project 1 root
│   ├── backend/                    # Django API & Scraper
│   ├── frontend/                   # React Dashboard
│   ├── Report.md                   # 1-2 page project report
│   └── README.md                   # Project-specific setup
├── product_recommendation_system/  # Project 2 root
│   ├── backend/                    # Django API & ML Engine
│   ├── frontend/                   # React UI
│   ├── Report.md                   # 1-2 page project report
│   └── README.md                   # Project-specific setup
└── README.md                       # Main repository guide (This file)
```

---

## 🛠 Prerequisites

Before running the projects, ensure you have the following installed:
- Python 3.10+
- Node.js & npm
- Chrome Browser (for Selenium)

---

## 🚀 Quick Start

### 1. LinkedIn Job Scraper
- **Backend (Port 8000):**
  ```bash
  cd linkedin_job_scraper/backend
  pip install -r requirements.txt
  python manage.py runserver 8000
  ```
- **Frontend (Port 3000):**
  ```bash
  cd linkedin_job_scraper/frontend
  npm install
  npm run dev -- --port 3000
  ```

### 2. Product Recommendation System
- **Backend (Port 8001):**
  ```bash
  cd product_recommendation_system/backend
  pip install -r requirements.txt
  python manage.py runserver 8001
  ```
- **Frontend (Port 3001):**
  ```bash
  cd product_recommendation_system/frontend
  npm install
  npm run dev -- --port 3001
  ```

---

## 📝 Internship Reports
Detailed reports for each project are available within their respective folders:
- [LinkedIn Job Scraper Report](./linkedin_job_scraper/Report.md)
- [Product Recommendation System Report](./product_recommendation_system/Report.md)
