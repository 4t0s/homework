import threading
import requests
import time
def get_data(i, url):
    data = requests.get(url).text
    with open(f"data_{i}.json", "w") as file:
        file.write(data)
        
start = time.time()
for i in range(1,101):
    get_data(i,f"https://jsonplaceholder.typicode.com/todos/{i}")
    time.sleep(1)
timed = time.time()
print(timed-start)
start = time.time()
for i in range(1,101):
    t=threading.Thread(target=get_data, args=(i,f"https://jsonplaceholder.typicode.com/todos/{i}"))
    t.start()
timed = time.time()
print(timed-start)