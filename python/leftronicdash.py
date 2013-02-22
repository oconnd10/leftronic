#!/usr/bin/env python

from os import fork, chdir, setsid, umask
from sys import exit
from leftronic import Leftronic 
import random, time

update = Leftronic("wIwPY46fAhaxv9gq2lxdcRah7YC8QUvM")

def updateCharts():
    number = random.randrange(1,100)
    update.pushNumber("nWJMk36I", number)
    number = random.randrange(1,100)
    update.pushNumber("oCbSJpaF", number)
    number = random.randrange(1,100)
    update.pushNumber("DHKGwiRq", number)
    number = random.randrange(1,100)
    update.pushNumber("brgmlTxV", number)
    number1 = random.randrange(1,100)
    number2 = random.randrange(1,100)
    update.pushPair("aPbTK98T", number1, number2)

def main():
	update.clear("aPbTK98T")
	update.clear("brgmlTxV")
	while True:
		updateCharts()
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
