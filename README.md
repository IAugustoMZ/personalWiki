# Personal Knowledge Wiki

Repositório pessoal de anotações de estudo, questões de revisão e diagramas de apoio. Os materiais estão organizados por curso e, dentro de cada curso, por notas Markdown datadas e numeradas.

## Navegação

- [Cursos](courses/README.md) — trilhas de Power BI e engenharia de dados.
- [Certificações](certifications/README.md) — notas e recursos para certificações profissionais (Databricks, etc).
- [Artefatos](artifacts/README.md) — diagramas e imagens referenciados pelas notas.
- [Questões](questions/README.md) — bancos de perguntas para revisão.
- [Idiomas](languages/README.md) — anotações de estudo de espanhol, chinês e japonês.

## Ambiente

O repositório inclui `Dockerfile` e `docker-compose.yml` para um ambiente Python 3.11. As dependências estão listadas em `requirements.txt`.

## Criando Novas Entradas

Use o Makefile para criar novas entradas facilmente:

```bash
make new-entry
```

O script interativo guiará você por:
1. Seleção da pasta de destino
2. Detecção da última entrada numerada
3. Entrada da data em `DDMMYYYY`
4. Criação da nova nota baseada no template anterior

## Site de Documentação

As notas podem ser lidas como site, com busca e navegação, usando MkDocs com o tema Material:

```bash
poetry install --with docs
make docs          # http://127.0.0.1:8000, recarrega ao salvar
make docs-build    # build estrito: falha em links quebrados
```

Sem `make`, use diretamente `poetry run mkdocs serve` e `poetry run mkdocs build --strict`.

A navegação é gerada automaticamente por `wiki_nav.py`, que encontra os READMEs e todas as notas Markdown nas pastas de conteúdo; `mkdocs.yml` configura o site e carrega esse hook. Os links relativos funcionam igual no GitHub e no site (`docs_dir: .` com o plugin `same-dir`). O tema é escuro, com paleta azul, prata e cinza definida em `stylesheets/tech.css`.

## Convenções

- As notas seguem o padrão `NN_<sigla>_DDMMYYYY.md`, preservando a sequência de estudo.
- As imagens ficam em `artifacts/` e são referenciadas pelas notas com caminhos relativos.
- Cada pasta de conteúdo possui um README próprio com seu escopo e atalhos de navegação.
