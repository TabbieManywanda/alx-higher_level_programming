#!/usr/bin/python3
'''prints the State object with the name passed as
argument from the database hbtn_0e_6_usa'''


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1],
                                                             argv[2],
                                                             argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(State).filter_by(name=argv[4]).first()
    if result:
        print(result.id)
    else:
        print("Not found")
    session.commit()
    session.close()
