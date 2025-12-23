import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import os

class LinkedInScraper:
    def __init__(self):
        self.options = Options()
        # self.options.add_argument("--headless")  # Optional: run in headless mode
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.options)
        self.wait = WebDriverWait(self.driver, 10)

    def scrape_jobs(self, keywords, location, num_jobs=10):
        search_url = f"https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}"
        self.driver.get(search_url)
        time.sleep(5)

        job_list = []
        
        # Simple scroll to load more jobs
        for _ in range(2):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        cards = soup.find_all('div', {'class': 'base-card'})

        for card in cards[:num_jobs]:
            try:
                title = card.find('h3', {'class': 'base-search-card__title'}).text.strip()
                company = card.find('h4', {'class': 'base-search-card__subtitle'}).text.strip()
                location_val = card.find('span', {'class': 'job-search-card__location'}).text.strip()
                post_date = card.find('time')['datetime'] if card.find('time') else "N/A"
                
                job_list.append({
                    'Title': title,
                    'Company': company,
                    'Location': location_val,
                    'Post Date': post_date
                })
            except Exception as e:
                print(f"Error parsing a card: {e}")
                continue

        return job_list

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    scraper = LinkedInScraper()
    try:
        results = scraper.scrape_jobs("Python Developer", "India", num_jobs=20)
        df = pd.DataFrame(results)
        
        # Duplicate removal
        df.drop_duplicates(inplace=True)
        
        # Save to CSV
        output_path = os.path.join(os.path.dirname(__file__), 'linkedin_jobs.csv')
        df.to_csv(output_path, index=False)
        print(f"Scraped {len(df)} jobs. Saved to {output_path}")
        
    finally:
        scraper.close()
