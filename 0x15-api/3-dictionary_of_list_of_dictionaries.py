#!/usr/bin/python3
"""Export data in the JSON format."""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    """Getting the Users Name."""
    ApiUrl = "https://jsonplaceholder.typicode.com/users/"
    Response = requests.get(url)
    ListOfNames = Response.json()

    for name in ListOfNames:
        Id = str(name.get("id"))
        ApiUrl = "https://jsonplaceholder.typicode.com/todos?userId=" + user_id
        Response = requests.get(ApiUrl)
        ListOfTasks = Response.json()

        username = name.get("username")

        Data = {}
        DataList = []

        for task in ListOfTasks:
            Data["task"] = task.get("title")
            Data["completed"] = task.get("completed")
            Data["username"] = Uname
            DataList.append(Data)
            Data = {}

        ExportJson = {}
        ExportJson[Id] = DataList

    with open("todo_all_employees.json", "w") as JsonFormat:
        json.dump(ExportJson, JsonFormat)
