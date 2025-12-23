# Report: Product Recommendation System

## Introduction
The Product Recommendation System is a full-stack application that provides personalized product suggestions based on user interests. It leverages machine learning algorithms to analyze product descriptions and find similarities.

## Abstract
Modern e-commerce platforms rely heavily on recommendation engines to improve user engagement. This project implements a content-based filtering system using TF-IDF vectorization and Cosine Similarity. The system identifies products with similar descriptions to provide relevant suggestions. The backend is powered by Django, while the frontend is built with React for a dynamic shopping experience.

## Tools Used
- **Backend**: Django, Django REST Framework, Scikit-learn, Pandas, NumPy.
- **Frontend**: React (Vite), Axios.
- **Language**: Python, JavaScript.

## Steps Involved in Building the Project
1. **Dataset Preparation**: Created a sample dataset of products across various categories like Electronics, Sports, and Home.
2. **Recommendation Engine**:
   - Used `TfidfVectorizer` from Scikit-learn to convert product descriptions into numerical vectors.
   - Calculated `Cosine Similarity` between product vectors to find the most relevant matches.
3. **API Development**:
   - Implemented logic to list all available products and fetch recommendations for a selected product.
   - Created DRF endpoints for seamless data flow.
4. **Frontend Development**:
   - Built a grid-based UI in React to display available products.
   - Implemented a details panel that updates dynamically with recommendations when a product is clicked.
5. **Testing**: Verified the accuracy of recommendations using different product types.

## Conclusion
The recommendation system effectively suggests relevant products based on their descriptions. This project demonstrates how machine learning can be integrated into a web application to enhance user experience and provide personalized content.
