from pipelines.training_pipeline import train_pipeline
from zenml.client import Client

if __name__ == "__main__":
    print(Client().active_stack.experiment_tracker.get_tracking_uri())
    train_pipeline(data_path="D:\Machine_Learning_Projects\Zenml_MLops\Cust_Satis_mlops\data\olist_customers_dataset.csv")

