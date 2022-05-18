import requests

host = "pulse-rest-testing.herokuapp.com"
# r = requests.get("https://{}/books".format(host))
res = "books"
r = requests.get(f"https://{host}/{res}")
resp_body = r.json()
# print(resp_body)
# for book in resp_body:
#     print(book["title"])

book_data = {"title": "War and Peace", "author": "Levko Debeluj"}
r1 = requests.post(f"https://{host}/{res}", data=book_data)
print(r1.json())
book_full_data = r1.json()
r2 = requests.delete(f"https://{host}/{res}/{book_full_data['id']}")
print(r2.status_code)
print(r2.text)