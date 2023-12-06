from typing import Any, List, Tuple
import mysql.connector

def extract_data(mysql_conn: mysql.connector.connection.MySQLConnection, query: str) -> List[Tuple[Any]]:
    cursor: mysql.connector.cursor.MySQLCursor = mysql_conn.cursor()
    cursor.execute(query)
    data: List[Tuple[Any]] = cursor.fetchall()
    cursor.close()
    return data
