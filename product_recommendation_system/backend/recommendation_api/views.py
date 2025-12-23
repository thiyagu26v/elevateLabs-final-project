from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .engine import get_recommendations, df

class ProductListView(APIView):
    def get(self, request):
        return Response(df.to_dict('records'), status=status.HTTP_200_OK)

class RecommendationView(APIView):
    def post(self, request):
        product_name = request.data.get('product_name')
        if not product_name:
            return Response({'error': 'Product name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        recommendations = get_recommendations(product_name)
        return Response(recommendations, status=status.HTTP_200_OK)
