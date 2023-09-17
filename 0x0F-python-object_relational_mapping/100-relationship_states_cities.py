#!/usr/bin/python3


"""
Script to create the State "California" with the City "San Francisco".
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 4:
        print("Wrong code format")
        sys.exit(1)

    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create a new State object
    new_state = State(name="California")

    # Create a new City object
    new_city = City(name="San Francisco")

    # Add the City object to the State object
    new_state.cities.append(new_city)

    # Add the State object to the session
    session.add(new_state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()
