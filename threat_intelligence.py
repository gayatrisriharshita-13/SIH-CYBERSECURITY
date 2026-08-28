from abuseipdb import check_ip_abuse
from virustotal import check_ip_virustotal, check_url_virustotal
from geolocation import geolocate_ip


def analyze_threat_intelligence(public_ips, urls=None):
    """
    Perform threat intelligence analysis for public IPs and URLs.
    """

    if urls is None:
        urls = []

    ip_results = []

    for ip in public_ips:

        try:
            abuse_result = check_ip_abuse(ip)
        except Exception as e:
            abuse_result = {
                "error": str(e)
            }

        try:
            virustotal_result = check_ip_virustotal(ip)
        except Exception as e:
            virustotal_result = {
                "error": str(e)
            }

        try:
            geolocation_result = geolocate_ip(ip)
        except Exception as e:
            geolocation_result = {
                "error": str(e)
            }

        ip_results.append({
            "ip_address": ip,
            "abuseipdb": abuse_result,
            "virustotal": virustotal_result,
            "geolocation": geolocation_result
        })

    url_results = []

    for url in urls:

        try:
            virustotal_result = check_url_virustotal(url)
        except Exception as e:
            virustotal_result = {
                "error": str(e)
            }

        url_results.append({
            "url": url,
            "virustotal": virustotal_result
        })

    return {
        "ip_results": ip_results,
        "url_results": url_results
    }