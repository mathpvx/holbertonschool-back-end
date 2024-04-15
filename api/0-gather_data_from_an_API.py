#!/usr/bin/python3
""" Python script that returns information about a given employee's To Do
list progress identified by ID, using REST API."""


import requests
import sys


if __name__ == "__main__":
    todo_json = requests.get("https://jsonplaceholder.typicode.com/todos")
    emps_info_json = requests.get("https://jsonplaceholder.typicode.com/users")

    emp_id = int(sys.argv[1])
    todo = todo_json.json()
    emps_info = emps_info_json.json()

    emp_todo = []
    done_task = []

    for emp_info in emps_info:
        # using get to prevent keyError
        if emp_info.get("id") == emp_id:
            emp_name = emp_info.get("name")

    for task in todo:
        if task.get("userId") == emp_id:
            if task.get("completed"):
                done_task.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(emp_name, len(done_task), 20))

    for done in done_task:
        print("\t", " ", done.get("title"))
