from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import Boolean, Column, create_engine, Date, ForeignKey, Integer, Numeric, String

from config import config


class BaseMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.upper()

    def __repr__(self):
        values = ', '.join('{}={!r}'.format(n, getattr(self, n)) for n in self.__table__.c.keys())
        return '{}({})'.format(self.__class__.__name__, values)

Base = declarative_base(cls=BaseMixin)


# Metadata
class COMPANY(Base):
    ID = Column(String, primary_key=True)


class CLIENT(Base):
    ID = Column(String, primary_key=True)


class PROJECT(Base):
    COMPANY_ID = Column(
        String, ForeignKey('COMPANY.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    ID = Column(String, primary_key=True)
    NAME = Column(String, nullable=False)
    CLIENT = Column(String, ForeignKey('CLIENT.ID', onupdate='CASCADE', ondelete='SET NULL'))
    LOCATION = Column(String)
    DATUM_VERTICAL = Column(String)
    DATUM_HORIZONTAL = Column(String)
    DATUM_HORIZONTAL_ZONE = Column(String)


class POINT(Base):
    COMPANY_ID = Column(
        String, ForeignKey('COMPANY.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    PROJECT_ID = Column(
        String, ForeignKey('PROJECT.ID', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    ID = Column(String, primary_key=True)
    TYPE = Column(String, nullable=False)
    LOGGED_BY = Column(String)
    CHECKED_BY = Column(String)
    STATUS = Column(String)
    DATE_START = Column(Date)
    DATE_END = Column(Date)
    LOCATION = Column(String)
    TERMINATION_REMARK = Column(String)
    FINAL_DEPTH = Column(Numeric(precision=2), nullable=False)
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


class PointMixin:
    @declared_attr
    def COMPANY_ID(cls):
        return Column(String, ForeignKey('COMPANY.ID', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)

    @declared_attr
    def PROJECT_ID(cls):
        return Column(String, ForeignKey('PROJECT.ID', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)

    @declared_attr
    def POINT_ID(cls):
        return Column(String, ForeignKey('POINT.ID', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)


class DepthIntervalMixin:
    TOP = Column(Numeric(precision=2), primary_key=True)
    BTM = Column(Numeric(precision=2))


# Field logging
class CONSTRUCTION(Base, PointMixin, DepthIntervalMixin):
    METHOD = Column(String, nullable=False)


class GEOLOGY(Base, PointMixin, DepthIntervalMixin):
    LEGEND = Column(String, nullable=False)
    USCS_SYMBOL = Column(String)
    ORIGIN = Column(String)
    MATERIAL = Column(String)
    COLOUR = Column(String)
    DESCRIPTION = Column(String)


class DEPTH_REMARKS(Base, PointMixin, DepthIntervalMixin):
    REMARK = Column(String, nullable=False)


class SOIL_STRENGTH(Base, PointMixin, DepthIntervalMixin):
    MIN = Column(String, nullable=False)
    MAX = Column(String)


class ROCK_CORE(Base, PointMixin, DepthIntervalMixin):
    TOTAL_CORE_RECOVERY = Column(Integer)
    ROCK_QUALITY_DESIGNATION = Column(Integer)


class ROCK_WEATHERING(Base, PointMixin, DepthIntervalMixin):
    MIN = Column(String, nullable=False)
    MAX = Column(String)


class ROCK_STRENGTH(Base, PointMixin, DepthIntervalMixin):
    MIN = Column(String, nullable=False)
    MAX = Column(String)


class ROCK_DISC(Base, PointMixin, DepthIntervalMixin):
    TYPE = Column(String)
    SUFFIX = Column(String)
    DIP_MIN = Column(String)
    DIP_MAX = Column(String)
    PLANARITY = Column(String)
    ROUGHNESS = Column(String)
    APERTURE_OBSERVATION = Column(String)
    INFILL = Column(String)
    APERTURE_MIN = Column(Integer)
    APERTURE_MAX = Column(Integer)
    REMARKS = Column(String)
    OVERRIDE = Column(String)


class ROCK_DISC_SPACING(Base, PointMixin, DepthIntervalMixin):
    MIN = Column(String, nullable=False)
    MAX = Column(String)


# Field testing
class SPT(Base, PointMixin, DepthIntervalMixin):
    BLOWS_SEAT = Column(String, nullable=False)
    BLOWS_TEST1 = Column(String)
    BLOWS_TEST2 = Column(String)
    HAMMER_BOUNCE = Column(Boolean, default=False, nullable=False)
    PEN_SEAT = Column(Integer, nullable=False)
    PEN_TEST1 = Column(Integer)
    PEN_TEST2 = Column(Integer)
    N = Column(Integer)
    N_INTERP = Column(Integer)
    REMARK = Column(String)
    REPORT = Column(String)


class LFWD(Base, PointMixin):
    TOP = Column(Numeric(precision=2), primary_key=True)
    MODULUS_MPa = Column(Numeric(precision=1), nullable=False)
    STRESS_kPa = Column(Numeric(precision=1))


# Samples and specimens for laboratory testing
class SAMPLE(Base, PointMixin, DepthIntervalMixin):
    TYPE = Column(String)
    REF = Column(String)


class SampleMixin:
    @declared_attr
    def SAMPLE_TOP(cls):
        return Column(String, ForeignKey('SAMPLE.TOP', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)

    @declared_attr
    def SAMPLE_TYPE(cls):
        return Column(String, ForeignKey('SAMPLE.TYPE', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)

    @declared_attr
    def SAMPLE_REF(cls):
        return Column(String, ForeignKey('SAMPLE.REF', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)


class SPECIMEN(Base, PointMixin, DepthIntervalMixin, SampleMixin):
    REF = Column(String)


class SpecimenMixin:
    @declared_attr
    def SPECIMEN_TOP(cls):
        return Column(String, ForeignKey('SPECIMEN.TOP', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)

    @declared_attr
    def SPECIMEN_REF(cls):
        return Column(String, ForeignKey('SPECIMEN.REF', onupdate='CASCADE', ondelete='CASCADE'),
                      primary_key=True)


# Laboratory testing
class PLI(Base, PointMixin, SampleMixin, SpecimenMixin):
    TYPE = Column(String, primary_key=True)
    IS50_MPa = Column(Numeric(precision=2), nullable=False)
    DEFECT = Column(Boolean, default=False, nullable=False)


class UCS(Base, PointMixin, SampleMixin, SpecimenMixin):
    UCS_MPa = Column(Numeric(precision=2), nullable=False)
    MODULUS_SECANT_GPa = Column(Numeric(precision=2))
    MODULUS_TANGENT_GPa = Column(Numeric(precision=2))
    DEFECT = Column(Boolean, default=False, nullable=False)


class WATER_CONTENT(Base, PointMixin, SampleMixin, SpecimenMixin):
    MC = Column(Numeric(precision=1))
    MC_VOLUMETRIC = Column(Numeric(precision=1))


class ATTERBERG_LIMITS(Base, PointMixin, SampleMixin, SpecimenMixin):
    LL = Column(Numeric(precision=1))
    PL = Column(Numeric(precision=1))
    PI = Column(Numeric(precision=1))
    LS = Column(Numeric(precision=1))


class GRADING_SUMMARY(Base, PointMixin, SampleMixin, SpecimenMixin):
    PERC_OVERSIZE = Column(Integer)
    PERC_GRAVEL = Column(Integer)
    PERC_SAND = Column(Integer)
    PERC_FINES = Column(Integer)
    PERC_SILT = Column(Integer)
    PERC_CLAY = Column(Integer)


class GRADING_DATA(Base, PointMixin, SampleMixin, SpecimenMixin):
    GRADING_SUMMARY_SPECIMEN_TOP = Column(String, ForeignKey(
        'GRADING_SUMMARY.SPECIMEN_TOP', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
    SIZE_mm = Column(Numeric(precision=3), nullable=False)
    PERC_PASSING = Column(Integer, nullable=False)


class CBR(Base, PointMixin, SampleMixin, SpecimenMixin):
    TYPE = Column(String, nullable=False)
    CBR = Column(Numeric(precision=1), nullable=False)
    SWELL = Column(Numeric(precision=1))


class AGGRESSIVITY(Base, PointMixin, SampleMixin, SpecimenMixin):
    pH = Column(Numeric(precision=1))
    SO4_ppm = Column(Integer)
    Cl_ppm = Column(Integer)
    CONDUCTIVITY_μS_cm = Column(Integer)
    SOLUBLE_SALTS_ppm = Column(Integer)


if __name__ == '__main__':
    engine = create_engine(config['db_url'])
    Base.metadata.create_all(engine)
