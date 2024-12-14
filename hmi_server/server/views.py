from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Text
from .serializers import TextSerializer

class TextView(APIView):
    def get(self, request):
        """
        Retrieve the most recently posted record.
        """
        try:
            latest_record = Text.objects.latest('id')  # Get the latest record by 'created_at'
            serializer = TextSerializer(latest_record)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Text.DoesNotExist:
            return Response({"message": "No records found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        """
        Create a new record.
        """
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
