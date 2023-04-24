#!/usr/bin/python3
"""
 extend your Python script to export data in the JSON format.
"""
import json
import requests
import sys


def completed_tasks(param):
    """
    Using what you did in the task #0, extend your Python
    script to export data in the JSON format.
    """
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(param)
    resp = requests.get(users_url)
    resp_json = resp.json()
    name = resp_json.get("name")

    tasks_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        param)
    tasks_resp = requests.get(tasks_url)
    tasks_json = tasks_resp.json()
    tasks_list = []

    for task in tasks_json:
        todo_dict = {}
        todo_dict["task"] = task.get("title")
        todo_dict["completed"] = task.get("completed")
        todo_dict["username"] = name
        tasks_list.append(todo_dict)

    tasks = {"{}".format(param): tasks_list}

    file_name = "{}.json".format(param)
    with open(file_name, "a") as file:
        json.dump(tasks, file)


if __name__ == "__main__":
    completed_tasks(sys.argv[1])
