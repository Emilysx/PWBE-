import django_filters as df
from django.db.models import Q
from .models import Autor

class AutoFilter(df.FilterSet):
    nome = df.CharFilter(method='filter_nome')
    nascion = df.CharFilter(method='nascion', lookup_expr='iexact')

    def filter_nome(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nome__icontains = value) | Q (sobrenome__icontains = value))

    def nascionalidade(self, qs, name, value: str):
        if not value:
            return qs
        return qs.filter(Q(nascion__icontains = value))


    class Meta:
        model = Autor
        fields = []

