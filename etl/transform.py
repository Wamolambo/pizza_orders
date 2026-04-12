import pandas as pd

def transform_customers(df: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted customer data
    '''
     # Normalize emails to lowercase
    df['email'] = df['email'].str.lower()

    # Keep earliest duplicated email
    df = df.sort_values('signup_date')
    df = df.drop_duplicates(subset='email', keep='first', inplace=False)

    # Remove records with invalid emails
    df = df[df['email'].str.contains('@', na=False)]

    # Replace NaN with empty string in country code
    df['country_code'] = df['country_code'].fillna('')

    return df


def transform_order_items(df: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted order items data
    '''

    # Exclude non posetive unite price 
    df = df[df['unit_price'] > 0 ]
    return df


def transform_order(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted order data
    '''

    # Convert to datetime
    df1['order_ts'] = pd.to_datetime(df1['order_ts'], utc=True, errors='coerce')

    # Rename column `sta-,tus` to `status`
    df1 = df1.rename(columns={'sta-,tus': 'status'})

    # Exclude orders referencing unknown customers
    df = df1[df1['customer_id'].isin(df2['customer_id'])]

     # Filter based on approved status codesList of valid order status
    df = df[df['status'].isin(['placed','shipped','cancelled','refunded'])]

    return df
