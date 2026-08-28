import re


def extract_urls_from_email(email_text):
    """
    Extract unique URLs from email text.
    """

    url_pattern = r'https?://[^\s<>"\']+|www\.[^\s<>"\']+'

    urls = re.findall(url_pattern, email_text)

    # Remove common punctuation attached to URLs
    cleaned_urls = []

    for url in urls:
        url = url.rstrip(".,;:!?)]}")

        if url not in cleaned_urls:
            cleaned_urls.append(url)

    return cleaned_urls