import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def cnScan(tgtHost, tgtPort):
	
	try:
		cnSock = socket(AF_INET, SOCK_STREAM)
		cnSock.connect((tgtHost, tgtPort))
		cnSock.send('Yosha\n')

		furence = cnSock.recv(100)
		screenLock.acquire()
		print "[+] " + str(tgtPort) + "/tcp open"

	except:
		screenLock.acquire()
		print "[-] " + str(tgtPort) + "/tcp closed"

	finally:
		screenLock.release()
		cnSock.close()

def portScan(tgtHost, tgtPorts):

	try:
		tgtIP = gethostbyname(tgtHost)

	except:
		print "[-] Can not resolve" + tgtHost + ", Unknown Host!"
		return 

	try:
		tgtName = gethostbyaddr(tgtIP)
		print "\n[+] Scan Results For: " + tgtName[0]

	except:
		print "\n{[+] Scan Results For: " + tgtIP

	setdefaulttimeout(1)
	for tgtPort in tgtPorts:
		t = Thread(target=cnScan, args=(tgtHost, int(tgtPort)))
		t.start()

def Main():

	parser = optparse.OptionParser('usage %prog -H = Target Host' + '-p = Targegt Ports')
	parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
	parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports')
	(options, args) = parser.parse_args()
	if (options.tgtHost == None) | (options.tgtPort == None):
		print parser.usage
		exit(0)
	else:
		tgtHost = options.tgtHost
		if '-' in str(options.tgtPort):
			tgtPorts = options.tgtPort.split('-')
			tgtPorts = range(int(tgtPorts[0]), int(tgtPorts[1]))
		else:
			tgtPorts = str(options.tgtPort).split(',')

	portScan(tgtHost,tgtPorts)	

if __name__ == '__main__':
	Main()	
