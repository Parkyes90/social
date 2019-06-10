from rest_framework import serializers

from core.serializers import AuthorAndCreateAtSerializer
from questions.models import Answer, Question


# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,Pylint
class AnswerSerializer(AuthorAndCreateAtSerializer):
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ["question", "voters", "updated_at"]

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()


# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,Pylint
class QuestionSerializer(AuthorAndCreateAtSerializer):
    slug = serializers.SlugField(read_only=True)
    answers_count = serializers.SerializerMethodField()
    user_has_answered = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ["updated_at"]

    def get_answers_count(self, instance):
        return instance.answer.count()

    def get_user_has_answered(self, instance):
        request = self.context.get("request")
        return instance.answer.filter(author=request.user).exists()
