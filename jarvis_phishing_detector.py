import tkinter as tk
import re
from datetime import datetime

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
        color = "#00ff9f"

    elif score <= 2:
        result = "SUSPICIOUS WEBSITE"
        color = "yellow"

    else:
        result = "PHISHING WEBSITE DETECTED"
        color = "red"

    result_label.config(text=result, fg=color)
    score_label.config(text=f"Risk Score: {score}")

    time = datetime.now().strftime("%H:%M:%S")
    history_box.insert(tk.END, f"[{time}] {url} → {result}\n")
    history_box.see(tk.END)


# Main Window
window = tk.Tk()
window.title("JARVIS Cyber Security Tool")
window.geometry("750x500")
window.configure(bg="#020617")

# Title
title = tk.Label(
    window,
    text="JARVIS PHISHING URL SCANNER",
    font=("Consolas",22,"bold"),
    fg="#38bdf8",
    bg="#020617"
)
title.pack(pady=15)

# URL Entry
entry = tk.Entry(
    window,
    width=60,
    font=("Consolas",12),
    bg="#0f172a",
    fg="white",
    insertbackground="white"
)
entry.pack(pady=10)

# Scan Button
scan_btn = tk.Button(
    window,
    text="SCAN URL",
    font=("Consolas",12,"bold"),
    bg="#2563eb",
    fg="white",
    padx=15,
    pady=5,
    command=detect_phishing
)
scan_btn.pack(pady=10)

# Result
result_label = tk.Label(
    window,
    text="Waiting for scan...",
    font=("Consolas",14,"bold"),
    fg="white",
    bg="#020617"
)
result_label.pack(pady=10)

# Risk Score
score_label = tk.Label(
    window,
    text="Risk Score: 0",
    font=("Consolas",12),
    fg="#22c55e",
    bg="#020617"
)
score_label.pack()

# History Label
history_label = tk.Label(
    window,
    text="SCAN HISTORY",
    font=("Consolas",14,"bold"),
    fg="#38bdf8",
    bg="#020617"
)
history_label.pack(pady=10)

# History Box
history_box = tk.Text(
    window,
    height=10,
    width=80,
    bg="#0f172a",
    fg="#22c55e",
    font=("Consolas",10)
)
history_box.pack()

window.mainloop()