#!/usr/bin/python3
""" Gather data from an API """

import json
import requests
"""modules to work with"""


def get_employee_tasks():
    """ a function to return all info about the employee """
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_response = requests.get(url + "users")
        user_data = user_response.json()

        """hold the employee data in a dictionary"""
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]
        no_task_done = len(task_done)

        """display the result"""
        print(f"Employee {employee_name} is done with tasks("
              f"{no_task_done}/{total_task}):")

        """title of completed task"""
        for task in task_done:
            print(f"\t {task['title']}")
    except Exception as e:
        print(f"an error occured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
