from candidate_scoring.models import Candidate, Score
from candidate_scoring.serializers import CandidateSerializer, ScoreSerializer
from rest_framework import views, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view




class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class ScoreViewSet(viewsets.ModelViewSet):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


# class CandidateDataViewSet(viewsets.ModelViewSet):
#     queryset = Score.objects.all().union(Candidate.objects.all())
#     serializer_class = CandidateDataSerializer