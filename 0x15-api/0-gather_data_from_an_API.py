#!/usr/bin/python3
"""Returns information about his/her ToDo list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    """"First Argument.u""""
    Ag = argv[1]

    """"Getting the USER ID."""
    IdUrl = "https://jsonplaceholder.typicode.com/todos?userId=" + Ag
    Response = requests.get(IdUrl)
    tasks = Response.json()

    """Getting the USER NAME."""
    UsersUrl = "https://jsonplaceholder.typicode.com/users/" + Ag
    Response = requests.get(UsersUrl)
    Users = Response.json()

    """Created variables to hold number of tasks."""
    FinishedTasks = 0
    AllTasks = 0

    """Empty List that will contain titles."""
    CompletedTodoList = []

    for task in tasks:
        if task["completed"]:

            FinishedTasks = FinishedTasks + 1
            TodoList.append(task["title"])

        AllTasks = AllTasks + 1

    print("Employee {} is done with tasks({}/{}):"
          .format(Users, FinishedTasks, AllTasks))

    for title in CompletedTodoList:
        print("\t {}".format(title))
