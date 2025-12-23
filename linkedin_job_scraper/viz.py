import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_visualization(csv_file):
    if not os.path.exists(csv_file):
        print("CSV file not found.")
        return

    df = pd.read_csv(csv_file)
    
    if df.empty:
        print("CSV is empty.")
        return

    # Visualize job frequency by company
    plt.figure(figsize=(12, 6))
    company_counts = df['Company'].value_counts().head(10)
    sns.barplot(x=company_counts.values, y=company_counts.index, palette='viridis')
    plt.title('Top 10 Companies by Job Postings')
    plt.xlabel('Number of Jobs')
    plt.ylabel('Company')
    
    viz_path = os.path.join(os.path.dirname(csv_file), 'job_frequency.png')
    plt.tight_layout()
    plt.savefig(viz_path)
    print(f"Visualization saved to {viz_path}")

if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), 'linkedin_jobs.csv')
    create_visualization(csv_path)
