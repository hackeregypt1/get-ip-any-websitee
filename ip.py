import socket
import sys

print ("Type Your Target Website Link: ")
hostname = input()
ip=socket.gethostbyname(hostname)
print ('Host Name Is: ',hostname, '/n' 'Target ip Is: ',ip)
