import http.client
import json

# Setting connection
conn = http.client.HTTPSConnection("simple-books-api.glitch.me")

#Status GET request
payload = ''
headers = {}
conn.request("GET", "/status", payload, headers)
response = conn.getresponse()
data = response.read()
print(data.decode("utf-8"))

#Book GET list request
payload = ''
headers = {}
conn.request("GET", "/books", payload, headers)
response = conn.getresponse()
data = response.read()
print(data.decode("utf-8"))

#Invalid GET request
payload = ''
headers = {}
conn.request("GET", "/books?type=crime", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#GET request two parameters
payload = ''
headers = {}
conn.request("GET", "/books?type=fiction&limit=2", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#GET requets - PATH parameter or PATH variable (part of the path that changes and is not sent - IDs normally)
payload = ''
headers = {}
conn.request("GET", "/books/2", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#POST request to a private end-point
#-- An access token would be neede for authentication--I do a POST to get the access token

1. Authenticating - bearer token
payload = json.dumps({
  "clientName": "John",
  "clientEmail": "john2@mail.com"
})
headers = {
  'Content-Type': 'application/json'
}
conn.request("POST", "/api-clients/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#2. Making the order request by using our regitered mail-access token
payload = json.dumps({
    "bookId": 2,
    "customerName": "John"
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
conn.request("POST", "/orders", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#3. Now let's have a loook to all the orders we have sent
#The body get ignored when get try to get the orders
payload = json.dumps({
    # "bookId": 2,
    # "customerName": "John"
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
conn.request("GET", "/orders", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#4. Let's get an specific order
payload = json.dumps({
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
orderid = "x8s-SgLDrlYjxgmCKmyZO"
conn.request("GET", "/orders/"+orderid, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#5. PATCH: Let's update an order
payload = json.dumps({
    "customerName": "John Pozo"
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
orderid = "x8s-SgLDrlYjxgmCKmyZO"
conn.request("PATCH", "/orders/"+orderid, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#6. GET again the modified/patched order
payload = json.dumps({
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
orderid = "x8s-SgLDrlYjxgmCKmyZO"
conn.request("GET", "/orders/"+orderid, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#7. DELETE the order
payload = json.dumps({
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
orderid = "x8s-SgLDrlYjxgmCKmyZO"
conn.request("DELETE", "/orders/"+orderid, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))

#8. GET to check if the order was deleted
payload = json.dumps({
    })
headers = {
    'Authorization': 'Bearer 379597d6a52c4c4d22449c247c1ebce8c0f46e352d90441d06ee6023e7fb8a23',
    'Content-Type': 'application/json'
    }
orderid = "x8s-SgLDrlYjxgmCKmyZO"
conn.request("GET", "/orders/"+orderid, payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


## API TESTING BY USING AUTOMATION TEST
##Newman + Reporting
