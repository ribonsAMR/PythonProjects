# Downloading using Threads and Queues

## References:

**General references [here](/../../#general-references-important)**

- `threading.Thread`: https://docs.python.org/3/library/threading.html#threading.Thread
- `Thread.start()`: https://docs.python.org/3/library/threading.html#threading.Thread.start
- `Thread.join()`: https://docs.python.org/3/library/threading.html#threading.Thread.join
- `threading.Lock`: https://docs.python.org/3/library/threading.html#lock-objects
- `queue.Queue`: https://docs.python.org/3/library/queue.html#module-queue
- `urllib.request.urlopen`: https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen
- `urllib.parse.urlparse`: https://docs.python.org/3/library/urllib.parse.html#urllib.parse.urlparse
- `os.path.basename`: https://docs.python.org/3/library/os.path.html#os.path.basename
- `os.path.exists`: https://docs.python.org/3/library/os.path.html#os.path.exists

### Concurrency tutorials:
1. https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python
2. https://www.oreilly.com/learning/python-cookbook-concurrency
3. https://code.tutsplus.com/articles/introduction-to-parallel-and-concurrent-programming-in-python--cms-28612
4. https://agiliq.com/blog/2013/09/understanding-threads-in-python/

## How to use:
Using Threads: `python3.6 dler.py`<br>
Using Queues: `python3.6 dler2.py`

You will be asked to enter the urls you want to download, leaving the line blank will stop the input process and will start the downloading, `-c` will cancel the input process and get back to the main loop.

The `general.py` file is for any use, edit `the_function` to fit your needs.

**Note:** Please read the comments and check out the references.
