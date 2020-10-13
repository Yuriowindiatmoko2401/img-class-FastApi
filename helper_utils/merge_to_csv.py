import pandas as pd
import os
import json

def main():
    
    workdir = os.getcwd()

    ls_labels = os.listdir(workdir + '/raw_data/all_labels')

    ls_labels.remove('.gitkeep')

    ls_labels.remove('.DS_Store')

    # read n collecting all json files into dict
    json_dict = {}
    for label in ls_labels:

        with open(workdir + "/" + "raw_data/json_file/{label}.json".format(label=label), 'r') as f:
            json_dict[label] = json.load(f)

    # read n collecting dict into dataframes
    df_dict = {}
    for label in ls_labels:
        df = pd.DataFrame(json_dict[label])
        df['col_name'] = df[label]
        df[label] = 1
        for ex_sku in [x for x in ls_labels if x != label]:
            df[ex_sku] = 0
        df_dict[label]=df

    # merge all dataframes into one
    df_baru = pd.DataFrame()

    for i, label in enumerate(ls_labels):
        df_baru = pd.concat([df_baru,df_dict[label]])

    df_baru = df_baru.reset_index(drop=True)

    df_baru.to_csv(workdir + "/" + "data.csv",index=False)


if __name__ == '__main__':
    main()