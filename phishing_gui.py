import tkinter as tk
import re

def detect_phishing():

    url = entry.get()
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

    if score == 0:
        result = "SAFE WEBSITE"
    elif score <= 2:
        result = "SUSPICIOUS WEBSITE"
    else:
        result = "PHISHING WEBSITE DETECTED"

    result_label.config(text=result)


# GUI Window
window = tk.Tk()
window.title("Phishing URL Detector")
window.geometry("400x200")

title = tk.Label(window, text="Phishing URL Detector", font=("Arial",16))
title.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(pady=10)

check_button = tk.Button(window,text="Check URL",command=detect_phishing)
check_button.pack(pady=10)

result_label = tk.Label(window,text="",font=("Arial",12))
result_label.pack(pady=10)

window.mainloop()