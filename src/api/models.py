'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student(s):
Description: Project 02 - Incidents WS (models)
'''

from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Key(Base):
    __tablename__ = 'keys'
    key = Column(String(32), primary_key=True)

# TODO #2: complete the definition of the Incident's model class
class Incident(Base):
    __tablename__ = 'incidents'

    def as_dict(self):
        return { 
             
        }
