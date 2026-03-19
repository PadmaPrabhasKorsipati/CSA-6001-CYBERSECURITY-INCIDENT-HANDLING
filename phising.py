import re
from email import message_from_string

print("===== PHISHING EMAIL INVESTIGATION TOOL =====\n")

# Step 1: Read Email File
try:
    with open("sample_email.txt", "r") as file:
        email_content = file.read()
except FileNotFoundError:
    print("Error: 'sample_email.txt' not found. Please create the file in the same directory.")
    exit()

email = message_from_string(email_content)

# Step 2: Extract Header Fields
from_header = email.get("From")
return_path = email.get("Return-Path")
subject = email.get("Subject")
received = email.get("Received")

print("Email Header Analysis:")
print("From:", from_header)
print("Return-Path:", return_path)
print("Subject:", subject)
print("Received IP:", received)
print("\n--------------------------\n")

# Step 3: Extract URLs
urls = re.findall(r'https?://[^\s]+', email_content)

print("URLs Found in Email:")
if urls:
    for url in urls:
        print(url)
else:
    print("No URLs found.")

print("\n--------------------------\n")

# Step 4: Phishing Indicators Detection
phishing_flags = []

# Check domain mismatch
if from_header and return_path and from_header.split('@')[-1] != return_path.split('@')[-1]:
    phishing_flags.append("Domain mismatch between From and Return-Path")

# Check suspicious keywords
suspicious_keywords = ["urgent", "verify", "suspend", "compromised"]
for word in suspicious_keywords:
    if word.lower() in email_content.lower():
        phishing_flags.append(f"Suspicious keyword detected: {word}")

# Check for IP-based URLs (e.g., http://10.0.5.55/login.php)
for url in urls:
    if re.search(r'https?://\d+\.\d+\.\d+\.\d+', url):
        phishing_flags.append(f"Suspicious IP-based URL detected: {url}")

# Step 5: Print Analysis Result
print("Phishing Indicators Detected:\n")

if phishing_flags:
    for flag in phishing_flags:
        print("⚠", flag)
else:
    print("No obvious phishing indicators found.")

print("\nInvestigation Completed.")