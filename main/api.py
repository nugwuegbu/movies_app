"""
Movies API for loading data when user sends  requests
Accepts data from Rest client like JS
"""

import json

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import MovieSerializer
from main.sparql_util import SparqlUtil
from main.fixed_constants import data_url,query


class MovieAPIView(APIView,SparqlUtil):
    """API for user request to load movies to DB"""

    permission_classes = [permissions.IsAuthenticated,]

    def get(self,request):
        self.user = request.user
        self.query = query
        self.data_url = data_url
        data = self.data_result()
        return Response(data,status=status.HTTP_200_OK)