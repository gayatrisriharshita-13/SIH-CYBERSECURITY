from ip_extractor import extract_ips_from_email
from ip_analyzer import analyze_ip_addresses


sample_email = """\
Received: from mail.example.com (185.220.101.25)
    by mail.destination.com;
X-Originating-IP: 8.8.8.8
Received: from internal.local (192.168.1.10)
    by mail.example.com;
Subject: Test email

This is the email body.
"""


if __name__ == "__main__":

    extracted_ips = extract_ips_from_email(sample_email)

    print("\nExtracted IPs:")
    print(extracted_ips)

    analysis = analyze_ip_addresses(extracted_ips)

    print("\nIP Analysis:")
    print(analysis)