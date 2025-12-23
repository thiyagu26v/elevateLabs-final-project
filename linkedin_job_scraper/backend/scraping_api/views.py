from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .scraper import LinkedInScraper
import pandas as pd
import os

class ScrapeJobsView(APIView):
    def post(self, request):
        keywords = request.data.get('keywords', 'Python Developer')
        location = request.data.get('location', 'India')
        num_jobs = int(request.data.get('num_jobs', 10))

        scraper = LinkedInScraper()
        try:
            results = scraper.scrape_jobs(keywords, location, num_jobs=num_jobs)
            df = pd.DataFrame(results)
            df.drop_duplicates(inplace=True)
            
            # Save to CSV (optional, but good for persistence)
            csv_path = os.path.join(os.path.dirname(__file__), 'linkedin_jobs.csv')
            df.to_csv(csv_path, index=False)
            
            return Response(results, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        finally:
            scraper.close()

class GetVisualizationView(APIView):
    def get(self, request):
        # In a real app, we'd serve the image file or base64
        # For this task, we'll return the company counts as JSON for the frontend to chart
        csv_path = os.path.join(os.path.dirname(__file__), 'linkedin_jobs.csv')
        if not os.path.exists(csv_path):
            return Response({'error': 'No data found. Scrape first.'}, status=status.HTTP_404_NOT_FOUND)
        
        df = pd.read_csv(csv_path)
        company_counts = df['Company'].value_counts().head(10).to_dict()
        return Response(company_counts, status=status.HTTP_200_OK)
