import re

def is_phishing_url(url):
    # List of known phishing keywords
    phishing_keywords = [
        "login", "account", "verify", "password", "banking", 
        "paypal", "secure", "update", "confirm", "credentials"
    ]
    
    # List of known suspicious domains
    suspicious_domains = [
        "phishing-site.com", "fake-login.com", "malicious-domain.net"
    ]
    
    # Check for suspicious keywords in the URL
    for keyword in phishing_keywords:
        if re.search(keyword, url, re.IGNORECASE):
            return True
    
    # Check for suspicious domains
    for domain in suspicious_domains:
        if domain in url:
            return True
    
    # Check for unusual characters or patterns
    if re.search(r"https?://[^\s]+@[^\s]+", url):  # Check for user:pass in URL
        return True
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", url):  # Check for IP addresses
        return True
    
    # If none of the above, assume it's safe
    return False

# Test the function
test_urls = [
    "https://secure-login.com/verify",
    "http://phishing-site.com/account",
    "https://example.com",
    "http://192.168.1.1/login",
    "https://legit-website.com"
]

for url in test_urls:
    if is_phishing_url(url):
        print(f"⚠️ Phishing detected: {url}")
    else:
        print(f"✅ Safe URL: {url}")