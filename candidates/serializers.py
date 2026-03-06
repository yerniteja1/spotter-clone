from rest_framework import serializers
from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):
    score_label = serializers.SerializerMethodField()

    class Meta:
        model  = Candidate
        fields = [
            'id', 'name', 'email', 'years_experience',
            'skills', 'score', 'score_label', 'applied_at', 'updated_at'
        ]
        read_only_fields = ['score', 'score_label', 'applied_at', 'updated_at']

    def get_score_label(self, obj):
        if obj.score >= 80: return "Strong"
        if obj.score >= 60: return "Good"
        if obj.score >= 40: return "Average"
        return "Weak"