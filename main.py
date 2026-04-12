import utils.db as config
import etl.extract as extract
import etl.transform as transform
import pandas


def create_tables():
    '''
        description: Initialise and create tables in Postgres database
    '''
    # Create connection to database
    connection = config.database_connection()
    cursor = connection.cursor()

    try:

        # Exceute schema file
        with open('db/schema.sql') as file:
            query = file.read()
            cursor.execute(query)
    except connection.Error as e:
        print('\nFailed to Initialise Database')
        print('\nError in db/schema.sql ' + str(e))

    finally:
        connection.commit()
        cursor.close()
        connection.close()
    

if __name__=="__main__":

    # Initialise database
    #create_tables()

    # Extract DataFrames from stored files
    customer_df, order_items_df, orders_df = extract.extract_order_data()

    # Transform DataFrames
    customer_clean = transform.transform_customers(customer_df)
    order_items_clean = transform.transform_order_items(order_items_df)

    print(order_items_clean.head(30))

    



    
















    # # conn = database_connection()

# # conn.cursor

# # Call get_credentials
# credentials = config.get_credentials()



# customer_path = credentials['paths']['customers']

# df = pandas.read_csv(customer_path)

# print(df.head(5))






#     # host_name = credentials['database']['host_name']
#     # user_name = credentials['database']['user_name']
#     # user_password = credentials['database']['user_password']
#     # databse_name = credentials['database']['databse_name']
#     # port = credentials['database']['port']