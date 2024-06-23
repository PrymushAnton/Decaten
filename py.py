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

url = 'https://automatic-funicular-gjrvpqqjp7xfwjxp-8000.app.github.dev/post/'  # Replace with your actual URL
data = {'key': 'value'}  # Your POST data

response = requests.post(url)

print(response.status_code)
print(response.json())