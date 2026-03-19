import pandas as pd

print("===== IOC BASED DETECTION SYSTEM =====\n")

# Step 1: Load IOC list
ioc_data = pd.read_csv("ioc_list.csv")
print("IOC List Loaded Successfully")
print(ioc_data)
print("\n------------------------------\n")

# Step 2: Load Log Data
logs = pd.read_csv("network_logs.csv")
print("Log File Loaded Successfully")
print(logs)
print("\n------------------------------\n")

# Step 3: Separate IOC types
malicious_ips = ioc_data[ioc_data['type'] == 'IP']['value'].tolist()
malicious_hashes = ioc_data[ioc_data['type'] == 'HASH']['value'].tolist()

# Step 4: Detect IOC Matches
logs['IP_Match'] = logs['destination_ip'].isin(malicious_ips)
logs['Hash_Match'] = logs['file_hash'].isin(malicious_hashes)

# Step 5: Flag Suspicious Events
logs['IOC_Flag'] = logs['IP_Match'] | logs['Hash_Match']

print("Detection Results:\n")
print(logs)

print("\n------------------------------\n")

# Step 6: Show Only Suspicious Events
suspicious_events = logs[logs['IOC_Flag'] == True]

print("Suspicious Events Detected:\n")
print(suspicious_events)

print("\nDetection Completed Successfully.")