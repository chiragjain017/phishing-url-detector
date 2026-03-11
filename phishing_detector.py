import re

def detect_phishing(url):

    score = 0

    suspicious_words = [
        "login","verify","secure","bank",
        "account","update","confirm","password"
    ]

    for word in suspicious_words:
        if word in url.lower():
            score += 1

    if len(url) > 75:
        score += 1

    if url.count(".") > 3:
        score += 1

    if "@" in url:
        score += 1

    ip_pattern = r"(\d{1,3}\.){3}\d{1,3}"
    if re.search(ip_pattern, url):
        score += 2

    return score


print("Phishing URL Detector")

url = input("Enter URL: ")

score = detect_phishing(url)

print("\nAnalysis Result:")

if score == 0:
    print("Safe Website")

elif score <= 2:
    print("Suspicious Website")

else:
    print("Phishing Website Detected")