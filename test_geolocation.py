from geolocation import geolocate_ip


test_ips = [
    "185.220.101.25",
    "8.8.8.8"
]


print("\nGeolocation Results:")

for ip in test_ips:
    result = geolocate_ip(ip)
    print(result)