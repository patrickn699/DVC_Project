import os
from get_data import read_para,get_data
import argparse

def load_and_save(config_path):
    config = read_para(config_path)
    df = get_data(config_path)
    new_cols = [cols.replace(" ",'_') for cols in df.columns]
    raw_data_path = config['load_data']['raw_dataset_csv']
    df.to_csv(raw_data_path,sep =',',index = False,header = new_cols)
    



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    passed = args.parse_args()
    load_and_save(config_path = passed.config)




