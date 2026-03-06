from django.contrib import admin
from .models import Candidate

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display  = ['name', 'email', 'years_experience', 'score', 'applied_at']
    list_filter   = ['years_experience']
    search_fields = ['name', 'email']
    ordering      = ['-score']