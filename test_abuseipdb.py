from abuseipdb import check_ip_abuse


if __name__ == "__main__":
    test_ip = "8.8.8.8"

    result = check_ip_abuse(test_ip)

    print("\nAbuseIPDB Result:")
    print(result)