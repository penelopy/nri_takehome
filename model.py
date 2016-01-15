from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import sessionmaker


ENGINE = None
Session = None

Base = declarative_base()

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key = True, nullable=False)
    strand_id = Column(Integer)
    strand_name = Column(String(32)) 
    standard_id = Column(Integer)
    standard_name = Column(String(32)) 
    difficulty = Column(Float)

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key = True, nullable=False)
    question_id = Column(Integer)
    assigned_hours_ago = Column(DateTime)
    answered_hours_ago = Column(DateTime)

def connect(): 
    global ENGINE
    global Session
    ENGINE = create_engine("sqlite:///questions.db", echo=True)
    Session = sessionmaker(bind=ENGINE)
    return Session()

db_session = connect()

def main():
    connect()
    Base.metadata.create_all(ENGINE)

if __name__ == "__main__":
    main()


