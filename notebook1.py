# Databricks notebook source
from datetime import datetime
dbutils.widgets.text("foo", "bar")
foo = dbutils.widgets.get("foo")

# COMMAND ----------

today = datetime.today()

# COMMAND ----------

print(foo)
print(today)
