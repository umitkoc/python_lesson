from requests import post

response=post("https://jsonplaceholder.typicode.com/posts",data={
    "userId":25,
    "title":"hello",
    "body":"world"
})
result=response
print(result.text)