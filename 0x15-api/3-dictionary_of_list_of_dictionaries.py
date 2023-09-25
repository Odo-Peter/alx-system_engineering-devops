#!/usr/bin/python3
""" py script that uses JSONPlaceholder API to get info about employee """
import json
import requests
import sys


if __name__ == "__main__":
    target_url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(target_url)
    res = requests.get(user)
    json_obj = res.json()
    d_task = {}
    for user in json_obj:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(target_url, userid)
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)
        d_task[str(userid)] = l_task
    file_name = 'todo_all_employees.json'
    with open(file_name, mode='w') as f:
        json.dump(d_task, f)
