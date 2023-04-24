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
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(param)
    task_url = "https://jsonplaceholder.typicode.com/todos/"

    user_response = requests.get(user_url)
    task_response = requests.get(task_url)

    user_resp = user_response.json()
    task_resp = task_response.json()

    tasks = 0
    completed_tasks = 0

    for my_dicts in task_resp:
        """
        looping throught the dictionary
        """
        if my_dicts.get("userId") == int(param):
            tasks += 1
            if my_dicts.get("completed") is True:
                completed_tasks += 1

    name = user_resp["name"]
    print("Employee {} is done with tasks({completed_tasks}/{tasks}):".format(name)

    for dicts in task_resp:
        """
        another loop in the dictoanry json response
        """
        if dicts.get("userId") == int(param) and dicts.get(
                "completed") is True:
            print("\t ", dicts.get("title"))


if __name__ == "__main__":
    gather_data(sys.argv[1])
