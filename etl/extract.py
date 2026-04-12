import utils.db as config
import pandas as pd


def extract_order_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    '''
        descroption: Extract data from stored files
    '''

    # Get file paths from yaml config file
    config_paths = config.get_credentials()
    customer_path = config_paths['paths']['customers']
    order_items_path = config_paths['paths']['order_items']
    orders_path = config_paths['paths']['orders']

    # Read files into Dataframes
    customer_df = pd.read_csv(customer_path)
    order_items_df = pd.read_csv(order_items_path)
    orders_df = pd.read_json(orders_path, lines=True)

    return customer_df, order_items_df, orders_df