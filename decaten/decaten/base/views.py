from django.shortcuts import render
from django.http import JsonResponse
import re
import requests

# Create your views here.
def base(request):
    return render(request, 'base/base.html')

def code_data(data):
    new_data = {}
    for message in data:
        index_of_message = data.index(message)
        for i in message:
            new_data[f"{i}{index_of_message}"] = [message[i]]
    return new_data

def decode_from_query_dict(data):
    role = ""
    new_messages = []
    for key in data:
        if re.search("role", key):
            role = data[key]
        elif re.search("content", key):
            new_messages.append({"role" : role, "content" : data[key]})
    return new_messages

def support_chat(request):
    if request.method == "POST":
        messages = request.POST
        print(messages)
        messages = decode_from_query_dict(messages)
        url = 'https://yaroslavsamchukapi.onrender.com/post/'
        
        messages = code_data(messages)
        response = requests.post(url, data=messages)

        print(response.status_code)
        print(response.json())
        return JsonResponse(data=response.json())

    return render(request, "base/support.html")