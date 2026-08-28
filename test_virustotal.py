from virustotal import (
    check_ip_virustotal,
    check_url_virustotal,
    check_domain_virustotal
)


print("\nVirusTotal IP Result:")
print(check_ip_virustotal("8.8.8.8"))


print("\nVirusTotal URL Result:")
print(check_url_virustotal("https://www.google.com/"))


print("\nVirusTotal Domain Result:")
print(check_domain_virustotal("google.com"))

if __name__ == "__main__":
    test_ip = "8.8.8.8"

    result = check_ip_virustotal(test_ip)

    print("\nVirusTotal Result:")
    print(result)