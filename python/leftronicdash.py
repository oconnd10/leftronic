#!/usr/bin/env python

from os import fork, chdir, setsid, umask
from sys import exit
from leftronic import Leftronic 
import random, time

update = Leftronic("wIwPY46fAhaxv9gq2lxdcRah7YC8QUvM")

def getDataFromSM2():
#SM2 API goes here

def updateLineChart(number):
	update.pushNumber("nWJMk36I", number)

def main():
	while True:
		#get data from SM2 function
		#pass it to the leftronic API
		#sleep for set perios of time to avoid rate limits
		number = random.randrange(1,100)
		updateLineChart(number)
		time.sleep(5)

if __name__ == "__main__":
	try:
		pid = fork()
		if pid>0:
			exit(0)
	except OSError, e:
		exit(1)
	chdir("/")
	setsid()
	umask(0)

	try:
		pid = fork()
		if pid>0:
			exit(0)
	except OSError, e:
		exit(1)


main()
