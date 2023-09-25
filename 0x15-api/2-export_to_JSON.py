#!/usr/bin/python3
""" py script that uses JSONPlaceholder API to get info about employee """
import json
import requests
import sys


if __name__ == "__main__":
    target_url = 'https://jsonplaceholder.typicode.com/'

    userid = sys.argv[1]
    user = '{}users/{}'.format(target_url, userid)
    res = requests.get(user)
    json_obj = res.json()
    name = json_obj.get('username')

    todos = '{}todos?userId={}'.format(target_url, userid)
    res = requests.get(todos)
    tasks = res.json()
    l_task = []
    for task in tasks:
        dict_task = {"task": task.get('title'),
                     "completed": task.get('completed'),
                     "username": name}
        l_task.append(dict_task)
    d_task = {str(userid): l_task}
    file_name = '{}.json'.format(userid)
    with open(file_name, mode='w') as f:
        json.dump(d_task, f)
