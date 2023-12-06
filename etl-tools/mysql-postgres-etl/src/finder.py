import mysql.connector
import psycopg2


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

def find_postgres_schemas(host, port, user, password, database):
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    
    cursor.execute("SELECT schema_name FROM information_schema.schemata")
    schemas = [schema[0] for schema in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return schemas

def find_postgres_tables(host, port, user, password, database):
    connection = psycopg2.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=database
    )
    cursor = connection.cursor()
    
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
    tables = [table[0] for table in cursor.fetchall()]
    
    cursor.close()
    connection.close()
    
    return tables