from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student


# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'student-list' : '/student-list/',
        'Detail' : '/student-list/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def detailView(request,pk):
    students = Student.objects.get(id=pk)  
    serializer = StudentSerializer(students , many = False)
    return Response(serializer.data) 




