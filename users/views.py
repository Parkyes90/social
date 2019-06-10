from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):
    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
