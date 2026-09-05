#for learning API requests in Python

import requests

response = requests.get(
    "https://jsonplaceholder.typicode.com/todos"
)

print(response.status_code)
print(response.text)

data = response.json()

print(data)

for item in data:
    print(f"todos number: {item['id']}")


print(f"Title of first todo: {data[0]['title']}")

print("completed todos:")
for item in data:
    if item['completed']:
        print(f"todo title: {item['title']}, \n"
              f"todos number: {item['id']}")