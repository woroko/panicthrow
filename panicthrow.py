#!/usr/bin/env python3
#Copyright 2018 John Mäkelä

import pygame, time, math, os

#SETTINGS_ALPHA = 0.2846
SETTINGS_ALPHA = 0.44313727585
#(sampling_rate/cutoff_freq)/(2*pi+(sampling_rate/cutoff_freq))

class HighPass:
	def __init__(self, alpha):
		self.alpha = alpha
		self.lastOutput = 0.0
		self.lastInput = 0.0
		self.started = False
	def update(self, x):
		if (not self.started):
			self.lastInput = x
			self.started = True
		self.lastOutput = self.alpha*(self.lastOutput+x-self.lastInput)
		self.lastInput = x
		return self.lastOutput
def main():
	pygame.init()
	pygame.joystick.init()
	joy_count = pygame.joystick.get_count()
	print(joy_count)
	joy = pygame.joystick.Joystick(0)
	joy.init()
	hpfx = HighPass(SETTINGS_ALPHA)
	hpfy = HighPass(SETTINGS_ALPHA)
	hpfz = HighPass(SETTINGS_ALPHA)

	while True:
		pygame.event.get()
		x = joy.get_axis(0)
		y = joy.get_axis(1)
		z = joy.get_axis(2)
		hpx = hpfx.update(x)
		hpy = hpfy.update(y)
		hpz = hpfz.update(z)

		magn = math.sqrt(hpx*hpx + hpy*hpy + hpz*hpz)
		#print("X: " + "{:>6.4f}".format(x) + " Y: " + "{:>6.4f}".format(y) + " Z: " 
		#	  + "{:>6.4f}".format(z))

		print("MAGN: " + "{:>6.4f}".format(magn))
		time.sleep(0.5)
		if magn > 0.03:
			print("magn>0.03!!!")
			#os.system("systemctl hibernate")
			return


main()