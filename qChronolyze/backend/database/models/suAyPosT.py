# backend/database/models/suAyPosT.py
from . import Column, Integer, String
#, create_engine
# from sqlalchemy.ext.declarative import declarative_base
from . import Base

class suAyPosTC(Base):
    __tablename__ = 'suAyPosT'

    suAyPos = Column(String, primary_key=True, nullable=False)
    surah = Column(Integer, nullable=False)
    ayah = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
    wrd = Column(String, nullable=False)  
    mean = Column(String, nullable=False, default='')  
    striDLs = Column(String, nullable=False, default='[]')
