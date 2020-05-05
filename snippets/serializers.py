"""We need a way of serializing and deserializing the snippet instances into representations such as json"""

from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

"""
Test the abstraction using following methods, 
from snippets.serializers import SnippetSerializer
serializer = SnippetSerializer()
print(repr(serializer))

"""


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']



