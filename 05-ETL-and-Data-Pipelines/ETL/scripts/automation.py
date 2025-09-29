# *** Import libraries required for connecting to mysql
import mysql.connector
from mysql.connector.connection_cext import MySQLConnectionAbstract

# *** Import libraries required for connecting to DB2 or PostgreSql
import psycopg2
from psycopg2.extensions import connection as postgres_connection_type


def get_last_rowid(conn: postgres_connection_type) -> int:
    """
        Find out the last rowid from PostgreSql data warehouse
        The function get_last_rowid must return the last rowid of the table sales_data on the PostgreSql database.
    """
    cursor = conn.cursor()
    sql = "select max(rowid) from sales_data"
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    return rows[0][0]


def get_latest_records(conn: MySQLConnectionAbstract, rowid: int) -> list:
    """
        List out all records in MySQL database with rowid greater than the one on the Data warehouse
        The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

        :param conn: MySQL connection object
        :param rowid: int
    """
    cursor = conn.cursor()
    sql = "select rowid, product_id, customer_id, quantity from sales_data where rowid > %d" % rowid
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.commit()
    return rows


def insert_records(postgresconnection: postgres_connection_type, records: list) -> None:
    """
        Insert the additional records from MySQL into PostgreSql data warehouse.
        The function insert_records must insert all the records passed to it into the sales_data table in PostgreSql.

        :param postgresconnection: postgres_connection_type
        :param records: list
        :return:
    """
    cursor = postgresconnection.cursor()
    for record in records:
        sql = f"INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES ({record[0]}, {record[1]}, {record[2]}, {record[3]})"
        cursor.execute(sql)
        postgresconnection.commit()
    return


if __name__ == "__main__":

    # *** Connect to MySQL
    mysql_connection = mysql.connector.connect(
        user='root',
        password='rootpassword',
        host='localhost',
        database='sales'
    )

    # *** Connect to PostgreSql
    dsn_hostname = 'localhost'
    dsn_user = 'postgres'
    dsn_pwd = 'postgres'
    dsn_port = "5432"
    dsn_database = "postgres"

    postgres_connection = psycopg2.connect(
        database=dsn_database,
        user=dsn_user,
        password=dsn_pwd,
        host=dsn_hostname,
        port=dsn_port
    )

    last_row_id = get_last_rowid(postgres_connection)
    print("Last row id on production datawarehouse = ", last_row_id)

    new_records = get_latest_records(mysql_connection, last_row_id)
    print("New rows on staging datawarehouse = ", len(new_records))

    insert_records(postgres_connection, new_records)
    print("New rows inserted into production datawarehouse = ", len(new_records))

    # disconnect from mysql warehouse
    mysql_connection.close()

    # disconnect from PostgreSql data warehouse
    postgres_connection.close()
