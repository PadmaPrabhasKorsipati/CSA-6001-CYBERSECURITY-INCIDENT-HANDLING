import pandas as pd

print("Generating IOC and Network Log datasets...")

# 1. Create the IOC List (Threat Intelligence)
ioc_data = {
    'type': ['IP', 'IP', 'HASH', 'HASH', 'DOMAIN'],
    'value': [
        '192.168.1.99', 
        '10.0.0.50', 
        'a591a6d40bf420404a011733cfb7b190', # Malicious MD5
        'b89356eb553f1246c6ea9b2138cdfb51', # Another malicious MD5
        'evil-malware-site.com'
    ]
}
pd.DataFrame(ioc_data).to_csv('ioc_list.csv', index=False)

# 2. Create the Network Logs (Simulated Traffic)
log_data = {
    'timestamp': ['08:00:01', '08:05:22', '08:12:45', '08:15:30', '08:20:10'],
    'source_ip': ['192.168.1.10', '192.168.1.11', '192.168.1.12', '192.168.1.10', '192.168.1.15'],
    'destination_ip': ['8.8.8.8', '192.168.1.99', '1.1.1.1', '10.0.0.50', '192.168.1.200'],
    'file_hash': [
        'd41d8cd98f00b204e9800998ecf8427e', # Normal
        'None', 
        'None', 
        'a591a6d40bf420404a011733cfb7b190', # Match!
        '8b1a9953c4611296a827abf8c47804d7'  # Normal
    ]
}
pd.DataFrame(log_data).to_csv('network_logs.csv', index=False)

print("Success! 'ioc_list.csv' and 'network_logs.csv' have been created.")