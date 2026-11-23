import requests

url = "http://127.0.0.1:8000/products"
payload = {"tillu badmos":"32"}

# Using the 'json' parameter automatically sets the Content-Type header
response = requests.post(url, json=payload)

print(response.status_code)
try:
    print(response.json())
except Exception:
    print(response)