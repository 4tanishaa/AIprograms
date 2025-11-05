import tkinter as tk
from tkinter import messagebox

issues = {
    "Computer won't start": {
        "causes": [
            "Power cable not connected properly",
            "Faulty power supply",
            "Power button issue"
        ],
        "confidence": 90
    },
    "No display": {
        "causes": [
            "Monitor cable loose",
            "RAM not seated properly",
            "Graphics card not detected"
        ],
        "confidence": 85
    },
    "Computer restarting randomly": {
        "causes": [
            "Overheating issue",
            "Power supply problem",
            "Faulty RAM or loose cables"
        ],
        "confidence": 80
    },
    "Internet not working": {
        "causes": [
            "Router/modem disconnected",
            "Network driver issue",
            "Wi-Fi disabled or weak signal"
        ],
        "confidence": 75
    },
    "System running very slow": {
        "causes": [
            "Too many background apps",
            "Low RAM",
            "Malware or junk files"
        ],
        "confidence": 70
    },
    "No sound": {
        "causes": [
            "Audio driver not installed",
            "Muted volume",
            "Speaker/headphone connection issue"
        ],
        "confidence": 65
    },
    "USB not detected": {
        "causes": [
            "USB port fault",
            "Driver not updated",
            "Device malfunction"
        ],
        "confidence": 60
    }
}

def diagnose():
    selected_issue = issue_var.get()
    if selected_issue in issues:
        problem = issues[selected_issue]
        causes_text = "\n".join([f"• {c}" for c in problem["causes"]])
        confidence_text = f"Confidence Score: {problem['confidence']}%"
        message = f"Possible Causes:\n{causes_text}\n\n{confidence_text}\n\nSuggested Fix:\n- Check connections\n- Restart your computer\n- Update drivers if needed."
        messagebox.showinfo("Diagnosis Result", message)
    else:
        messagebox.showwarning("Unknown Issue", "Please select a valid issue.")

root = tk.Tk()
root.title("💻 Computer Troubleshooting Expert System")
root.geometry("550x450")
root.config(bg="#e3f2fd")

title_label = tk.Label(root, text="🧠 Computer Troubleshooting Expert System", font=("Arial", 16, "bold"), bg="#2196f3", fg="white", pady=10)
title_label.pack(fill="x")

desc_label = tk.Label(root, text="Select the problem you're facing:", font=("Arial", 12), bg="#e3f2fd")
desc_label.pack(pady=15)

issue_var = tk.StringVar(value="Select an issue")

issues_list = list(issues.keys())
dropdown = tk.OptionMenu(root, issue_var, *issues_list)
dropdown.config(width=35, font=("Arial", 11))
dropdown.pack(pady=10)

btn = tk.Button(root, text="Diagnose Problem", command=diagnose, font=("Arial", 13, "bold"), bg="#4caf50", fg="white", padx=10, pady=5)
btn.pack(pady=20)

footer_label = tk.Label(root, text="Developed by Tanisha Nakate | AI-Python Expert System", font=("Arial", 10), bg="#e3f2fd", fg="#555")
footer_label.pack(side="bottom", pady=10)

root.mainloop()
