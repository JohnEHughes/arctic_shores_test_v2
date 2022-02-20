from django.db import models
from django.core.exceptions import ValidationError

"""
2x models created:
Candidate
Score
"""


# Validator method to check the reference string argument meets the formatting requirements
def validator_ref(value):
    if len(value) != 8:             # Check if the string is 8 in length
        raise ValidationError("Reference must be 8 chars in length!")
    else:
        count = 0
        for i in value:              # iterate the string and check unicode if it is (a-zA-Z0-9)
            if (57 >= ord(i) >= 48) or (90 >= ord(i) >= 65) or (122 >= ord(i) >= 97):
                count += 1
                if count == 8:
                    return value
            else:
                raise ValidationError("Reference must be only letters and numbers!")


# Validator to check if the score variable is between 0 and 100
def validate_score(value):
    if 0 <= value <= 100:
        return value
    else:
        raise ValidationError("Score must be between 0 and 100!")


"""
Candidate model - two fields - name and candidate_ref
candidate_ref must be unique and checked with the above validator_ref()
"""
class Candidate(models.Model):
    name = models.CharField('Candidate Name', max_length=60)
    candidate_ref = models.CharField('Candidate Reference', unique=True,  max_length=8, validators =[validator_ref])

    def __str__(self):
        return self.name


"""
Score model - two fields - candidate_ref and score
candidate_ref -checked with the above validate_score() and is used as the relationship foreignkey

"""
class Score(models.Model):
    candidate_ref = models.ForeignKey(Candidate, default=None, on_delete=models.CASCADE)
    score = models.FloatField('Candidate Score', validators=[validate_score])
