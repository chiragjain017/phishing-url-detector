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
        result_label.config(text="SAFE WEBSITE", fg="#00ff88")

    elif score <= 2:
        result_label.config(text="SUSPICIOUS WEBSITE", fg="yellow")

    else:
        result_label.config(text="PHISHING WEBSITE DETECTED", fg="red")


# GUI Window
window = tk.Tk()
window.title("Cyber Security Tool - Phishing Detector")
window.geometry("520x320")
window.configure(bg="#0f172a")

# Title
title = tk.Label(
    window,
    text="PHISHING URL DETECTOR",
    font=("Consolas",20,"bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
title.pack(pady=20)

# Input label
label = tk.Label(
    window,
    text="Enter Website URL:",
    font=("Arial",12),
    fg="white",
    bg="#0f172a"
)
label.pack()

# URL Entry
entry = tk.Entry(
    window,
    width=45,
    font=("Arial",12),
    bg="#1e293b",
    fg="white",
    insertbackground="white"
)
entry.pack(pady=10)

# Button
check_button = tk.Button(
    window,
    text="SCAN URL",
    font=("Arial",12,"bold"),
    bg="#2563eb",
    fg="white",
    padx=15,
    pady=5,
    command=detect_phishing
)
check_button.pack(pady=10)

# Result
result_label = tk.Label(
    window,
    text="",
    font=("Arial",14,"bold"),
    bg="#0f172a"
)
result_label.pack(pady=20)

window.mainloop()