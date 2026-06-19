import requests

print(" Status code")
url = "https://httpbin.org/status/404"

response = requests.get(url)
if response.status_code != 200:
    print(f"Error: Received status code {response.status_code}")
else:
    print("Success!")

url1 = "https://httpbin.org/get/"

print(" Dynamic request with parameters")
response1 = requests.get(url1)

params = {
    "user": "Moises",
    "task": "Scraping"
}
response2 = requests.get(url1, params=params)
print(response2.url) 

print("HEADERS CONTENT TYPE")
url_ww3schools = "https://www.w3schools.com/"
    
get_response = requests.get(url_ww3schools)
header = get_response.headers
print(header)
print(header["Content-Type"])