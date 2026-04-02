# test_datetime_utils.py


import datetime
from src.utils.datetime_utils import timestamp_to_date_col


def test_timestamp_to_date_col(spark):
    spark.conf.set("spark.sql.session.timeZone", "UTC")

    # Create a DataFrame with a known timestamp column using a datetime object
    data = [(datetime.datetime(2026, 4, 2, 10, 30, 0),)]
    schema = "ride_timestamp timestamp"
    df = spark.createDataFrame(data, schema=schema)

    # Use the utility to add a date column
    result_df = timestamp_to_date_col(spark, df, "ride_timestamp", "ride_date")

    # Assert that the extracted date matches the expected value
    row = result_df.select("ride_date").first()

    expected_date = datetime.date(2026, 4, 2)  # Expected: 2026-04-02

    assert row["ride_date"] == expected_date
