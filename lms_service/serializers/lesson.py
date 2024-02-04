from rest_framework import serializers

from lms_service.models import Lesson
from lms_service.validators import valid_url


class LessonSerializer(serializers.ModelSerializer):
    # paid_lesson = serializers.PrimaryKeyRelatedField(required=False, read_only=True)
    link = serializers.URLField(validators=[valid_url])

    class Meta:
        model = Lesson
        fields = "__all__"


