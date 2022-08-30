import psycopg2

try:
    conn = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    cursor = conn.cursor()
    print("PostgreSQL connection is established \n")
    postgreSQL_select_Query = 'select * from "Employee"'

    cursor.execute(postgreSQL_select_Query)
    
    result = cursor.fetchmany(1);
    print(result)


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cursor.close()
        conn.close()
        print("\nPostgreSQL connection is closed")