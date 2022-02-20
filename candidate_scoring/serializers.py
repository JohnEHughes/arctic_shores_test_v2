from rest_framework_json_api import serializers
from candidate_scoring.models import Candidate, Score


"""
Serializers created for the two models

"""

class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'candidate_ref')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('candidate_ref', 'score')

