import os
import json
import requests

def requests_json_objects():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    directory = "requests"
    os.mkdir(directory)
    for i, obj in enumerate(data, start=1):
        with open(os.path.join(directory, f"json_object_{i}.json"), 'w') as file:
            json.dump(obj, file, indent=2)
            print(f"Saved json_object_{i}.json")

if __name__ == "__main__":
    requests_json_objects()
