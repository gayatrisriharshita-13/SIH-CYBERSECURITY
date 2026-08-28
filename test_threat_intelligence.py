from ip_analyzer import analyze_ip_addresses
from abuseipdb import check_ip_abuse


test_ips = [
    "185.220.101.25",
    "192.168.1.10",
    "8.8.8.8"
]

analysis = analyze_ip_addresses(test_ips)

print("\nIP Analysis:")
print(analysis)

print("\nAbuseIPDB Results:")

for ip in analysis["public_ips"]:
    result = check_ip_abuse(ip)
    print(result)