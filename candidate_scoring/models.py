from django.db import models
from django.core.exceptions import ValidationError



def validator_ref(value):
    if len(value) != 8:
        raise ValidationError("Reference must be 8 chars in length!")
    else:
        count = 0
        for i in value:
            if (57 >= ord(i) >= 48) or (90 >= ord(i) >= 65) or (122 >= ord(i) >= 97):
                count += 1
                if count == 8:
                    return value
            else:
                raise ValidationError("Reference must be only letters and numbers!")


def validate_score(value):
    if 0 <= value <= 100:
        return value
    else:
        raise ValidationError("Score must be between 0 and 100!")



class Candidate(models.Model):
    name = models.CharField('Candidate Name', max_length=60)
    candidate_ref = models.CharField('Candidate Reference', unique=True,  max_length=8, validators =[validator_ref])

    def __str__(self):
        return self.name



class Score(models.Model):
    candidate_ref = models.ForeignKey(Candidate, default=None, on_delete=models.CASCADE)
    score = models.FloatField('Candidate Score', validators=[validate_score])
