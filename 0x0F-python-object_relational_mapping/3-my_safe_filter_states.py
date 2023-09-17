#!/usr/bin/python3


"""
Script to safely filter and display values from the states table
based on the provided state name.
"""


import MySQLdb
import sys


def safe_filter_states(username, password, database_name, state_name):
    """
    Safely filter and display values from the states table.

    Args:
        username (str): The username for MySQL authentication.
        password (str): The password for MySQL authentication.
        database_name (str): The name of the MySQL database to connect to.
        state_name (str): The state name to search for in the database.

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

        # Create a parameterized query to select states based on user input
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Wrong code format")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    # Call the function to safely filter and display states
    safe_filter_states(mysql_username, mysql_password, db_name, state)
