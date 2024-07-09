import requests

params = {"name":"Bharat","age":20}
payload = {"name":"Bhanu","age":69}
proxies = {"http":"139.99.237.62:80","https":"139.99.237.62:80"}
# headers={"User-Agent":"HelloWorld/1.1", "Accept":"image/png"}
headers={"User-Agent":"HelloWorld/1.1", "Accept":"image/jpeg"}
responseg= requests.get('https://httpbin.org/get',params=params) # Requesting data with params
responsep= requests.post('https://httpbin.org/post',data=payload) # Posting data with payload
responses= requests.get('https://httpbin.org/status/404') # Retrieving status
responseu= requests.get('https://httpbin.org/user-agent',headers=headers) # Retrieving User-Agent
responsei= requests.get('https://httpbin.org/image',headers=headers) # Retrieving Images
responsep= requests.get('https://httpbin.org/get',proxies=proxies) # Using Proxies
for _ in [1,2,3]:
    try:
        responsed= requests.get('https://httpbin.org/delay/5',timeout=3) # Timeout
    except:
        continue
print(responseg.url)
print(responsep.status_code)
# if responses.status_code==responses.status_code.not_found:
#     print("Not Found")
# else:
#     print(responses)
res_json= responseg.json()
del res_json['origin']
print(res_json)
print(responseu.text)
with open('myimagep.png','wb') as f:
    f.write(responsei.content)
with open('myimagej.jpg','wb') as f:
    f.write(responsei.content)
