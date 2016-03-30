from depot.fields.sqlalchemy import UploadedFileField
from enum import IntEnum
from flask_login import UserMixin
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Numeric
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import Timestamp

from smartcook.database import Base, Model
from smartcook.fuelpoint.models import FuelPoint
from smartcook.public.models import SubRegion
from smartcook.sa_types import EnumChoiceType
from smartcook.user.models import User, Gender


class AdFileType(IntEnum):
    image = 1
    video = 2


class AdType(IntEnum):
    broadcast = 1
    in_purchase = 2


class AdTime(IntEnum):
    morning = 1
    afternoon = 2
    evening = 3
    all_times = 0


class AdLocation(IntEnum):
    market = 1
    small_store = 2


class Advertiser(Base, UserMixin, Model):
    name = Column(String(128), nullable=False, unique=True)

    def __repr__(self):
        return '<Advertiser({})>'.format(self.name)


class Advertisement(Base, Timestamp, Model):
    advertiser_id = Column(None, ForeignKey(Advertiser.id), nullable=False)
    advertiser = relationship(Advertiser, backref=backref('advertisements'))

    file = Column(UploadedFileField)
    file_type = Column(EnumChoiceType(AdFileType, impl=Integer()), nullable=False)

    name = Column(String(128), nullable=False, unique=True)
    duration = Column(Integer)
    active = Column(Boolean)


class ShownAdvertisement(Base, Timestamp, Model):
    ad_id = Column(None, ForeignKey(Advertisement.id), nullable=False)
    ad = relationship(Advertisement, backref=backref('shown_history'))

    fuel_point_id = Column(None, ForeignKey(FuelPoint.id), nullable=False)
    fuel_point = relationship(FuelPoint, backref=backref('shown_ads'))


class BroadcastAdCriteria(Base, Model):
    time_of_day = Column(EnumChoiceType(AdTime, impl=Integer()), nullable=False)

    sub_region_id = Column(None, ForeignKey(SubRegion.id))
    sub_region = relationship(SubRegion)

    location_type = Column(EnumChoiceType(AdLocation, impl=Integer()), nullable=False)

    ad_id = Column(None, ForeignKey(Advertisement.id))
    ad = relationship(Advertisement, backref=backref('broadcast_criteria', uselist=False))

    min_repetition = Column(Integer)
    max_repetition = Column(Integer)


class InPurchaseAdCriteria(Base, Model):
    time_of_day = Column(EnumChoiceType(AdTime, impl=Integer()), nullable=False)

    sub_region_id = Column(None, ForeignKey(SubRegion.id))
    sub_region = relationship(SubRegion)

    location_type = Column(EnumChoiceType(AdLocation, impl=Integer()), nullable=False)

    ad_id = Column(None, ForeignKey(Advertisement.id))
    ad = relationship(Advertisement, backref=backref('inpurchase_criteria', uselist=False))

    gender = Column(EnumChoiceType(Gender, impl=Integer()), nullable=False)

    #household size
    hh_size = Column(Integer, default=1)
    language = Column(String(30), default='en')
    fuel_spend_level = Column(Numeric)

    repetition = Column(Integer)
    message = Column(String(256))


class UserAdInterest(Base, Timestamp, Model):
    ad_id = Column(None, ForeignKey(Advertisement.id))
    ad = relationship(Advertisement, backref=backref('user_interests'))

    fuel_point_id = Column(None, ForeignKey(FuelPoint.id))
    fuel_point = relationship(FuelPoint, backref=backref('user_ad_interests'))

    # for registered user
    user_id = Column(None, ForeignKey(User.id))
    user = relationship(User, backref=backref('user_ad_interests'))

    # for unregistered user
    phone_number = Column(String(15))
