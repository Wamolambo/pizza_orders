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

    df = df[df['unit_price'] > 0 ]
    return df