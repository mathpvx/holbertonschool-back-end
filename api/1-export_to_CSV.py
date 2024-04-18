#!/usr/bin/python3
""" Python script that returns information about a given employee's To Do
list progress identified by ID, using REST API.
Export data in the CSV format.
"""


import csv
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
            the_employee = emp_info

    filename = "{}.csv".format(emp_id)
    with open(filename, 'w', newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todo:
            if task.get("userId") == emp_id:
                writer.writerow([the_employee.get("id"),
                                 the_employee.get("username"),
                                 task.get("completed"),
                                 task.get("title")])
