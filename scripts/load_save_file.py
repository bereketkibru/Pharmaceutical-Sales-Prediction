import dvc.api
import pandas as pd
import pickle
import dvc.api
from f_logger import F_Logger


f_logger = F_Logger("load_save_file.log").get_f_logger()

def get_data(tag, Fpath, repo='G:/10_academy/Week_3/solution/Pharmaceutical-Sales-Prediction'):
    rev = tag
    path=Fpath
    data_url = dvc.api.get_url(path=path, repo=repo, rev=rev)
    df = pd.read_csv(data_url)
    f_logger.info(f"Read data from {path}, version {tag}")
    return df

def save_csv(df, csv_path):
        try:
            df.to_csv(csv_path, index=False)
            print('File Successfully Saved.!!!')
            f_logger.info(f"File Successfully Saved to {csv_path}")

        except Exception:
            print("Save failed...")
            f_logger.error(f"saving failed")

        return df
def read_model(file_name):
        with open(f"../models/{file_name}.pkl", "rb") as f:
            f_logger.info(f"Model loaded from {file_name}.pkl")
            return pickle.load(f)

def write_model(self, file_name, model):
        with open(f"../models/{file_name}.pkl", "wb") as f:
            f_logger.info(f"Model dumped to {file_name}.pkl")
            pickle.dump(model, f)
