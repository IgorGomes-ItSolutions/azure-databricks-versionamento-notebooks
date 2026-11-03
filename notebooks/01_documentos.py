# Databricks notebook source
# MAGIC %md
# MAGIC # Documentos fictícios: Python, SQL e PySpark
# MAGIC Projeto de organização e versionamento. Nenhum registro representa uma pessoa ou operação real.
# MAGIC Execute as células em ordem. Importe também `data/documentos.csv`, preservando a estrutura do repositório.
# MAGIC Código preparado com auxílio de IA e revisado por regras e verificações explícitas.

# COMMAND ----------
import csv
from pathlib import Path
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, StringType

dbutils.widgets.text("limite", "30", "Quantidade mínima (exclusiva)")
dbutils.widgets.text("arquivo_csv", "../data/documentos.csv", "Caminho do CSV no workspace")
limite = int(dbutils.widgets.get("limite"))
caminho = Path(dbutils.widgets.get("arquivo_csv")).resolve()
with caminho.open(encoding="utf-8", newline="") as arquivo:
    registros = list(csv.DictReader(arquivo))
schema = StructType([StructField(nome, StringType(), True)
                     for nome in ["id", "documento", "quantidade"]])
bruto = spark.createDataFrame(registros, schema)
display(bruto)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Qualidade dos dados
# MAGIC Python carrega o arquivo e os parâmetros. PySpark transforma as colunas distribuídas.
# MAGIC `try_cast` retorna nulo quando um texto não pode ser convertido. Rejeitamos campos inválidos.
# MAGIC Duplicatas idênticas são removidas; IDs com conteúdos diferentes interrompem a execução.

# COMMAND ----------
tipado = bruto.selectExpr("try_cast(id as int) as id", "trim(documento) as documento",
                          "try_cast(quantidade as int) as quantidade")
regra = (F.col("id").isNotNull() & (F.col("id") > 0)
         & F.col("documento").isNotNull() & (F.length("documento") > 0)
         & F.col("quantidade").isNotNull() & (F.col("quantidade") >= 0))
rejeitados = tipado.filter(~F.coalesce(regra, F.lit(False)))
candidatos = tipado.filter(regra).dropDuplicates()
conflitos = candidatos.groupBy("id").count().filter(F.col("count") > 1)
assert conflitos.count() == 0, "ID conflitante: revise os dados antes de continuar"
documentos = candidatos
documentos.createOrReplaceTempView("documentos_versionamento_lab")
print({"brutos": bruto.count(), "válidos": documentos.count(),
       "rejeitados": rejeitados.count(),
       "duplicatas": tipado.filter(regra).count() - documentos.count()})
display(rejeitados)

# COMMAND ----------
# Filtro equivalente à condição WHERE quantidade > limite em SQL.
filtrados = documentos.filter(F.col("quantidade") > limite).orderBy(F.desc("quantidade"))
display(filtrados)

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT documento, quantidade
# MAGIC FROM documentos_versionamento_lab
# MAGIC WHERE quantidade > 30
# MAGIC ORDER BY quantidade DESC;

# COMMAND ----------
# MAGIC %sql
# MAGIC SELECT COUNT(*) AS tipos_documentos, SUM(quantidade) AS total_documentos,
# MAGIC        ROUND(AVG(quantidade), 2) AS media_por_tipo
# MAGIC FROM documentos_versionamento_lab;

# COMMAND ----------
# Comparação das duas APIs usando o mesmo parâmetro, sem interpolar texto SQL.
resultado_sql = spark.sql("SELECT documento, quantidade FROM documentos_versionamento_lab")
resultado_sql = resultado_sql.filter(F.col("quantidade") > limite)
assert set(map(tuple, resultado_sql.collect())) == set(map(tuple, filtrados.select("documento", "quantidade").collect()))
assert documentos.count() == 6
assert rejeitados.count() == 2
assert documentos.agg(F.sum("quantidade")).first()[0] == 194
print("Verificações concluídas: 6 tipos, total 194; SQL e PySpark equivalentes.")

# COMMAND ----------
import matplotlib.pyplot as plt
linhas = documentos.orderBy(F.desc("quantidade")).collect()
fig, ax = plt.subplots(figsize=(10, 4))
ax.barh([x.documento for x in linhas], [x.quantidade for x in linhas], color="#147d92")
ax.invert_yaxis()
ax.set_xlabel("Quantidade fictícia")
ax.set_title("Documentos por tipo — laboratório")
fig.tight_layout()
display(fig)
plt.close(fig)

# COMMAND ----------
# MAGIC %md
# MAGIC ## Interpretação e versionamento
# MAGIC Os três tipos acima de 30 somam 130 documentos (67,01% dos 194).
# MAGIC Alterações na lista Python original não alteram um DataFrame já criado.
# MAGIC Uma view temporária pertence à sessão: execute novamente após reiniciar o compute.
# MAGIC Faça alterações numa branch, revise o diff e os testes antes de promover para main.
# MAGIC Não exporte tokens, resultados reais ou credenciais. Encerre o compute ao terminar.
