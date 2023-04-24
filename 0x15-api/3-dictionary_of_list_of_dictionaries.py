#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""
import json
import requests
import sys


def completed_tasks():
    """
    extend your Python script to export data in the JSON format.
    """
    param = 1
    all_tasks = {}
    while True:
        url = "https://jsonplaceholder.typicode.com/users/{}".format(param)
        resp = requests.get(url)
        resp_json = resp.json()
        if len(resp_json) == 0:
            break
        name = resp_json.get("name")

        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            param)
        tasks = requests.get(url)
        tasks_json = tasks.json()
        task_list = []

        for task in tasks_json:
            my_dicts = {}
            my_dicts["task"] = task.get("title")
            my_dicts["completed"] = task.get("completed")
            my_dicts["username"] = name
            task_list.append(my_dicts)

        all_tasks[param] = task_list
        param += 1

    file_name = "todo_all_employees.json"
    with open(file_name, "a") as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    completed_tasks()
