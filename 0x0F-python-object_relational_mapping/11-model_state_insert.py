#!/usr/bin/python3


"""
Script to add the State object "Louisiana" to the database hbtn_0e_6_usa.
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

    # Create a new State object for Louisiana
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit it to the database
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)

    # Close the session
    session.close()
