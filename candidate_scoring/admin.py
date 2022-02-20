from django.contrib import admin
from .models import Candidate, Score

"""
Two views registered with the admin for quick checks

"""


admin.site.register(Candidate)
admin.site.register(Score)

