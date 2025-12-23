# Report: LinkedIn Job Scraper

## Introduction
The LinkedIn Job Scraper is a full-stack application designed to automate the extraction of job postings from LinkedIn based on specific keywords and locations. It provides a user-friendly interface to trigger scraping and visualize the distribution of jobs across different companies.

## Abstract
Scraping job data manually is time-consuming. This project automates the process using Selenium and BeautifulSoup. The backend, built with Django and Django REST Framework, handles the scraping logic and data processing. The frontend, built with React, allows users to input search parameters and view the results in real-time, along with a bar chart showing job frequency by company.

## Tools Used
- **Backend**: Django, Django REST Framework, Selenium, BeautifulSoup, Pandas, WebDriver-Manager.
- **Frontend**: React (Vite), Axios, Chart.js.
- **Language**: Python, JavaScript.

## Steps Involved in Building the Project
1. **Environment Setup**: Initialized Django for the backend and Vite for the React frontend.
2. **Backend Logic**:
   - Implemented `LinkedInScraper` class using Selenium to navigate LinkedIn's search results.
   - Used BeautifulSoup to parse job titles, companies, and locations.
   - Leveraged Pandas for data cleaning and duplicate removal.
3. **API Development**:
   - Created DRF views to handle scraping requests and serve visualization data.
   - Configured CORS to allow the React frontend to communicate with the Django backend.
4. **Frontend Development**:
   - Built a dashboard in React with input fields for keywords and locations.
   - Integrated Axios for API calls and Chart.js for data visualization.
5. **Deduplication**: Implemented logic to ensure only unique job listings are saved and displayed.

## Conclusion
The project successfully automates the job search process, providing a structured way to analyze job market trends. The integration of a full-stack architecture ensures scalability and a seamless user experience.
