from ip_analyzer import analyze_ip_addresses
from url_extractor import extract_urls_from_email
from threat_intelligence import analyze_threat_intelligence


test_email = """
Received: from 185.220.101.25
Please verify your account at https://www.example.com/login
You can also visit https://google.com
"""


# Extract IPs
test_ips = [
    "185.220.101.25",
    "192.168.1.10",
    "8.8.8.8"
]

analysis = analyze_ip_addresses(test_ips)

print("\nIP Analysis:")
print(analysis)


# Extract URLs
urls = extract_urls_from_email(test_email)

print("\nExtracted URLs:")
print(urls)


# Combined Threat Intelligence
results = analyze_threat_intelligence(
    analysis["public_ips"],
    urls
)

print("\nThreat Intelligence Results:")
print(results)