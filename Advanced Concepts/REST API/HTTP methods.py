import requests
url="https://jsonplaceholder.typicode.com/todos/"
API_KEY="testapikey"
# headers={
#     "Authorization": "Bearer "+API_KEY
# }
# params={
#     "location": "NYC"
# }
# response=requests.get(url, headers=headers, params=params)

# for json typicde params
params={
    "userId":3
}
response=requests.get(url, params=params)
result = (response.json())
