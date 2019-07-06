import socket
import sys
import threading
from queue import Queue
print_lock=threading.Lock()

'''try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("successful")
except Exception as e:
    print("failed")
port=80
try:
    host_ip=socket.gethostbyname('www.google.com')
except Exception as e:
    print("there is an error")
    sys.exit()
s.connect((host_ip,port))
print("successfully connected to google.com on port ",port,host_ip)
'''

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server=socket.gethostbyname('www.facebook.com')
def pscan(port):
    try:
        con=s.connect((server,port))
        with print_lock:
            print("port ",port," open")
        con.close()    
        
    except:
        pass
def threader():
    while True:
        worker=q.get()
        portscan(worker)
        q.task_done()
q=Queue()        
for x in range(10):
    if pscan(x):
        t=threading.Thread(traget=threader)
        t.daemon=True
        t.start()
for worker in range(1,50):
    q.put(worker)
q.join()

