#!/usr/bin/python3
"""access a REST API for TODO lists of employees"""

import requests
import sys
from sys import argv


if __name__ == '__main__':
    baseUrl = 'https://jsonplaceholder.typicode.com/users'
    empId = sys.argv[1]
    url = baseUrl + "/" + empId

    # Get employee name
    response = requests.get(url)
    empName = response.json().get('name')

    # Get data on the ToDo of the employee
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = 0
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(empName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
