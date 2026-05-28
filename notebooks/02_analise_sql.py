# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * 
# MAGIC FROM igpm_historico
# MAGIC LIMIT 10

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     ano,
# MAGIC     ROUND(SUM(valor), 2) as valor_total
# MAGIC FROM igpm_historico
# MAGIC GROUP BY ano
# MAGIC ORDER BY ano ASC

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH acumulado_ano AS (
# MAGIC     SELECT    
# MAGIC         ano,
# MAGIC         ROUND(SUM(valor), 2) as valor_total
# MAGIC     FROM igpm_historico
# MAGIC     GROUP BY ano
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     ano,
# MAGIC     valor_total
# MAGIC FROM acumulado_ano
# MAGIC WHERE valor_total > 10.0
# MAGIC ORDER BY ano ASC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC WITH acumulado_ano AS (
# MAGIC     SELECT    
# MAGIC         ano,
# MAGIC         ROUND(SUM(valor), 2) as valor_total
# MAGIC     FROM igpm_historico
# MAGIC     GROUP BY ano
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     ano,
# MAGIC     valor_total,
# MAGIC     LAG(valor_total) OVER(ORDER BY ano) AS ano_anterior,
# MAGIC     ROUND(valor_total - ano_anterior, 2)  AS variacao
# MAGIC FROM acumulado_ano
# MAGIC ORDER BY ano ASC

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE OR REPLACE TABLE classificacao_ano AS
# MAGIC
# MAGIC WITH acumulado_ano AS (
# MAGIC     SELECT    
# MAGIC         ano,
# MAGIC         ROUND(SUM(valor), 2) as valor_total
# MAGIC     FROM igpm_historico
# MAGIC     GROUP BY ano
# MAGIC )
# MAGIC
# MAGIC SELECT
# MAGIC     ano,
# MAGIC     valor_total,
# MAGIC     CASE 
# MAGIC         WHEN valor_total > 10.0 THEN 'Alta inflação'
# MAGIC         WHEN valor_total < 0.0 THEN 'Deflação'
# MAGIC         ELSE 'Inflação moderada'
# MAGIC     END AS classificacao
# MAGIC FROM acumulado_ano
# MAGIC ORDER BY ano ASC

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC SELECT * FROM classificacao_ano

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC     ih.data,
# MAGIC     ih.mes,
# MAGIC     ih.ano,
# MAGIC     ih.valor,
# MAGIC     ca.classificacao
# MAGIC FROM igpm_historico AS ih
# MAGIC JOIN classificacao_ano as ca ON ih.ano = ca.ano
# MAGIC ORDER BY data

# COMMAND ----------

# MAGIC %md
# MAGIC