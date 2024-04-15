#!/usr/bin/python3
""" Python script that returns information about a given employee's To Do
list progress identified by ID, using REST API.
Export data in Json format."""


import requests
import sys
import json


if __name__ == "__main__":
    todo_json = requests.get("https://jsonplaceholder.typicode.com/todos")
    emps_info_json = requests.get("https://jsonplaceholder.typicode.com/users")
    
    """converts responses to lists"""
    todo = todo_json.json()
    emps_info = emps_info_json.json()
    
    emp_id = int(sys.argv[1])
    json_obj = {}
    tasks_list = []

    for emp_info in emps_info:
        # using get to prevent keyError
        if emp_info.get("id") == emp_id:
            the_employee = emp_info
            
    for task in todo:
        if task.get("userId") == emp_id:
            task_dict = {}
            task_dict["task"] = task.get("title")
            task_dict["completed"] = task.get("completed")
            task_dict["username"] = the_employee.get("username")
            tasks_list.append(task_dict)
            
    json_obj[str(the_employee.get("id"))] = tasks_list
    
    filename = "{}.json".format(emp_id)
    with open(filename, 'w') as file:
        json.dump(json_obj, file)
