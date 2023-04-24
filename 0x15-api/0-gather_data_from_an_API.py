#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys


def gather_data(param):
    """
    Write a Python script that, using this REST API
    for a given employee ID, returns information about his/her
    TODO list progress.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{param}"
    task_url = "https://jsonplaceholder.typicode.com/todos/"

    user_response = requests.get(user_url)
    task_response = requests.get(task_url)

    user_resp = user_response.json()
    task_resp = task_response.json()

    tasks = 0
    completed_tasks = 0

    for my_dicts in task_resp:
        if my_dicts.get("userId") == int(param):
            tasks += 1
            if my_dicts.get("completed") is True:
                completed_tasks += 1

    name = user_resp["name"]
    print(f"Employee {name} is done with tasks({completed_tasks}/{tasks}):")

    for dicts in task_resp:
        if dicts.get("userId") == int(param) and dicts.get(
                "completed") is True:
            print("\t ", dicts.get("title"))


if __name__ == "__main__":
    gather_data(sys.argv[1])
