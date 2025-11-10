# solar_databricks

Repositório de orquestração e pipelines (Databricks/Spark) que integram séries de geração solar com dados meteorológicos. Este projeto centraliza notebooks e jobs que fazem ingestão, preparação (_silver_) e modelagem (_gold_) para experimentos e automação.

## Repositórios Relacionados
- Solar (modelagem e utilitários de séries solares): https://github.com/lksprado/Solar
- OpenWeather (cliente/integração para dados meteorológicos): https://github.com/lksprado/openweather

Use este repositório como “cola” entre os dois acima: consome clima (OpenWeather) e combina com geração/experimentos (Solar) dentro de uma pipeline executável em Databricks.

## Estrutura do Projeto
- `solar_clima_pipeline/_silver/`
  - Notebooks de preparação de dados (SVR diário/horário para energia e clima).
- `solar_clima_pipeline/gold/solar_and_weather_model.py`
  - Script/experimento que junta dados de geração solar com clima para modelagem em nível “gold”.

## Pré‑requisitos
- Python 3.9+ (ou Databricks Runtime compatível)
- Spark/Databricks (para execução distribuída)
- Dependências usuais para modelagem (ex.: `pyspark`, `pandas`, `scikit-learn`) conforme seus ambientes/notebooks.
- Credenciais/variáveis de acesso para a API do OpenWeather (conforme o repositório `openweather`).

## Como Usar
1) Obtenha/ingira dados meteorológicos com base no repo `openweather` (defina chaves e endpoints conforme a documentação de lá).
2) Padronize/preparen os dados solares/utilitários com o repo `Solar` quando necessário.
3) Execute os notebooks em `_silver/` para gerar camadas intermediárias.
4) Rode o experimento de junção/modelagem em `_gold/`:
   - Local/CLI (exemplo):
     - `python solar_clima_pipeline/gold/solar_and_weather_model.py`
   - Databricks:
     - Importe notebooks/arquivos, configure um Job e parâmetros (paths de entrada/saída, chaves OpenWeather, etc.).

## Notas de Integração
- Paths e esquemas de dados devem ser alinhados entre os três repositórios.
- Armazéns (bronze/silver/gold) podem ser pastas locais, DBFS ou catálogos do Lakehouse; ajuste no código/notebooks conforme seu ambiente.
- Para automação, considere criar um Job no Databricks que:
  - Ingesta clima (OpenWeather) → prepara (_silver_) → treina/avalia (_gold_).

## Próximos Passos
- Documentar parâmetros/flags do `solar_and_weather_model.py` quando estabilizados.
- Adicionar exemplos mínimos de entrada/saída e amostras de dataset.
- Incluir arquivos de ambiente (ex.: `requirements.txt` ou `environment.yml`) alinhados com Databricks.

## Licença
Defina a licença de uso conforme a necessidade do projeto.
