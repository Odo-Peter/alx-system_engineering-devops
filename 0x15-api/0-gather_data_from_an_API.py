#!/usr/bin/python3
"""py script that uses JSONPlaceholder API to get info about employee """
import requests
import sys


if __name__ == "__main__":
    target_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(target_url, sys.argv[1])
    res = requests.get(user)
    json_obj = res.json()
    print("Employee {} is done with tasks".format(
        json_obj.get('name')), end="")

    todos = '{}todos?userId={}'.format(target_url, sys.argv[1])
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        if task.get('completed') is True:
            l_task.append(task)

    print("({}/{}):".format(len(l_task), len(tasks)))
    for task in l_task:
        print("\t {}".format(task.get("title")))
