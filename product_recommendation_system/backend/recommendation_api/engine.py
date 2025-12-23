import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import os

# Sample product data
products_data = [
    {"id": 1, "name": "Wireless Headphones", "category": "Electronics", "description": "High-quality wireless headphones with noise cancellation."},
    {"id": 2, "name": "Running Shoes", "category": "Sports", "description": "Lightweight running shoes for professional athletes."},
    {"id": 3, "name": "Coffee Maker", "category": "Home", "description": "Programmable coffee maker with thermal carafe."},
    {"id": 4, "name": "Smart Watch", "category": "Electronics", "description": "Water-resistant smart watch with heart rate monitor."},
    {"id": 5, "name": "Yoga Mat", "category": "Sports", "description": "Eco-friendly yoga mat with non-slip surface."},
    {"id": 6, "name": "Blender", "category": "Home", "description": "High-speed blender for smoothies and shakes."},
    {"id": 7, "name": "Bluetooth Speaker", "category": "Electronics", "description": "Portable bluetooth speaker with extra bass."},
    {"id": 8, "name": "Hiking Boots", "category": "Sports", "description": "Durable hiking boots for all terrains."},
    {"id": 9, "name": "Air Fryer", "category": "Home", "description": "Compact air fryer for healthy cooking."},
    {"id": 10, "name": "Laptop Stand", "category": "Electronics", "description": "Ergonomic laptop stand with adjustable height."},
]

df = pd.DataFrame(products_data)

def get_recommendations(product_name, num_recommendations=3):
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(df['description'])
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
    
    indices = pd.Series(df.index, index=df['name']).drop_duplicates()
    
    if product_name not in indices:
        return []

    idx = indices[product_name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]
    
    product_indices = [i[0] for i in sim_scores]
    return df.iloc[product_indices].to_dict('records')
