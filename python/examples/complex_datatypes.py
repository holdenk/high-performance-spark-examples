from pyspark.sql.session import SparkSession
from pyspark.sql.types import Row
from dataclasses import dataclass


# We need the session before we can use @udf
spark = SparkSession.builder.master("local[4]").getOrCreate()

@dataclass(frozen=True)
class Dog:
    name: str
    age: int
    places: dict
    moms: list

df = spark.createDataFrame([
    Dog(
        "timbit",
        4,
        {"park": 100, "vet": -100, "home": 80},
        ["carolyn", "holden"])
])
df.show()
df.printSchema()
