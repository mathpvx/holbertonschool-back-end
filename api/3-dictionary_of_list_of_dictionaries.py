#!/usr/bin/python3
""" Python script that returns information every employees To Do
list progress identified by ID, using REST API.
Export data in Json format."""


import requests
import json


if __name__ == "__main__":
    todo_json = requests.get("https://jsonplaceholder.typicode.com/todos")
    emps_info_json = requests.get("https://jsonplaceholder.typicode.com/users")

    """converts responses to lists"""
    todo = todo_json.json()
    emps_info = emps_info_json.json()

    json_obj = {}
    tasks_list = []

    for emp_info in emps_info:
        for task in todo:
            if emp_info.get("id") == task.get("userId"):
                task_dict = {}
                task_dict["task"] = task.get("title")
                task_dict["completed"] = task.get("completed")
                task_dict["username"] = emp_info.get("username")
                tasks_list.append(task_dict)
        json_obj[str(emp_info.get("id"))] = tasks_list

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(json_obj, file)
