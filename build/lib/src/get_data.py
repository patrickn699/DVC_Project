import yaml
import pandas as pd
import os
import argparse

def read_para(config_path):
    with open(config_path) as p:
        config = yaml.safe_load(p)
        return config



def get_data(config_path):
    config = read_para(config_path)
    #print(config)
    data_path = config['data_source']['s3_source']
    df = pd.read_csv(data_path,sep =',',encoding = 'utf-8')
    return df



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config',default='params.yaml')
    passed = args.parse_args()
    get_data(config_path = passed.config)


