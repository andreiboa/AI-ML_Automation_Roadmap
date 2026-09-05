#for learning API requests in Python

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos/1"
)

print(response.status_code)
print(response.text)

data = response.json()

print(data)

print(f"Title: {data['title']} \n",
      f"Completed: {data.get('completed')} \n"
      )