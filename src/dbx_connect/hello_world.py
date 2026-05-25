from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Initialize Spark session
    spark = SparkSession.builder.appName("HelloWorldApp").getOrCreate()

    # Create a simple DataFrame
    data = [(1, "Hello"), (2, "World")]
    columns = ["id", "word"]
    df = spark.createDataFrame(data, columns)

    # Show the DataFrame
    display(df)

    # Stop the Spark session
    spark.stop()
