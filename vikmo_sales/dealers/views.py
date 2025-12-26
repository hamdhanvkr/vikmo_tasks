from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def test_api(request):
    if request.method == 'GET':
        return Response({
            "message": "GET request successful",
            "status": "ok"
        })
        

    if request.method == 'POST':
        data = request.data
        print("Received data:", data.name)
        return Response({
            "message": "POST request successful",
            "received_data": data
        }, status=status.HTTP_201_CREATED)
