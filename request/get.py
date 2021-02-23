from requests import get

response=get("https://jsonplaceholder.typicode.com/posts")

print(response.text)