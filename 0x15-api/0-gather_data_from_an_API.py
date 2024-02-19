#!/usr/bin/python3
"""this for requesting a fake api"""
import requests
from sys import argv

if __name__ == '__main__':
    """to prvent to work when imported"""

    employee_id = argv[1]
    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')

    user_data = users.json()

    tasks_completed = 0
    total_tasks = len(todos.json())

    for task in todos.json():
        if task['completed']:
            tasks_completed += 1

    print(
        f"Employee {user_data['name']} is done with tasks "
        f"({tasks_completed}/{total_tasks}):")

    for task in todos.json():
        if task['completed']:
            tasks_completed += 1
            print(f"\t {task['title']}")
