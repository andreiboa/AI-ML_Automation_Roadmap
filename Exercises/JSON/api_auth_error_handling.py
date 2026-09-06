
#Learning Authentication and Error Handling in python API

import os
import requests

api_key = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        headers=headers,
        timeout=5  # Set a timeout for the request (in seconds)
    )
    response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
except requests.exceptions.HTTPError as http_err: #error in the HTTP response
    print(f"HTTP error occurred: {http_err}")
except requests.exceptions.Timeout: #error in the request timeout
    print("Request timed out")
except requests.exceptions.RequestException as e: #error in the request
    print(f"An error occurred: {e}")

if response.status_code == 200:   
    data = response.json()

if "title" in data:
    print(f"Title todo: {data.get('title')}")
else:
    print("No title found in the response data")