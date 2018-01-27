"""
Using Threads and Lock
"""
from threading import Thread, Lock
from urllib.request import urlopen, urlparse
import os, time

def download(url, lock):
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
	def __init__(self, url, lock):
		super().__init__()
		self.url = url
		self.lock = lock

	def run(self):
		#print("Downloading: %s" %os.path.basename(self.url))
		download(self.url, self.lock)

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

	"""
	if urls:
		return urls
	else:
		return False
	"""
	return urls if urls else False

def main():
	lock = Lock()
	try:
		urls = take_urls()
		if urls:
			threads = [DownloadThread(i, lock) for i in urls]
			for i in threads: i.start()
			
			for i in threads: i.join()
				
			print("Downloading is done. 👌")

	except KeyboardInterrupt:
		print("\nGoodbye! 👋")
		exit(0)

if __name__ == '__main__':
	main()