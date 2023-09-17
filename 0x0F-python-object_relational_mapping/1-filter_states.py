#!/usr/bin/python3


"""
Script to list states with names starting with 'N'
"""


import MySQLdb
import sys


def filter_states(username, password, database_name):
    """
    List states with names starting with 'N' from a MySQL database.

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

        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

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
        print("Wrong code format")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list filtered states
    filter_states(mysql_username, mysql_password, database_name)
