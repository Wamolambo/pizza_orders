import utils.db as config
import etl.extract as extract
import etl.transform as transform
import etl.load as load
import pandas as pd
from utils.logger import get_logger
import sys

# Initialise logger
logger = get_logger()

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
        logger.w('\nFailed to Initialise Database')
        print('\nError in db/schema.sql ' + str(e))

    finally:
        connection.commit()
        cursor.close()
        connection.close()
    

if __name__=="__main__":

    if sys.argv[1] == "init":
  
        # Initialise database
        logger.info("Initialising tables")
        create_tables()
        logger.info("Table Succesfuly Initialised")
    if sys.argv[1] == "run":
        logger.info("Pipeline Started")
        

        # Extract DataFrames from stored files
        customer_df, order_items_df, orders_df = extract.extract_order_data()

        # Transform DataFrames
        customer_clean = transform.transform_customers(customer_df)
        order_clean = transform.transform_order(orders_df,customer_clean)
        order_items_clean = transform.transform_order_items(order_items_df,order_clean)

        # Load data to postgres
        connection = config.database_connection()
        load.copy_dataframe(connection,customer_clean,"customers")
        load.copy_dataframe(connection,order_clean,"orders")
        load.copy_dataframe(connection,order_items_clean,"order_items")

        connection.commit()
        connection.close()

        logger.info("Pipeline Completed")


   