# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS  bronze

# COMMAND ----------

df = spark.read.format("json").load('s3://solar-weather/bronze/').select("*","_metadata.file_name")
df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("bronze.solar_production")
display(df)
