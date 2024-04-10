from pyspark.sql.session import SparkSession
from pyspark.sql.types import Row

# We need the session before we can use @udf
spark = SparkSession.builder.master("local[4]").getOrCreate()

df1 = spark.createDataFrame([Row("timbit"), Row("amigo")], ["names"])
df2 = spark.createDataFrame(
    [Row("timbit", "san francisco"), Row("amigo", "ottawa")],
    ["names", "place"])

df2.select(df2['names'],
           # Note we use == and != in Python versus === & !== in Scala
           df2['names'] == df2['names'],
           df2['names'] != df2['names']).show()
