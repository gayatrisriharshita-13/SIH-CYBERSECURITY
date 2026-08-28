import os
import requests
from dotenv import load_dotenv


load_dotenv()

ABUSEIPDB_API_KEY = os.getenv("ABUSEIPDB_API_KEY")
ABUSEIPDB_URL = "https://api.abuseipdb.com/api/v2/check"


def check_ip_abuse(ip_address, max_age_days=90):
    """
    Check an IP address against AbuseIPDB.
    """

    if not ABUSEIPDB_API_KEY:
        raise ValueError("ABUSEIPDB_API_KEY not found in .env")

    headers = {
        "Accept": "application/json",
        "Key": ABUSEIPDB_API_KEY
    }

    params = {
        "ipAddress": ip_address,
        "maxAgeInDays": max_age_days
    }

    response = requests.get(
        ABUSEIPDB_URL,
        headers=headers,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()["data"]

    return {
        "ip_address": data.get("ipAddress"),
        "abuse_confidence_score": data.get("abuseConfidenceScore"),
        "total_reports": data.get("totalReports"),
        "country_code": data.get("countryCode"),
        "usage_type": data.get("usageType"),
        "isp": data.get("isp"),
        "domain": data.get("domain"),
        "is_whitelisted": data.get("isWhitelisted"),
        "last_reported_at": data.get("lastReportedAt")
    }