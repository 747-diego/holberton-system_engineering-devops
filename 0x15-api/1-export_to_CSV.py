#!/usr/bin/python3
"""Export data in the CSV format."""

if __name__ == "__main__":
    import requests
    from sys import argv

    Ag = argv[1]
    Id = str(Ag)

    """Getting the Tasks."""
    ApiUrl = "https://jsonplaceholder.typicode.com/todos?userId=" + Ag
    Response = requests.get(url)
    ListofTasks = Response.json()

    """Getting the Users."""
    ApiUrl = "https://jsonplaceholder.typicode.com/users/" + Ag
    resp = requests.get(url)
    Name = Response.json()

    """Setting the Username to a variable."""
    Uname = Name.get("username")

    with open(Id + ".csv", "w") as File:
        for task in ListofTasks:
            TaskComplete = task.get("completed")
            Tt = task.get("title")
            line = '"{}","{}","{}","{}"\n'.format(Id, Uname, TaskCompleted, Tt)
            File.write(line)
