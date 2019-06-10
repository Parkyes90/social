# noinspection PyMethodMayBeStatic,PyMethodMayBeStatic,Pylint
from rest_framework import serializers


# noinspection PyMethodMayBeStatic,Pylint
class AuthorAndCreateAtSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()

    def get_created_at(self, instance):
        return instance.created_at.strftime("%B %d, %Y")
