#!/usr/bin/python3


"""
Script that lists all City objects from the database hbtn_0e_101_usa..
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


def main():
    # Check if the script is called with the correct number of arguments
    if len(argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>".format(argv[0]))
        return

    # Extract command-line arguments
    mysql_username, mysql_password, database_name = argv[1], argv[2], argv[3]

    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}")
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query to retrieve all City objects, sorted by cities.id, with their associated State
    cities = session.query(City).order_by(City.id).all()

    # Loop through the cities and print the results
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    main()