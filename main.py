import utils.db as config
import pandas


def create_tables():
    # Create connection to database
    connection = config.database_connection()
    cursor = connection.cursor()

    # Exceute schema file
    with open('db/schema.sql') as file:
        query = file.read()
        cursor.execute(query)

    connection.commit()
    cursor.close()
    connection.close()



create_tables()


# if __name__ == "__main___":
#     import sys

#     # if sys.argv[1] == "init":
#     #     init_db()

#     # Create connection to database
#     connection = config.database_connection()
#     cursor = connection.cursor()

#     # Exceute schema file
#     with open('db/schema.sql') as file:
#         query = file.read()

#         cursor.execute(query)

#     connection.commit()
#     cursor.close()
#     connection.close()













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