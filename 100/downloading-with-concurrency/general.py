"""
Using Threads, Lock and Queues
"""
from queue import Queue
from threading import Thread, Lock
import os
import time

lock = Lock()

# Edit this to suit your needs
# Note: Use a lock to prevent the race condition.


def the_function(arg):
  pass


class TheThread(Thread):

  def __init__(self, queue):
    super().__init__()
    self.queue = queue

  def run(self):
    arg = self.queue.get()
    the_function(arg)
    self.queue.task_done()


def main():
  # The list of data to push to the queue later
  my_list = []

  q = Queue()

  for i in range(10):
    worker = TheThread(q)
    worker.daemon = True
    worker.start()

  # Push the data one by one to the queue
  for i in my_list:
    q.put(i)

  # Prevent the script from quiting early till the queue finishes.
  q.join()


if __name__ == '__main__':
  main()
