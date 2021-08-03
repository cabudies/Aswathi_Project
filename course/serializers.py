from rest_framework import serializers
from .models import Degree

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = "__all__"
