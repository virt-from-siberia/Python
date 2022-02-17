import requests
from requests import HTTPError
from requests.exceptions import Timeout

response = requests.get("http://engineerspock.com/")

print(response)
print(response.status_code)

if response:
    print('works')

for url in ["http://engineerspock.com/", "http://engineerspock.com/lolo"]:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_error:
        print(f"error:{http_error}")
    else:
        print('connected successfully')

response = requests.get("http://engineerspock.com/")
print(response.content)

response.encoding = 'utf8'
print(response.text)

response = requests.get("http://api.github.com/")
print(response.text)

data = response.json()
print(data)

blog_response = requests.get("http://engineerspock.com/")
git_response = requests.get("http://api.github.com/")

print('=============================')

print(blog_response.headers, end="\n")
print(' ')
print(git_response.headers, end="\n")
print(' ')
print(blog_response.headers['content-type'])

placeholder_response = requests.get("http://jsonplaceholder.typicode.com/comments", params=b"postId=1")
print(placeholder_response.text)

response = requests.post("http://httpbin.org/post", json=data)
json_response = response.json()
print(json_response['headers']['Content-Type'])

# auth_response = requests.get("https://apt.github.com/user", auth=("EngineerSpock", getpass()))

try:
    response = requests.get('https://apt.github.com/user', timeout=1)
except Timeout:
    print("the request time out")

with requests.Session() as session:
    session.auth = ('Alex', '123')

    response = requests.get('https://apt.github.com/user')
