import ipaddress


def analyze_ip_addresses(ip_addresses):
    """
    Validate and filter a list of IP addresses.

    Returns only unique public IP addresses.
    """

    public_ips = []
    invalid_ips = []
    non_public_ips = []

    for ip in ip_addresses:

        try:
            address = ipaddress.ip_address(ip)

        except ValueError:
            invalid_ips.append(ip)
            continue

        if address.is_global:
            if ip not in public_ips:
                public_ips.append(ip)
        else:
            if ip not in non_public_ips:
                non_public_ips.append(ip)

    return {
        "public_ips": public_ips,
        "invalid_ips": invalid_ips,
        "non_public_ips": non_public_ips
    }