# import requests 

# response = requests.post("https://automatic-funicular-gjrvpqqjp7xfwjxp-8000.app.github.dev/", data={"messages" : [{"role" : "user", "content" : "Hi!"}]})

# print(response.json())

# import requests

# url = "https://automatic-funicular-gjrvpqqjp7xfwjxp-8000.app.github.dev/"
# data = {"messages": [{"role": "user", "content": "Hi!"}]}

# response = requests.post(url, json=data)

# print(response.status_code)
# try:
#     print(response.json())
# except:
#     print("No json in response")
# print(response.text)

import requests

def code_data(data):
    new_data = {}
    for message in data:
        index_of_message = data.index(message)
        for i in message:
            new_data[f"{i}{index_of_message}"] = [message[i]]
    return new_data

url = 'https://yaroslavsamchukapi.onrender.com/post/'
data = [{"role" : "user", "content": "Hi! Who are you? And what you are doing here?"}] 
data = code_data(data)
print(data)


response = requests.post(url, data=data)

print(response.status_code)
print(response.json())