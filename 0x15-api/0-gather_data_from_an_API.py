#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""
import requests;
import sys


args = sys.argv
parameter = args[1]
api_url = f"https://jsonplaceholder.typicode.com/users/{parameter}"

response = requests.get(api_url)

# call json on the response object to view the data that is sent back by the API
print(response.json())
