import re
from email import policy
from email.parser import Parser
import ipaddress


IP_PATTERN = r"""
    (?:
        (?:\d{1,3}\.){3}\d{1,3}
        |
        [0-9a-fA-F:]+:[0-9a-fA-F:]+
    )
"""


def extract_ips_from_email(email_text):
    """
    Extract valid IP addresses from security-relevant email headers.

    Checks:
    - Received
    - X-Originating-IP
    - X-Forwarded-For

    Returns:
        list[str]: Unique valid IP addresses.
    """

    message = Parser(policy=policy.default).parsestr(email_text)

    relevant_headers = []

    relevant_headers.extend(message.get_all("Received", []))
    relevant_headers.extend(message.get_all("X-Originating-IP", []))
    relevant_headers.extend(message.get_all("X-Forwarded-For", []))

    found_ips = []

    for header in relevant_headers:

        matches = re.findall(IP_PATTERN, str(header), re.VERBOSE)

        for candidate in matches:

            # Remove brackets sometimes used around IPs
            candidate = candidate.strip("[]")

            try:
                ip = ipaddress.ip_address(candidate)
                ip = str(ip)

                if ip not in found_ips:
                    found_ips.append(ip)

            except ValueError:
                continue

    return found_ips