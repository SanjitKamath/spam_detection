"""
URL Feature Extraction
======================

Extracts features used to detect phishing links.
"""

import re
from urllib.parse import urlparse


def extract_urls(text):

    pattern = r'https?://[^\s]+'
    return re.findall(pattern, text)


def url_length(url):

    return len(url)


def contains_ip(url):

    return bool(re.search(r"\d+\.\d+\.\d+\.\d+", url))


def suspicious_tld(url):

    parsed = urlparse(url)

    suspicious = ["xyz", "top", "tk", "ml"]

    for tld in suspicious:
        if parsed.netloc.endswith(tld):
            return 1

    return 0


def url_feature_vector(text):

    urls = extract_urls(text)

    if not urls:
        return [0,0,0]

    url = urls[0]

    return [
        url_length(url),
        contains_ip(url),
        suspicious_tld(url)
    ]