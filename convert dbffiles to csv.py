#convert dbf files to csv

from simpledbf import Dbf5
dbf = Dbf5('industria_forestal_2018.dbf')
df = dbf.to_dataframe()
df.to_csv("industria_forestal_2018.csv", index=False, encoding='utf-8-sig')