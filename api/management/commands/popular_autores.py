import pandas as pd
from django.core.management.base import BaseCommand # Onde vamos pegar os comandos
from django.db import transaction
from api.models import Autor # A tabela que vamos popular

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/autores.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        # DataFrame é como uma tabela virtual
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]
       
        if o['truncate']: Autor.objects.all().delete()

        # Essa linha serve para padronizar a columa 'nome'
        df["nome"] = df["nome"].astype(str).str.strip()
        df["sobrenome"] = df["sobrenome"].astype(str).str.strip()

        df["data_nasc"] = pd.to_datetime(df["data_nasc"], errors="coerce", format = "%Y-%m-%d").dt.date

        #
        df["nascion"] = df.get("nascion", "").astype(str).str.strip().str.capitalize().replace({"":None})
        
        # Está eliminando do DataFrame todas as linhas onde nome ou sobrenome estão vazios.
        df = df.query("nome != '' and sobrenome != '' ")

        # Está excluindo as colunas que estão em brancos
        df = df.dropna(subset=['data_nasc'])

        if o['update']:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
               _, created =  Autor.objects.update_or_create(
                   nome = r.nome, sobrenome = r.sobrenome, data_nasc = r.data_nasc,
                   defaults={"nascion": r.nascion}
               )

               criados += int(created)
               atualizados += (not created)

            self.stdout.write(self.style.SUCCESS(f'Criados: {criados} | Atualizados: {atualizados}'))
        else:
            objs = [Autor(
                nome = r.nome, sobrenome = r.sobrenome, data_nasc = r.data_nasc, nascion = r.nascion
            ) for r in df.itertuples(index=False)]

            Autor.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Criados: {len(objs)}'))
            
            