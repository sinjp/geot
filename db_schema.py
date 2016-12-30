from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Date, ForeignKey, Integer, Numeric, String


Base = declarative_base()


class Company(Base):
    __tableNAME__ = 'company'

    ID = Column(String, primary_key=True)

    def __repr__(self):
        return f'ID={self.ID}'


class Client(Base):
    __tableNAME__ = 'client'

    ID = Column(String, primary_key=True)

    def __repr__(self):
        return f'ID={self.ID}'


class Project(Base):
    __tableNAME__ = 'project'

    COMPANY_ID = Column(
        String, ForeignKey(Company.ID, onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    ID = Column(String, primary_key=True)
    NAME = Column(String)
    CLIENT = Column(String, ForeignKey(Client.ID, onupdate='CASCADE', ondelete='SET NULL'))
    LOCATION = Column(String)
    DATUM_VERTICAL = Column(String)
    DATUM_HORIZONTAL = Column(String)
    DATUM_HORIZONTAL_ZONE = Column(String)

    def __repr__(self):
        return (f'ID={self.ID}, NAME={self.NAME}, CLIENT={self.CLIENT}, '
                f'LOCATION={self.LOCATION}')


class Point(Base):
    __tableNAME__ = 'point'

    COMPANY_ID = Column(
        String, ForeignKey(Company.ID, onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    PROJECT_ID = Column(
        String, ForeignKey(Project.ID, onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    ID = Column(String, primary_key=True)
    TYPE = Column(String)
    LOGGED_BY = Column(String)
    CHECKED_BY = Column(String)
    STATUS = Column(String)
    DATE_START = Column(Date)
    DATE_END = Column(Date)
    LOCATION = Column(String)
    TERMINATION_REMARK = Column(String)
    FINAL_DEPTH = Column(Numeric(precision=2))
    X_EASTING = Column(Numeric(precision=3))
    Y_NORTHING = Column(Numeric(precision=3))
    Z_ELEVATION = Column(Numeric(precision=3))
    WGS84_LAT = Column(Numeric(precision=8))
    WGS84_LNG = Column(Numeric(precision=8))
    INCLINATION = Column(Numeric(precision=1), default=90)
    CREW = Column(String)
    MACHINE = Column(String)
    PIT_LENGTH = Column(Numeric(precision=2), default=None)
    PIT_WIDTH = Column(Numeric(precision=2), default=None)
    PAGE_DEPTH = Column(Integer, default=6)

    def __repr__(self):
        return (f'ID={self.ID}, TYPE={self.TYPE}, STATUS={self.STATUS}, '
                f'FINAL_DEPTH={self.FINAL_DEPTH}')
