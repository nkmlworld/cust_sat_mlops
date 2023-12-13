import logging
import pandas as pd
from zenml import step


class IngestData:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
        logging.info(f'Ingesting Data from {self.data_path}')
        return pd.read_csv(self.data_path)


@step
def ingest_df(data_path: str) -> pd.DataFrame:
    """
    Ingesting data from data path

    :param data_path:
        data_path : Path of the data
    :return:
        pd.DataFrame: the ingested data in dataframe
    """
    try:
        # ingest_data = IngestData(data_path).get_data()
        ing_data = IngestData(data_path)
        df = ing_data.get_data()
        return df
    except Exception as e:
        logging.error(f"Error while ingesting data: {e}")
        raise e
