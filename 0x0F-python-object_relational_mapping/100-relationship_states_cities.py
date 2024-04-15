#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco"
   from the database hbtn_0e_100_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:/{}'
                           .format(username, password, db_name),pool_pre_ping=True)

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create the State "California" and the City "San Francisco"
    session.add(City(name = "San Francisco", state=State(name="Californie")))
    session.commit()

    # Close the session
    session.close()

