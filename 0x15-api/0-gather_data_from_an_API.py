#!/usr/bin/python3
"""
Python script that returns information about his/her TODO list progress.
Requirements:
    Using urllib or requests module
    expected an integer as a parameter, which is the employee ID
    Display:
        First line: Employee ``name`` is done with tasks(done task/total)
        Second line: total task title for the completed tasks
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    employee_id = sys.argv[1]
    user_res = requests.get(url + "users/{}".format(employee_id))
    user = user_res.json()
    name = user.get("name")

    params = {"userId": employee_id}
    todos_res = requests.get(url + "todos", params=params)
    todos = todos_res.json()

    comp_todos = []
    for todo in todos:
        if todo.get("completed") is True:
            comp_todos.append(todo.get("title"))

    print("Employee {} is done with tasks({}/{})".
            format(name, len(comp_todos), len(todos)))

    for comp in comp_todos:
        print("\t {}".format(comp))
