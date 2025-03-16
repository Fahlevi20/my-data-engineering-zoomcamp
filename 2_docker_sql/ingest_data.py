#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
from sqlalchemy import create_engine
import argparse
from time import time

# user
# password
# host
# port
# database name
# table name
# url of the csv 
)

def main(params):
    # Membaca file Parquet
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    
    csv_name= "output.csv"
    
    os.system(f"wget{url} -O {csv_name}")
    df = pd.read_parquet("yellow_tripdata_2024-01.parquet", engine="pyarrow")  # atau "fastparquet"

    # Menampilkan beberapa baris pertama
    print(df.head())
 

    df.to_csv("yellow_tripdata_2024-01.csv", index=False)

    print("Konversi berhasil! File CSV telah disimpan.")



    engine = create_engine("postgresql://{user}:{password}@{host}:{port}/{db}")



    df_iter = pd.read_csv('yellow_tripdata_2024-01.csv',iterator=True, chunksize=100000)


    df=next(df_iter)



    df.tpep_pickup_datetime=pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime=pd.to_datetime(df.tpep_dropoff_datetime)



    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')



    df.to_sql(name='yellow_taxi_data', con=engine, if_exists='append')




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

if __name__=="__main__":
    
    parser = argparse.ArgumentParser(description='Ingest CSV Data to Postgres', usage='%(prog)s [options]')
    parser.add_argument('user', help='user name for postgres')
    parser.add_argument('password', help='user password for postgres')
    parser.add_argument('host', help='password for postgres')
    parser.add_argument('port', help='port for postgres')
    parser.add_argument('db', help='user database name for postgres')
    parser.add_argument('table_name', help='name of the table where we will write the result to postgres')
    parser.add_argument('url', help='url of the csv file')

    args = parser.parse_args()
    main(args)
