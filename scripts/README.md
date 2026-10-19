# Scripts

Utilidades para gerenciar o repositório da wiki pessoal.

## new_entry.sh

Script interativo para criar novas entradas de notas Markdown.

### Uso

```bash
./new_entry.sh
```

Ou via Makefile:

```bash
make new-entry
```

### Funcionalidade

- Navega interativamente pela estrutura de pastas
- Identifica a última entrada numerada na pasta selecionada
- Valida o padrão de nomenclatura: `NN_<sigla>_DDMMYYYY.md`
- Clona o template anterior para a nova nota
- Incrementa o número da sequência automaticamente
- Solicita a data da nova entrada no formato `DDMMYYYY`

### Exemplo de Uso

```
== Select folder inside: (root) ==
  1) certifications
  2) courses
  3) languages
  4) questions
Select an option: 2

== Select folder inside: courses ==
  0) .. (go up)
  1) data_engineer_formation
Select an option: 1

== Select folder inside: courses/data_engineer_formation ==
  0) .. (go up)
  1) pyspark_kafka_processamento_batch_streaming
Select an option: 1

Target folder: courses/data_engineer_formation/pyspark_kafka_processamento_batch_streaming
Last entry: 12_def_spkbst_25102025.md
Next number: 13
Enter the entry date (DDMMYYYY): 26102025
Created: courses/data_engineer_formation/pyspark_kafka_processamento_batch_streaming/13_def_spkbst_26102025.md
```
