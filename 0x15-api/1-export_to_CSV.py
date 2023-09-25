#!/usr/bin/python3
""" py script that uses JSONPlaceholder API to get info about employee """
import csv
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
        l_task.append([userid,
                       name,
                       task.get('completed'),

                       task.get('title')])
    file_name = '{}.csv'.format(userid)
    with open(file_name, mode='w') as employee_file:
        employee_writer = csv.writer(employee_file,
                                     delimiter=',',
                                     quotechar='"',
                                     quoting=csv.QUOTE_ALL)
        for task in l_task:
            employee_writer.writerow(task)
