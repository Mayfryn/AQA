import requests
params = {"q":"ukr"}
headers = {'User-Agent': 'myapp/0.1', 'Accept-Encoding': 'html'}
r = requests.get('https://google.com', params=params, headers=headers)

print(r)

print(r.history)
# print(r.text)
print(r.headers)
print(r.status_code)
print(r.url)
print(r.request.headers)
