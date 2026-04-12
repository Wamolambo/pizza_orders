import io

def copy_dataframe(conn, df, table):
    """Load a pandas DataFrame into a PostgreSQL table using COPY"""

    # Prepare the CSV buffer
    buffer = io.StringIO()
    df.to_csv(buffer, index=False, header=False, sep=',', na_rep='')
    buffer.seek(0)

    with conn.cursor() as cur:
        copy_query = f"COPY {table} FROM STDIN (FORMAT CSV, DELIMITER ',')"
        
        with cur.copy(copy_query) as copy:
            copy.write(buffer.read())


print("Data loaded successfully!")
