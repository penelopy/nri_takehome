from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


ENGINE = None
Session = None

Base = declarative_base()

class Question(Base): #TODO convert fields to DateTime, Integer, Float
    __tablename__ = "questions"
    id = Column(Integer, primary_key = True, nullable=False)
    question_id = Column(String(5))
    strand_id = Column(String(5))
    strand_name = Column(String(32)) 
    standard_id = Column(String(5))
    standard_name = Column(String(32)) 
    difficulty = Column(String(5))

class Students(Base): #TODO convert fields to DateTime, Integer
    __tablename__ = "students"
    id = Column(Integer, primary_key = True, nullable=False)
    student_id = Column(String(5))
    question_id = Column(String(5))
    assigned_hours_ago = Column(String(5))
    answered_hours_ago = Column(String(5))

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


