#!/usr/bin/env python
# coding: utf-8

import os
import argparse
from time import time
from sqlalchemy import create_engine
import pandas as pd


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url

    if url.endswith('.csv.gz'):
        csv_name = 'output.csv.gz'
    else:
        csv_name = 'output.csv'

    print(url)
    print(csv_name)

    os.system(f'wget {url} -O {csv_name}')

    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df2 = pd.read_csv(csv_name, iterator=True,
                      chunksize=100000, compression='gzip')
    df = next(df2)

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name,
                        con=engine, if_exists='replace')
    df.to_sql(name=table_name,
              con=engine, if_exists='append')

    while True:
        t_start = time()
        df = next(df2)
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

        df.to_sql(name=table_name, con=engine, if_exists='append')
        t_end = time()
        print('Inserted another chunk, it took %.3f seconds' % (t_end-t_start))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')

    parser.add_argument('--user', required=True, help='user name for postgres')
    parser.add_argument('--password', required=True,
                        help='password for postgres')
    parser.add_argument('--host', required=True, help='host for postgres')
    parser.add_argument('--port', required=True, help='port for postgres')
    parser.add_argument('--db', required=True,
                        help='database name for postgres')
    parser.add_argument('--table_name', required=True,
                        help='name of the table where we will write the results to')
    parser.add_argument('--url', required=True, help='url of the csv file')

    args = parser.parse_args()

    main(args)
