#!/usr/bin/python3


"""
Script to print the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Check if the script is called with the correct number of arguments
    if len(sys.argv) != 5:
        print("Wrong code format")
        sys.exit(1)

    # Get the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state = sys.argv[4]

    # Create an SQLAlchemy engine to connect to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query and print the State object with the given state name
    state = session.query(State).filter_by(name=state_name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()
