import requests

url='https://jsonplaceholder.typicode.com/posts'

# response = requests.get(url)
# print(response.json())

data={
    "title": "test",
    "body": "test body",
    "userId": 12
}
headers = {"Content-Type": "application/json; charset=utf-8"}

response = requests.post(url, headers=headers, json=data)

print(response.json())
