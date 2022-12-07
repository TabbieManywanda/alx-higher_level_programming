#!/usr/bin/python3
''' lists all State objects from the
database hbtn_0e_6_usa'''


from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://argv[1]:argv[2]@localhost:3306/argv[3]')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
