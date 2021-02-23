from requests import get
from requests import get
response=get("https://jsonplaceholder.typicode.com/posts",params={
    "id":25
})

print(response.text)