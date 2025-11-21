#!/usr/bin/env python3
import requests
import json

# Test the signup endpoint
url = "http://127.0.0.1:8000/api/v1/auth/users"
data = {
    "username": "testuser",
    "email": "test@example.com", 
    "password": "testpassword123"
}

try:
    response = requests.post(url, json=data, headers={"Content-Type": "application/json"})
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")