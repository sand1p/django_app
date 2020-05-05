from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

"""The root of our API is to list all existing snippets or to create new snippet 
Note that because we want to be able to POST to this view from clients that won't have a CSRF token
we need to mark the view as csrf_exempt. This isn't something that you'd normally want to do,
and REST framework views actually use more sensible behavior than this,
but it'll do for our purposes right now.
"""


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets or create new code snippet.
    :param request:
    :return:
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
