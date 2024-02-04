from rest_framework import serializers

from lms_service.models import Course, Lesson
from lms_service.serializers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):
    # paid_course = serializers.PrimaryKeyRelatedField(required=False)
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(read_only=True)

    def get_lessons_count(self, obj):
        lessons_count = obj.lessons.count()
        return lessons_count

    def update(self, instance, validated_data):
        course = Course.objects.get(pk=instance.id)
        Course.objects.filter(pk=instance.id).update(**validated_data)


        return instance

    class Meta:
        model = Course
        fields = "__all__"
