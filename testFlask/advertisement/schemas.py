from marshmallow import Schema
from marshmallow.fields import Method, Nested, Integer, String, Float

from smartcook.public.schemas import SubRegionSchema


class BroadcastAdCriteriaSchema(Schema):
    time_of_day = Method('get_time_of_day')
    location_type = Method('get_location_type')

    sub_region = Nested(SubRegionSchema)

    min_repetition = Integer()
    max_repetition = Integer()

    def get_time_of_day(self, obj):
        return obj.time_of_day.name

    def get_location_type(self, obj):
        return obj.location_type.name

    class Meta:
        additional = ('id',)


class InPurchaseAdCriteriaSchema(Schema):
    time_of_day = Method('get_time_of_day')
    location_type = Method('get_location_type')
    gender = Method('get_gender')

    sub_region = Nested(SubRegionSchema)

    repetition = Integer()
    hh_size = Integer()

    language = String(default='en')
    fuel_spend_level = Float()

    def get_time_of_day(self, obj):
        return obj.time_of_day.name

    def get_location_type(self, obj):
        return obj.location_type.name

    def get_gender(self, obj):
        return obj.gender.name

    class Meta:
        additional = ('id', 'message',)


class AdvertisementSchema(Schema):
    file_url = Method('get_file_url')
    file_type = Method('get_file_type')

    # broadcast_criteria = Nested(BroadcastAdCriteriaSchema)
    # inpurchase_criteria = Nested(InPurchaseAdCriteriaSchema)

    def get_file_url(self, obj):
        return obj.file and obj.file.url

    def get_file_type(self, obj):
        return obj.file_type.name

    class Meta:
        additional = ('id', 'name',)
