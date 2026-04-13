import io
from utils.logger import get_logger

# Initialise logger
logger = get_logger()

def copy_dataframe(conn, df, table):
    """Load a pandas DataFrame into a PostgreSQL table using COPY"""

    logger.info(f"{table} Load Started")

    # Prepare the CSV buffer
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, header=False, sep=',', na_rep='')
    buffer.seek(0)

    with conn.cursor() as cur:
        copy_query = f"COPY {table} FROM STDIN (FORMAT CSV, DELIMITER ',')"
        
        with cur.copy(copy_query) as copy:
            copy.write(buffer.read())


    logger.info(f"{table} Load Completed")
    logger.info(f"Loaded {len(df)} {table}")
