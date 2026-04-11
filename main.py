import yaml
import psycopg


def get_credentials() -> dict:
    '''
    description: Read database connection data from .yaml file
    Retruns:    dictionary
    '''
    try:
        with open(file='config.yml',mode="r") as f:
            configs = yaml.safe_load(f) # safe_load instead read
            return configs

            
    except:
        print('failed to read config file')
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
        conn = psycopg.connect( user='postgres',
                                password='admin',
                                host='localhost',
                                port=port)
        
        
        print("Database connection pass")
        return conn
    except:
        print("Database connection fail")
    

conn = database_connection()
