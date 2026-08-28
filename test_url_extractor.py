from url_extractor import extract_urls_from_email


test_email = """
Hello,

Please verify your account at https://www.example.com/login

You can also visit https://google.com for more information.

Thanks.
"""


urls = extract_urls_from_email(test_email)

print("\nExtracted URLs:")
print(urls)