#!/usr/bin/python3
"""Export data in the JSON format."""

if __name__ == '__main__':
    import json
    import requests
    import sys import argv

    Ag = sys.argv[1]

    """Getting the Tasks."""
    ApiUrl = "https://jsonplaceholder.typicode.com/todos?userId="
    Response = requests. get(ApiUrl + Ag)
    ListOfTasks = Response.json()

    """Getting the Users Name."""
    ApiUrl = "https://jsonplaceholder.typicode.com/users/"
    Response = requests.get(ApiUrl + Ag)
    Name = Response.json()
    Uname = Name.get("username")

    Data = {}
    DataList = []

    for task in ListOfTasks:
        Data["task"] = task.get("title")
        Data["completed"] = task.get("completed")
        Data["username"] = Uname
        DataList.append(Data)
        Data = {}

    ExportJson = {}
    ExportJson[Ag] = DataList

    with open(Ag + ".json", "w") as JsonFormat:
        json.dump(ExportJson, JsonFormat)
