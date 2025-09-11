import pandas as pd
from django.core.management.base import BaseCommand # Onde vamos pegar os comandos
from django.db import transaction
from api.models import Livro # A tabela que vamos popular
class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--arquivo", default="population/livros.csv")
        parser.add_argument("--truncate", action="store_true")
        parser.add_argument("--update", action="store_true")

    @transaction.atomic
    def handle(self, *a, **o):
        # DataFrame é como uma tabela virtual
        df = pd.read_csv(o["arquivo"], encoding="utf-8-sig")
        df.columns = [c.strip().lower().lstrip("\ufeff") for c in df.columns]
       
        if o['truncate']: Livro.objects.all().delete()

        # Essa linha serve para padronizar a columa 'titulo'
        df["titulo"] = df["titulo"].astype(str).str.strip()
        df["subtitulo"] = df["subtitulo"].astype(str).str.strip()

        df["autor"] = df["autor"].astype(str).str.strip()
        df["editora"] = df["editora"].astype(str).str.strip()

        df["descricao"] = df["descricao"].astype(str).str.strip()
        df["idioma"] = df["idioma"].astype(str).str.strip()
        df["ano_pub"] = pd.to_numeric(df["ano_pub"], errors="coerce", downcast="integer")
    
        
        df["paginas"] = pd.to_numeric(df["paginas"], errors="coerce", downcast="integer")
        df["preco"] = pd.to_numeric(df["preco"], errors="coerce", downcast="integer")
        df["estoque"] = pd.to_numeric(df["estoque"], errors="coerce", downcast="integer")
        df["desconto"] = pd.to_numeric(df["desconto"], errors="coerce", downcast="integer")


        df["disponivel"] = df["disponivel"].map({"True": True, "False": False})
        df["dimensoes"] = pd.to_numeric(df["dimensoes"], errors="coerce", downcast="integer")
        df["peso"] = pd.to_numeric(df["peso"], errors="coerce", downcast="integer")
        
        # Fiz hoje - 11/09
        criados = 0
        for r in df.itertuples(index=False):
            # Pega ou cria o autor
            autor_obj, _ = Autor.objects.get_or_create(
                nome=r.autor  # aqui r.autor já vem da coluna do CSV
            )
    
            # Pega ou cria a editora
            editora_obj, _ = Editora.objects.get_or_create(
                nome=r.editora
            )
            criados += int(created)
            self.stdout.write(self.style.SUCCESS(f"Livros criados: {criados}"))

        
        # Está eliminando do DataFrame todas as linhas onde nome ou sobrenome estão vazios.
        df = df.query("titulo != '' and subtitulo != '' ")

        # Está excluindo as colunas que estão em brancos
        df = df.dropna(subset=['ano'])

        if o['update']:
            criados = atualizados = 0
            for r in df.itertuples(index=False):
               _, created =  Livro.objects.update_or_create(
                   titulo = r.titulo, subtitulo = r.subtitulo, ano = r.ano,
                   defaults={"nascion": r.nascion}
               )

               criados += int(created)
               atualizados += (not created)

            self.stdout.write(self.style.SUCCESS(f'Criados: {criados} | Atualizados: {atualizados}'))
        else:
            objs = [Livro(
                titulo = r.titulo, subtitulo = r.subtitulo, ano = r.ano, nascion = r.nascion
            ) for r in df.itertuples(index=False)]

            Livro.objects.bulk_create(objs, ignore_conflicts=True)
            self.stdout.write(self.style.SUCCESS(f'Criados: {len(objs)}'))
            

