import pandas as pd
from utils.logger import get_logger

# Initialise logger
logger = get_logger()


def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted customer data
    '''

    logger.info("Customer Transform Started")


     # Normalize emails to lowercase
    df['email'] = df['email'].str.lower()

    # Keep earliest duplicated email
    df = df.sort_values('signup_date')
    df = df.drop_duplicates(subset='email', keep='first', inplace=False)

    # Remove records with invalid emails
    df = df[df['email'].str.contains('@', na=False)]

    # Replace NaN with empty string in country code
    df['country_code'] = df['country_code'].fillna(' ')

    logger.info("Customer Transform Completed")
    logger.info(f"Customer Transform = {len(df)}")
    return df


def transform_order_items(df: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted order items data
    '''

    logger.info("Order Items Transform Started")

    # Exclude non posetive unite price 
    df = df[(df['quantity'] > 0) & (df['unit_price'] > 0)]

    # Enforce FK to orders
    df = df[df['order_id'].isin(df2['order_id'])]

    logger.info("Order Items Transform Completed")
    logger.info(f"Order Items Transform = {len(df)}")
    return df


def transform_order(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted order data
    '''

    logger.info("Orders Transform Started")

    # Convert to datetime
    df1['order_ts'] = pd.to_datetime(df1['order_ts'], utc=True, errors='coerce')
    
    # Drop rows where order_ts
    df1 = df1.dropna(subset=['order_ts'])

    # Rename column `sta-,tus` to `status`
    df1 = df1.rename(columns={'sta-,tus': 'status'})

     # Filter based on approved status codesList of valid order status
    df1 = df1[df1['status'].isin(['placed','shipped','cancelled','refunded'])]

    # Exclude orders referencing unknown customers
    df = df1[df1['customer_id'].isin(df2['customer_id'])]

    logger.info("Orders Transform Completed")
    logger.info(f"Orders Transform = {len(df)}")

    return df
