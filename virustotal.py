import os
import requests
from dotenv import load_dotenv


load_dotenv()

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/ip_addresses"


def check_ip_virustotal(ip_address):
    """
    Check an IP address using VirusTotal.
    """

    if not VIRUSTOTAL_API_KEY:
        raise ValueError("VIRUSTOTAL_API_KEY not found in .env")

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    response = requests.get(
        f"{VIRUSTOTAL_URL}/{ip_address}",
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()["data"]["attributes"]

    return {
        "ip_address": ip_address,
        "reputation": data.get("reputation"),
        "country": data.get("country"),
        "asn": data.get("asn"),
        "as_owner": data.get("as_owner"),
        "last_analysis_stats": data.get("last_analysis_stats", {})
    }