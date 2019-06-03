#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import glob
import serial
import time
import urllib.request


def serial_ports():
	ports = []
	if sys.platform.startswith('win'):
		ports = ['COM%s' % (i + 1) for i in range(256)]
	elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
		# this excludes your current terminal "/dev/tty"
		ports = glob.glob('/dev/ttyACM*')
		if ports == []:
			ports = glob.glob('/dev/tty.usb*')
		print(ports)
	elif sys.platform.startswith('darwin'):
		ports = glob.glob('/dev/tty.usb*')
	else:
		raise EnvironmentError('Unsupported platform')

	result = ports
	return result


# types: Sonar - sonar arduino, Box - box controlling arduino
# returns serial connection
def connect_to():
	arduinos = serial_ports()
	print(arduinos)
	ser = []
	box, light = None, None
	while box == None and light == None:
		for i in range(len(arduinos)):
			ser.append(serial.Serial(arduinos[i], 115200))
			time.sleep(3)
			ser[i].write("?".encode())
			types = ser[i].readline().strip().decode("utf-8")
			print(types)
			if types == "Box" and box == None:
				box = ser[i]
	return box


def action(i, ser):
	ser.write(str(i).encode())
	door = ser.readline().strip().decode("utf-8")
	print(door)


if __name__ == "__main__":
	print()
	print(glob.glob('/device/tty.*'))
	print()
	print()
	box = connect_to()
	action(1, box)
