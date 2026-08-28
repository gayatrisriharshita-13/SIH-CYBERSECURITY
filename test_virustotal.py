from virustotal import check_ip_virustotal


if __name__ == "__main__":
    test_ip = "8.8.8.8"

    result = check_ip_virustotal(test_ip)

    print("\nVirusTotal Result:")
    print(result)