import os
import base64
import requests
from dotenv import load_dotenv


load_dotenv()

VIRUSTOTAL_API_KEY = os.getenv("VIRUSTOTAL_API_KEY")
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/ip_addresses"
VIRUSTOTAL_URL_REPORT = "https://www.virustotal.com/api/v3/urls"
VIRUSTOTAL_DOMAIN_URL = "https://www.virustotal.com/api/v3/domains"

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
def check_url_virustotal(url):
    """
    Check a URL using VirusTotal.
    """

    if not VIRUSTOTAL_API_KEY:
        raise ValueError("VIRUSTOTAL_API_KEY not found in .env")

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    # VirusTotal accepts an unpadded URL-safe Base64 identifier
    url_id = base64.urlsafe_b64encode(
        url.encode()
    ).decode().rstrip("=")

    response = requests.get(
        f"{VIRUSTOTAL_URL_REPORT}/{url_id}",
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()["data"]["attributes"]

    return {
        "url": url,
        "reputation": data.get("reputation"),
        "malicious": data.get("last_analysis_stats", {}).get("malicious", 0),
        "suspicious": data.get("last_analysis_stats", {}).get("suspicious", 0),
        "harmless": data.get("last_analysis_stats", {}).get("harmless", 0),
        "undetected": data.get("last_analysis_stats", {}).get("undetected", 0),
        "categories": data.get("categories", {}),
        "title": data.get("title")
    }


def check_domain_virustotal(domain):
    """
    Check a domain using VirusTotal.
    """

    if not VIRUSTOTAL_API_KEY:
        raise ValueError("VIRUSTOTAL_API_KEY not found in .env")

    headers = {
        "x-apikey": VIRUSTOTAL_API_KEY
    }

    response = requests.get(
        f"{VIRUSTOTAL_DOMAIN_URL}/{domain}",
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()["data"]["attributes"]

    return {
        "domain": domain,
        "reputation": data.get("reputation"),
        "malicious": data.get("last_analysis_stats", {}).get("malicious", 0),
        "suspicious": data.get("last_analysis_stats", {}).get("suspicious", 0),
        "harmless": data.get("last_analysis_stats", {}).get("harmless", 0),
        "undetected": data.get("last_analysis_stats", {}).get("undetected", 0),
        "categories": data.get("categories", {}),
        "tags": data.get("tags", {}),
        "registrar": data.get("registrar")
    }