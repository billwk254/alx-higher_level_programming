#!/usr/bin/python3


"""
Script to list all cities from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def list_cities(username, password, database_name):
    """
    List all cities from the specified database.

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

        # Execute the SQL query to select all cities
        cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
                        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")

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

    # Call the function to list cities
    list_cities(mysql_username, mysql_password, database_name)
