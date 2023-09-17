#!/usr/bin/python3


"""
Script to list all cities of a specific state from the database hbtn_0e_4_usa.
"""


import MySQLdb
import sys


def filter_cities(username, password, database_name, state_name):
    """
    Filter and display cities of the specified state from the database.

    Args:
        username (str): The username for MySQL authentication.
        password (str): The password for MySQL authentication.
        database_name (str): The name of the MySQL database to connect to.
        state_name (str): The name of the state to filter cities by.

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

        # Create a parameterized query to select cities of the specified state
        query = "SELECT cities.id, cities.name FROM cities \
                 JOIN states ON cities.state_id = states.id \
                 WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows
        rows = cursor.fetchall()

        # Extract city names from the result
        city_names = [row[1] for row in rows]

        # Display the results as a comma-separated string
        result = ", ".join(city_names)
        print(result)

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
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter and display cities
    filter_cities(mysql_username, mysql_password, database_name, state_name)
