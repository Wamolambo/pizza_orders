import pandas as pd

def transform_customers(customer_df: pd.DataFrame) -> pd.DataFrame:
    '''
        description : Transform extracted customer data
    '''
     # Normalize emails to lowercase
    customer_df['email'] = customer_df['email'].str.lower()

    # Keep earliest duplicated email
    customer_df = customer_df.sort_values('signup_date')
    customer_df = customer_df.drop_duplicates(subset='email', keep='first', inplace=False)

    # Remove records with invalid emails
    customer_df = customer_df[customer_df['email'].str.contains('@', na=False)]

    # Replace NaN with empty string in country code
    customer_df['country_code'] = customer_df['country_code'].fillna('')

    return customer_df