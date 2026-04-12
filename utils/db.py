import yaml
import psycopg
from utils.logger import get_logger

# Initialise logger
logger = get_logger()

def get_credentials() -> dict:
    '''
    description: Read database connection data from .yaml file
    Retruns:    dictionary
    '''
    try:
        logger.info('Reading config file')
        with open(file='config.yml',mode="r") as f:
            configs = yaml.safe_load(f) # safe_load instead read
            
            return configs

            
    except yaml.error:
        logger.error('failed to read config file')
    finally:
        f.close()


def database_connection():
    '''
        description: Connect to Postgres Database
    '''

    # Call get_credentials
    credentials = get_credentials()

    # Get credentials from dict
    host_name = credentials['database']['host_name']
    user_name = credentials['database']['user_name']
    user_password = credentials['database']['user_password']
    databse_name = credentials['database']['databse_name']
    port = credentials['database']['port']



    try:
        conn = psycopg.connect( user=user_name,
                                password=user_password,
                                host=host_name,
                                port=port)
        
        
        logger.info("Succeful Database Connection")
        return conn
    except:
        logger.info("Failed Database Connection")
    


