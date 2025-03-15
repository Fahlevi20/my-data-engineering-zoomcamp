#!/usr/bin/env python
# coding: utf-8


import pandas as pd
from sqlalchemy import create_engine

from time import time

# Membaca file Parquet
df = pd.read_parquet("yellow_tripdata_2024-01.parquet", engine="pyarrow")  # atau "fastparquet"

# Menampilkan beberapa baris pertama
print(df.head())


df.to_csv("yellow_tripdata_2024-01.csv", index=False)

print("Konversi berhasil! File CSV telah disimpan.")



engine = create_engine("postgresql://root:root@localhost:5432/ny_taxi")



df_iter = pd.read_csv('yellow_tripdata_2024-01.csv',iterator=True, chunksize=100000)


df=next(df_iter)

len(df)


df.info()



df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)



df.head(n=0).to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')



get_ipython().run_line_magic('time', "df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')")




count = 0  # Initialize batch count
total_start = time()  # Track total execution time

while True:
    try:
        t_start = time()

        df = next(df_iter)  # Get next batch from iterator
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append', index=False)  # Append data

        t_end = time()
        count += 1  # Increment batch count

        print(f"Inserted batch {count}, took {t_end - t_start:.3f} seconds")

    except StopIteration:  # Break when there are no more batches
        print("No more data to process.")
        break

    except Exception as e:  # Catch any other errors
        print(f"Error encountered: {e}")
        break

total_end = time()  # Track total execution time
print(f'Completed! Total time taken was {total_end - total_start:.3f} seconds for {count} batches.')



