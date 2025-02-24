import pandas as pd

with open('output.csv.gz') as zipped:
    print(zipped.readline())

# df2 = pd.read_csv('output.csv.gz', iterator=True,
#                   chunksize=100000)
# df = next(df2)
# print(df.head(10))
