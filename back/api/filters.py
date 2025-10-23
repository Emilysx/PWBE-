import django_filters as df
from django.db.models import Q
from .models import Autor
from .models import Livro

class LivroFilter(df.FilterSet):
    id = df.NumberFilter(field_name='id', lookup_expr='exact')
    titulo = df.CharFilter(field_name='titulo', lookup_expr='icontains')
    autor = df.CharFilter(method='filter_autor')

    def filter_autor(self, qs, name, value):
        if not value:
            return qs
        return qs.filter(Q(autor__nome__icontains=value) | Q(autor__sobrenome__icontains=value))

    class Meta:
        model = Livro
        fields = []


class AutorFilter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nascion = df.CharFilter(field_name='nascion', lookup_expr='iexact')

    def filter_nome(self, ps, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nome__icontains=value) | Q(nascion__icontains=value))

    class Meta:
        model = Autor
        fields = []