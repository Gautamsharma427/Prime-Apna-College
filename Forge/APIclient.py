import requests

url = "http://127.0.0.1:8000/products/wm01"
payload = {"SKU":"12C"}

# Using the 'json' parameter automatically sets the Content-Type header
response = requests.delete(url)

print(response.status_code)
try:
    print(response.json())
except Exception:
    print(response)