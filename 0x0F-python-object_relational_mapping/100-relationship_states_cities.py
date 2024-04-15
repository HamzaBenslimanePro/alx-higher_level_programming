#!/usr/bin/python3
"""Script that creates the State "California" with the City "San Francisco"
   from the database hbtn_0e_100_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create an engine to interact with the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a session
    session = Session()

    # Create the State "California" and the City "San Francisco"
    california = State(name='California', cities=[City(name='San Francisco')])
    session.add(california)
    session.commit()

    # Close the session
    session.close()

