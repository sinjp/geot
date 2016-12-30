from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Column, create_engine, Date, ForeignKey, Integer, Numeric, String

from config import config


class BaseMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(n, getattr(self, n)) for n in self.__table__.c.keys())
        return '{}({})'.format(self.__class__.__name__, values)

Base = declarative_base(cls=BaseMixin)


class PointMixin:
    COMPANY_ID = Column(
        String, ForeignKey('company.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    PROJECT_ID = Column(
        String, ForeignKey('project.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    POINT_ID = Column(
        String, ForeignKey('point.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)


class Company(Base):
    ID = Column(String, primary_key=True)


class Client(Base):
    ID = Column(String, primary_key=True)


class Project(Base):
    COMPANY_ID = Column(
        String, ForeignKey('company.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    ID = Column(String, primary_key=True)
    NAME = Column(String)
    CLIENT = Column(String, ForeignKey('client.id', onupdate='CASCADE', ondelete='SET NULL'))
    LOCATION = Column(String)
    DATUM_VERTICAL = Column(String)
    DATUM_HORIZONTAL = Column(String)
    DATUM_HORIZONTAL_ZONE = Column(String)


class Point(Base):
    COMPANY_ID = Column(
        String, ForeignKey('company.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    PROJECT_ID = Column(
        String, ForeignKey('project.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
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


if __name__ == '__main__':
    engine = create_engine(config['db_url'])  # in-memory db
