import requests


GEOLOCATION_URL = "http://ip-api.com/json"


def geolocate_ip(ip_address):
    """
    Get geolocation and network information for a public IP address.
    """

    response = requests.get(
        f"{GEOLOCATION_URL}/{ip_address}",
        params={
            "fields": "status,message,country,countryCode,city,isp,as,lat,lon"
        },
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    if data.get("status") != "success":
        return {
            "ip_address": ip_address,
            "error": data.get("message", "Geolocation lookup failed")
        }

    return {
        "ip_address": ip_address,
        "country": data.get("country"),
        "country_code": data.get("countryCode"),
        "city": data.get("city"),
        "isp": data.get("isp"),
        "asn": data.get("as"),
        "latitude": data.get("lat"),
        "longitude": data.get("lon")
    }