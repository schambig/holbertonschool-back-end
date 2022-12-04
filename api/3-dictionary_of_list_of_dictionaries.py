#!/usr/bin/python3
''' Export data in the JSON format '''
import json
import requests as r  # give an alias to the module


def get_api():
    ''' Gather data from an API '''
    url = 'https://jsonplaceholder.typicode.com/'
    usrs = r.get(url + 'users').json()

    with open('to_all_employees.json', 'w') as file:
        obj = {}
        for emp in usrs:
            task_list = []
            uid = emp.get('id')
            todo = r.get(url + 'todos',
                         params={'userId': uid}).json()
            for task in todo:
                tmp_obj = {
                    'username': emp.get('username'),
                    'task': task.get('title'),
                    'completed': task.get('completed')
                    }
                task_list.append(tmp_obj)
            obj[uid] = task_list
        # serialize an onject into a JSON stream
        json.dump(obj, file)


if __name__ == '__main__':
    get_api()
