#convert dbf files to csv

from simpledbf import Dbf5
dbf = Dbf5('file.dbf')
df = dbf.to_dataframe()
df.to_csv("file.csv", index=False, encoding='utf-8-sig')
