import mysql.connector


def find_mysql_dbs(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    
    cursor.execute("SHOW DATABASES")
    dbs = [db[0] for db in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return dbs

def find_mysql_tables(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    
    cursor.execute("SHOW TABLES")
    tables = [table[0] for table in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return tables