import mysql.connector
import psycopg2
from config import mysql_config, postgres_config


def get_mysql_connection():
    # Get MySQL connection parameters from config
    host = mysql_config['host']
    user = mysql_config['user']
    password = mysql_config['password']
    database = mysql_config['database']

    # Establish MySQL connection
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return connection

def get_postgres_connection():
    # Get PostgreSQL connection parameters from config
    host = postgres_config['host']
    user = postgres_config['user']
    password = postgres_config['password']
    database = postgres_config['database']

    # Establish PostgreSQL connection
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

    return connection
