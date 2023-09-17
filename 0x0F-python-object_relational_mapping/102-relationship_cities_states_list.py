#!/usr/bin/python3


"""
Script that lists all City objects from the database hbtn_0e_101_usa.
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

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all City objects.
    cities = session.query(City).order_by(City.id).all()

    # Loop through the cities and print the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()
