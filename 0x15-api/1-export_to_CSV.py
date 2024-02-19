#!/usr/bin/python3
"""Requesting a fake API and exporting data in CSV format."""
import csv
import requests
from sys import argv


def get_user_data(employee_id):
    users = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    user_data = users.json()
    return user_data, todos.json()


def print_completed_tasks(user_data, tasks):
    tasks_completed = 0
    total_tasks = len(tasks)

    print(f"Employee {user_data['name']} is done with tasks"
          "f({tasks_completed}/{total_tasks}):")

    for task in tasks:
        if task['completed']:
            tasks_completed += 1
            print(f"\t{task['title']}")


def export_to_csv(user_data, tasks):
    csv_file_name = f"{user_data['id']}.csv"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        fieldnames = [
            'USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()

        for task in tasks:
            writer.writerow({
                'USER_ID': user_data['id'],
                'USERNAME': user_data['username'],
                'TASK_COMPLETED_STATUS': str(task['completed']),
                'TASK_TITLE': task['title']
            })

    # print(f"\tExported data to {csv_file_name}")


if __name__ == '__main__':
    employee_id = argv[1]
    user_data, tasks = get_user_data(employee_id)

    # print_completed_tasks(user_data, tasks)
    export_to_csv(user_data, tasks)
