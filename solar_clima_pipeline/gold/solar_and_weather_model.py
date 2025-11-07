import dlt
from pyspark.sql.functions import col

@dlt.table(
    name="energia_clima_gld",
    comment="Tabela Gold com join entre consumo diário e clima"
)
def create_gold_table():
    df_clima = dlt.read("silver.fct_daily_weather")
    df_kwh = dlt.read("silver.fct_daily_kwh")
    
    df_join = df_clima.join(df_kwh, on="date", how="inner")
    
    return df_join
