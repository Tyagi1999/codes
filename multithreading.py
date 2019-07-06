import threading
def f1():
    for i in range(100):
        print(" f1: "+str(i))
def f2():
    for i in range(100):
        print(" f2: "+str(i))
t1=threading.Thread(target=f1)
t2=threading.Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()
print("hello")
