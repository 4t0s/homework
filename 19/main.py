import threading
import time
import requests
import os

def get_data(i, url):
    data = requests.get(url).text
    time.sleep(1)
    with open(f"data_{i}.json", "w") as file:
        file.write(data)
        
timestamp = time.time()

for i in range(1,11):
    get_data(i,f"https://jsonplaceholder.typicode.com/todos/{i}")
    
timed = time.time()
print(timed-timestamp)

timestamp = time.time()

for i in range(11,21):
    t=threading.Thread(target=get_data, args=(i,f"https://jsonplaceholder.typicode.com/todos/{i}"))
    t.start()
    
timed = time.time()
print(timed-timestamp)