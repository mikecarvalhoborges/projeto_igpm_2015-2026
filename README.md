# Análise do IGP-M 2015-2026
Projeto de análise de dados sobre a evolução do IGP-M (Índice Geral de Preços do Mercado) no Brasil entre 2015 e 2026, utilizando dados reais extraídos via API do Banco Central do Brasil.

## Objetivo
Analisar o comportamento histórico do IGP-M, principal índice de reajuste de aluguéis no Brasil, identificando tendências, comparativos ano vs. ano e classificando os períodos por nível de inflação.

## Tecnologias Utilizadas
| Tecnologia | Uso | 
| --- | --- |
| Python | Consumo de API, tratamento de dados e visualizações |
| pandas | Manipulação e transformação dos dados |
| matplotlib | Gráficos exploratórios |
| Databricks | Processamento com SparkSQL e armazenamento em tabela Delta | 
| SQL | Análises com CTEs, JOINs e Window Functions |
| Power BI | Modelagem Star Schema e dashboard interativo |

## Principais Insights
1. 🔺 Pico histórico na pandemia (2020):
O IGP-M acumulou 21,10% em 2020, o maior valor do período analisado. A combinação de alta do dólar, ruptura nas cadeias de suprimento e aumento de commodities agrícolas pressionou o índice, que tem 60% de peso no atacado (IPA).
2. 📉 Deflação em 2023:
O ano de 2023 registrou -3,18% acumulado, o pior resultado do período. Uma combinação de queda no preço de commodities e apreciação do real derrubou o índice para território negativo, trazendo alívio para inquilinos mas prejuízo para proprietários.
3. 🔺 Nova alta em 2026:
O IGP-M apresenta tendência de alta em 2026, sinalizando possível retomada de pressão inflacionária após dois anos de índices baixos (2024 e 2025).

## Arquitetura do Projeto
[API Banco Central do Brasil]
        ↓
[Python — requests + pandas + matplotlib]
        ↓
[Databricks — SparkSQL + Tabela Delta]
        ↓
[SQL — CTEs, JOINs, Window Functions]
        ↓
[Power BI — Star Schema + Dashboard]

## Fonte dos Dados
Os dados foram extraídos via API pública do Banco Central do Brasil (SGS) — sem necessidade de autenticação.

Série: 189 — IGP-M (FGV)
Período: Janeiro/2015 a Dezembro/2026
Frequência: Mensal
Endpoint: https://api.bcb.gov.br/dados/serie/bcdata.sgs.189/dados


⚠️ Nota: A conexão direta entre Databricks Community Edition e Power BI via JDBC/ODBC não é suportada. Os dados foram exportados em CSV para a conexão com o Power BI. Em ambiente corporativo, essa conexão seria feita diretamente.


## Análises SQL Realizadas

IGP-M acumulado por ano — GROUP BY + SUM
Classificação por período — CASE WHEN
Comparativo ano vs. ano — LAG() Window Function
Variação anual — CTE + cálculo de diferença
Cruzamento com classificação — JOIN entre tabelas
