#!/bin/bash    
import hashlib
import datetime
import pytz

def generate_token(username):
    # Define the timezone for Accra, Ghana
    tz = pytz.timezone('Africa/Accra')
    
    # Get the current datetime in the Accra timezone
    current_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    
    # Create the string to be hashed
    token_string = f"{current_time} . {username.upper()}"
    
    # Hash the string using SHA-1
    sha1_hash = hashlib.sha1(token_string.encode('utf-8')).hexdigest()
    
    return sha1_hash

# Example usage
username1 = "admin"
username2 = "administrator"

token1 = generate_token(username1)
token2 = generate_token(username2)

print(f"Token for '{username1}': {token1}")
print(f"Token for '{username2}': {token2}")
