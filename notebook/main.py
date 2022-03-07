import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="docker",
                                  host="db",
                                  port="5432",
                                  database="world")
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from city order by id fetch first 10 rows only"
    

    cursor.execute(postgreSQL_select_Query)
    world_records = cursor.fetchall()
    
    for row in world_records:
        print("Id = ", row[0])
        print("City = ", row[1])
        print("Country = ", row[2], "\n")

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")