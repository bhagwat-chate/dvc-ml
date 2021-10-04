import yaml
import os
import numpy as np
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score 
import json

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)

    return content

def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path, exist_ok=True)
        print(f"directory is created at {dir_path}")

def save_local_df(data, data_path, index_status = False):
    data.to_csv(data_path, index = index_status)
    print(f'data is saved at {data_path}')


def evaluate_metrics(test_y, predicted_values):
    rmse = np.sqrt(mean_squared_error(test_y, predicted_values))
    mae = mean_absolute_error(test_y, predicted_values)
    r2 = r2_score(test_y, predicted_values)

    return rmse, mae, r2

def save_reports(report: dict, report_path: str, indent_count=4):
    with open(report_path, 'w') as f:
        json.dump(report, f, indent=indent_count)
    print(f"reports are saved at {report_path}")

