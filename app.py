import os
import sqlite3
import pymysql

from typing import List

db_path = os.path.join(os.getcwd(), 'chinook.db')
connection = sqlite3.connect(db_path)


def execute_query(connection,
                  query_sql: str) -> List:
    """
    Execute a query against the database
    :param connection:
    :param query_sql: The SQL query to execute
    :return: The results of the query
    """
    cursor = connection.cursor()
    results = cursor.execute(query_sql)
    return results


def unwrapp_query_result(record: List) -> None:
    '''
    Функция для красивого вывода результата в консоль
    :param : результат запроса
    '''
    for record in record:
        print(record)


def get_employees():
    '''
    Функция для получения списка сотрудников
    :return: список сотрудников
    '''

    query_sql = f'''
        SELECT *
        FROM employees;
    '''
    result = execute_query(connection, query_sql)
    unwrapp_query_result(result)


get_employees()


