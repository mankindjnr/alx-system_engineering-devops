#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
 returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    """
    script that displays an employee todo tasks and completed
    """
    param = sys.argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{param}"
    task_url = f"https://jsonplaceholder.typicode.com/todos/"

    # calling a requests.get request t0 tasks and users which
    # will respond witht the item with id 1
    user_response = requests.get(user_url)
    task_response = requests.get(task_url)

    # call json on the response object to view the
    # data that is sent back by the API
    user_resp = user_response.json()
    task_resp = task_response.json()

    # counting the tasks of userid given in the command_line
    tasks = 0
    completed_tasks = 0

    # looping a list of dictionaries
    for my_dicts in task_resp:
        if my_dicts.get("userId") == int(param):
            tasks += 1
            if my_dicts.get("completed") is True:
                completed_tasks += 1
                # print()
                # print(my_dicts)

                name = user_resp["name"]
    print(f"Employee {name} is done with tasks({completed_tasks}/{tasks}):")

    # looping a list of and printing only the tasks done
    for dicts in task_resp:
        if dicts.get("userId") == int(param) and dicts.get(
                "completed") is True:
            print("\t ", dicts.get("title"))
