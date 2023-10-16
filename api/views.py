from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Question
from .serializers import QuestionSerializer

@api_view(['GET'])
def questions_list(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)
