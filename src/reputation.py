"""
Domain Reputation Checker
=========================
Checks whether a domain appears suspicious.
"""

from urllib.parse import urlparse


SUSPICIOUS_DOMAINS = [
    "bit.ly",
    "tinyurl.com",
    "goo.gl"
]


def domain_reputation(text):

    urls = []

    import re

    urls = re.findall(r'https?://[^\s]+', text)

    if not urls:
        return 0

    domain = urlparse(urls[0]).netloc

    if domain in SUSPICIOUS_DOMAINS:
        return 1

    return 0