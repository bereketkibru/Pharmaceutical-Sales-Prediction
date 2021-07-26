# importing libraries
from numpy.lib.function_base import median
import pandas as pd
import numpy as np
from urllib.parse import urlparse
import mlflow


# Get url from Dvc
import dvc.api
path = 'data/train.csv'
repo = 'G:/10_academy/Week_3/solution/Pharmaceutical-Sales-Prediction'
version = 'train_v1'

data_url = dvc.api.get_url(
    path= path,
    repo=repo,
    rev= version
)
mlflow.set_experiment('demo')



if __name__=="__main__":
    # warnings.filterwarnings('ignore')
    np.random.seed(40)

    #read the data
    data=pd.read_csv(data_url   ,sep=",")

    #log data params
    mlflow.log_param('data_url',data_url)
    mlflow.log_param('data_version',version)
    mlflow.log_param('input_rows',data.shape[0])
    mlflow.log_param('input_cols',data.shape[1])

    print(data.head(1))
    
