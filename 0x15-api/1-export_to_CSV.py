#!/usr/bin/python3
"""
Based on task #0, export data in CSV format
Requirements:
    Records all tasks that are owned by ID
    Format: "id", "username", "task_status", "task_title"
    Extension: {id}.csv
"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https//jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]
    user_resp = requests.get(url + "users/{}".format(user_id))
    user = user_resp.json()
    username = user.get("username")

    params = {"userId": user_id}
    todos_resp = requests.get(url + "todos", params=params)

    todos = todos_resp.json

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        output = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        for todo in todos:
            output.writerow(
                [user_id, username, todo.get("completed"), todo.get("title")])
