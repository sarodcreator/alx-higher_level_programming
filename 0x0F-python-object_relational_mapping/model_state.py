#!/usr/bin/python3
"""class definition of a State and an instance Base = declarative_base():

State class:
inherits from Base Tips
links to the MySQL table states
class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
class attribute name that represents a column of a string with maximum 128 characters and can’t be null
"""

from sys  import argv
import model_state Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
            (argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.ceate_all(engine)
