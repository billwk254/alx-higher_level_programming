#!/usr/bin/python3


"""
Script to list all states from a MySQL database using MySQLdb.

This script connects to a MySQL database and retrieves a list of states,
sorted in ascending order by their IDs.

Usage:
    ./0-select_states.py <mysql_username> <mysql_password> <database_name>

Arguments:
    mysql_username: The username for MySQL authentication.
    mysql_password: The password for MySQL authentication.
    database_name: The name of the MySQL database to connect to.

This script requires the MySQLdb module.

Example:
    ./0-select_states.py root root hbtn_0e_0_usa
"""


import MySQLdb
import sys


def list_states(username, password, database_name):
    """
    List all states from a MySQL database.

    Args:
        username (str): The username for MySQL authentication.
        password (str): The password for MySQL authentication.
        database_name (str): The name of the MySQL database to connect to.

    Returns:
        None
    """
    try:
        # Establish a connection to the MySQL server
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Execute the SQL query to select all states, ordered by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    list_states(mysql_username, mysql_password, database_name)
