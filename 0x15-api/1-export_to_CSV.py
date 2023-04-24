#!/usr/bin/python3
"""
 extend your Python script to export data in the CSV format.
"""
import requests
import sys


def completed_tasks(id):
    """
    Using what you did in the task #0, extend your Python
    script to export data in the CSV format.
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    resp = requests.get(url)
    resp_json = resp.json()
    name = resp_json["username"]

    app_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
    tasks = requests.get(app_url)
    tasks_json = tasks.json()
    number_tasks = len(tasks_json)

    file_name = "{}.csv".format(id)

    with open(file_name, "a") as csv_file:
        for task in tasks_json:
            complete = task.get("completed")
            title = task.get("title")
            data = "\"{}\",\"{}\",\"{}\",\"{}\"\n".format(id,
                                                          name,
                                                          complete,
                                                          title)
            csv_file.write(data)


if __name__ == "__main__":
    completed_tasks(sys.argv[1])
