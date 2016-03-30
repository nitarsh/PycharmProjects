from smartcook.advertisement.models import Advertisement
from smartcook.repos import SaRepository


class SaAdRepository(SaRepository):
    model = Advertisement
