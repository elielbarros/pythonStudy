"""
# English
 - Threads -

# Portuguese
 - Threads -

"""
from threading import Thread
from time import sleep


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time
        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


t1 = MyThread('Thread 1', .5)
t1.start()

t2 = MyThread('Thread 2', 1)
t2.start()

t3 = MyThread('Thread 3', 1.5)
t3.start()

for i in range(10):
    print(i)
    sleep(.5)

