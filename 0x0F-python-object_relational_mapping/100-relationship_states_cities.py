#!/usr/bin/python3
'''creates the State “California” with the
City “San Francisco” from the database
hbtn_0e_100_usa'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
from sys import argv
from sqlalchemy.schema import Table


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                             argv[2],
                                                             argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    newstate = State(name='California')
    newcity = City(name='San Francisco')
    newstate.cities.append(newcity)
    session.add_all([newstate, newcity])
    session.commit()
    session.close()
