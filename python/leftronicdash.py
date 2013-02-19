#!/usr/bin/env python

from leftronic import Leftronic 
import random, time

update = Leftronic("wIwPY46fAhaxv9gq2lxdcRah7YC8QUvM")

def updateLineChart(number):
	update.pushNumber("nWJMk36I", number)

def main():
	#count = 0
	while True:
		number = random.randrange(1,100)
		updateLineChart(number)
		#count+=1
		time.sleep(5)

main()
