import datetime
import json

from zeep import Client
from zeep.cache import InMemoryCache
from zeep.transports import Transport

from app.core.config import settings
from app.logger import log
from app.sync_redis import cache

transport = Transport(cache=InMemoryCache(), timeout=15)
service = None


def connectToWebService():
    global service
    if service:
        return service

    try:
        host = settings.WEBSERVICE_HOST
        path = settings.WEBSERVICE_PATH
        log.debug(f"Connecting to {host}/{path}?singlewsdl")
        client = Client(f"{host}/{path}?singlewsdl", transport=transport)

        service = client.service
    except Exception as e:
        log.error(f"Failed to connect to web service: {e}")
        service = None

    return service


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(n)


def getIndexPrices(startdate, enddate):
    r = []
    try:
        service = connectToWebService()
        dr = daterange(startdate, enddate)
        for d in dr:
            parameters = {"Date": d, "CountryCode": "UG"}
            r.append(service.GetIndexDailySummary(**parameters))
    except Exception as e:
        log.error("Failed to retrieve prices")

    return r


def getMarketPrices(startdate, enddate, stock="ALL"):
    r = []

    parameters = {
        "MarketCode": 0,
        "FromDate": startdate.strftime("%Y-%m-%d"),
        "ToDate": enddate.strftime("%Y-%m-%d"),
        "AssetClass": stock,
        "DataPeriod": ord("D"),
        "CountryCode": "UG",
    }

    try:
        service = connectToWebService()
        r = service.MarketPricesForDateRange(**parameters)
    except Exception as e:
        log.error("Failed to retrieve prices")

    return r


def livePrices():
    s = cache.hgetall("security")
    securities = {}
    for _s in s:
        v = json.loads(s[_s])
        securities[v["code"]] = v
    service = connectToWebService()
    prices = service.LiveMarketPrices()
    r = {"market": [], "index": [], "bond": []}
    for x in prices:
        if x.Board == "Normal":
            try:
                pChange = (float(x.Change) / float(x.OpeningPrice)) * 100.0
            except Exception:
                pChange = 0
            s = securities.get(x.Company, None)
            if s:
                type = s["security_type"]
            else:
                type = "NO_SECURITY_TYPE"

            if type == "COMMON_STOCK":
                r["market"].append(
                    {
                        "stock": x.Company,
                        "change": float(x.Change),
                        "change_percent": float(pChange),
                        "open": float(x.OpeningPrice),
                        "high": float(x.High),
                        "low": float(x.Low),
                        "close": float(x.Close),
                        "last_deal_price": float(x.LastDealPrice),
                        "last_traded_quantity": int(x.LastTradedQuantity),
                        "market_cap": float(x.MarketCap),
                        "time": x.Time.isoformat(),
                        "volume": float(x.Volume),
                    }
                )
            elif type == "CORPORATE_BOND":
                r["bond"].append(
                    {
                        "stock": x.Company,
                        "change": float(x.Change),
                        "change_percent": float(pChange),
                        "open": float(x.OpeningPrice),
                        "high": float(x.High),
                        "low": float(x.Low),
                        "close": float(x.Close),
                        "last_deal_price": float(x.LastDealPrice),
                        "last_traded_quantity": int(x.LastTradedQuantity),
                        "market_cap": float(x.MarketCap),
                        "time": x.Time.isoformat(),
                        "volume": float(x.Volume),
                    }
                )

    try:
        prices = service.LiveIndexPrices()

        if prices:
            for x in prices:
                r["index"].append(
                    {
                        "index": x.IndexCode,
                        "name": x.IndexDescription,
                        "open": float(x.OpeningPrice),
                        "price": float(x.IndexPrice),
                        "market_cap": float(x.TotalMarketCap),
                        "time": x.TradeDate.isoformat(),
                    }
                )
    except Exception as e:
        log.error("Failed to retrieve index prices")

    return r


def delayedPrices():
    service = connectToWebService()
    prices = service.DelayedMarketPrices()
    r = {"market": [], "index": []}
    for x in prices:
        if x.Board == "Normal":
            r["market"].append(
                {
                    "stock": x.Company,
                    "change": float(x.Change),
                    "open": float(x.OpeningPrice),
                    "high": float(x.High),
                    "low": float(x.Low),
                    "close": float(x.Close),
                    "last_deal_price": float(x.LastDealPrice),
                    "last_traded_quantity": float(x.LastTradedQuantity),
                    "market_cap": float(x.MarketCap),
                    "time": x.Time.isoformat(),
                    "volume": float(x.Volume),
                }
            )

    try:
        prices = service.LiveIndexPrices()

        if prices:
            for x in prices:
                r["index"].append(
                    {
                        "index": x.IndexCode,
                        "name": x.IndexDescription,
                        "open": float(x.OpeningPrice),
                        "price": float(x.IndexPrice),
                        "market_cap": float(x.TotalMarketCap),
                        "time": x.TradeDate.isoformat(),
                    }
                )
    except Exception as e:
        log.error("Failed to retrieve index prices")

    return r
