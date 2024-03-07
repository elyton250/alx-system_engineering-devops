import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/")
    users = user.json()
    
    filename= "todo_all_employees.json"
    
    for user in users:
        json.dump