"""
Using Threads, Lock and Queues
"""
from queue import Queue, Empty
from threading import Thread, Lock
from urllib.request import urlopen, urlparse
import os, time

lock = Lock()

def download(url):
	lock.acquire()

	filename = os.path.basename(url)
	counter = 1

	while os.path.exists(filename):
		filename = str(counter) + "-" + os.path.basename(url)
		counter += 1

	print(filename)
	open(filename, 'w').close() # reserve the file name

	lock.release()

	# Download the file
	with urlopen(url) as urlfile, open(filename, 'wb') as file:
		file.write(urlfile.read())

class DownloadThread(Thread):
	def __init__(self, queue):
		super().__init__()
		self.queue = queue

	def run(self):
		while True:
			#print("Downloading: %s" %os.path.basename(self.url))
			url = self.queue.get()
			download(url)
			self.queue.task_done()

def take_urls() -> "list of urls":

	urls: list = []

	print("Input urls below, leave it blank to stop, '-c' to cancel:")

	while True:
		user_input = input("-> ")
		if not user_input: #break
			break

		if user_input.lower() == "-c": return False

		if not urlparse(user_input).scheme:
			print("Enter a valid url: http(s)//www.name.domain.")
			continue

		urls.append(user_input)

	return urls if urls else False

def main():
	q = Queue()

	for i in range(10):
		worker = DownloadThread(q)
		worker.daemon = True
		worker.start()

	urls = take_urls()

	for i in urls:
		q.put(i)

	q.join()

if __name__ == '__main__':
	main()