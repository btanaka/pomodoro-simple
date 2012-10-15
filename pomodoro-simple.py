#!/usr/bin/env python
"""
pomodoro-simple.py -- a simple pomodoro timer to run in the shell. 
uses mac os x 'say'
"""

import time
import subprocess
import sys

class Pomodoro:

	def __init__(self):
		self.say_cmd = "/usr/bin/say end of " # mac os x only
		self.sleepiness = 60 
		self.work_period = 25
		self.rest_period = 5

	def timer(self, message, time_remaining):
		print "%s for %s minutes" % (message, str(time_remaining))
		while time_remaining > 0:
			sys.stdout.write(str(time_remaining) + " ")
			sys.stdout.flush()
			time.sleep(self.sleepiness)
			time_remaining -= 1
		p = subprocess.Popen(self.say_cmd + message, shell=True)
		p.wait()
		print "\n"

def main():
	doro = Pomodoro()
	while True:
		doro.timer("rest", doro.rest_period)
		doro.timer("work", doro.work_period)

if __name__ == "__main__":
	main()
