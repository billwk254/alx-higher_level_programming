#!/usr/bin/python3


"""
Script to print the first State object from the database hbtn_0e_6_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 4:
        print("Wrong code format")
        sys.exit(1)

    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Close the session
    session.close()
