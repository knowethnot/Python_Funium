import socket
import threading
from queue import Queue

print_lock = threading.Lock()
target = input('[Enter] <===> (Your Target Host) <----> ')

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		conn = s.connect((target,port))
		with print_lock:
			print('\n[+] port', port, ' is open!')
			conn.close()
	except:
		pass

def Thread():
	while True:
		bot = q.get()
		portscan(bot)
		q.task_done()
	
q = Queue()

def Main():

	for x in range(30):
		t = threading.Thread(target=Thread)
		t.daemon = True
		t.start()

	for bot in range(1, 240001):
		q.put(bot)

	q.join()

if __name__ == '__main__':
	Main()
