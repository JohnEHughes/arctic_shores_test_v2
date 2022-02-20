from rest_framework_json_api import serializers
from candidate_scoring.models import Candidate, Score


class CandidateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Candidate
        fields = ('name', 'candidate_ref')

class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = ('candidate_ref', 'score')


# class CandidateDataSerializer(serializers.HyperlinkedModelSerializer):
#     scores = serializers.SlugRelatedField(many=True, read_only=True, slug_field="scores")
#
#     class Meta:
#         model = Candidate
#         fields = ('name', 'candidate_ref', 'scores')


# from django.db import models
#
# class Artist(models.Model):
#   name = models.CharField(max_length=255)
#
#   def __str__(self):
#     return self.name
#
# class Song(models.Model):
#   name = models.CharField(max_length=255)
#   artist = models.ForeignKey(Artist, related_name="songs", on_delete=models.CASCADE)
#
#   def __str__(self):
#     return self.name
#
#
#
# from rest_framework import serializers
# from .models import Song, Artist
#
# class ArtistSerializer(serialisers.ModelSerializer):
#   songs = serializers.SlugRelatedField(
#     many=True,
#     read_only=True,
#     slug_field="name"
#   )
#
#   class Meta:
#     model = Artist
#     fields = ('id', 'name', 'songs')