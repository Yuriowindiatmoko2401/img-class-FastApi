import pandas as pd
import os
import json


workdir = os.getcwd()
data_folder = open(workdir + '/' + "list_sku.txt", 'r')
Lines = data_folder.readlines()

ls_sku = []

for line in Lines:
    ls_sku.append(line.replace('\n',''))

json_dict = {}
for sku in ls_sku:
    with open(workdir + "/{sku}.json".format(sku=sku), 'r') as f:
        json_dict[sku] = json.load(f)

df_dict = {}
for sku in ls_sku:
    df = pd.DataFrame(json_dict[sku])
    df['col_name'] = df[sku]
    df[sku] = 1
    for ex_sku in [x for x in ls_sku if x != sku]:
        df[ex_sku] = 0
    df_dict[sku]=df


df_baru = pd.DataFrame()

for i, sku in enumerate(ls_sku):
    df_baru = pd.concat([df_baru,df_dict[sku]])

df_baru = df_baru.reset_index(drop=True)

df_baru.to_csv("data.csv",index=False)


