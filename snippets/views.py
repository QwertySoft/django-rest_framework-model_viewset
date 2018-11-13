from rest_framework import viewsets # Importamos el modulo de viewsets
from snippets.serializers import SnippetSerializer # Importamos el serializador de snippets
from snippets.models import Snippet # Importamos el modelo Snippet

class SnippetViewSet(viewsets.ModelViewSet): # Definimos una vista de tipo model
    """
    API endpoint that allows retrieve all snippets.
    """
    queryset = Snippet.objects.all() # Indicamos el QuerySet para listar todos los snippets
    serializer_class = SnippetSerializer # Definimos que seralizador usar para transformar los datos devueltos por el QuerySet a JSON