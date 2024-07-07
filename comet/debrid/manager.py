import aiohttp

from .realdebrid import RealDebrid
from .alldebrid import AllDebrid
from .premiumize import Premiumize


def getDebrid(session: aiohttp.ClientSession, config: dict):
    debrid_service = config["debridService"]
    debrid_api_key = config["debridApiKey"]
    if debrid_service == "realdebrid":
        return RealDebrid(session, debrid_api_key)
    if debrid_service == "alldebrid":
        return AllDebrid(session, debrid_api_key)
    if debrid_service == "premiumize":
        return Premiumize(session, debrid_api_key)