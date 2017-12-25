#!/usr/bin/python3
import pyperclip
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
	print("Usage: txtman -[option]")
	sys.exit()

str = pyperclip.paste()
mode = sys.argv[1]
space = ' '

if ('-a' in mode or '--aesthetic' in mode):
	if mode[-1].isdecimal():
		space *= int(mode[-1])
	pyperclip.copy(space.join(str))
	print(space.join("aestheticized") + " text copied to clipboard")
elif (mode == '-c' or mode == '--capitalize'):
	pyperclip.copy(str.upper())
	print("capitalized text copied to clipboard".upper())
elif (mode == '-h' or mode == '--help'):
	print(' '.join("aestheticized") + " text" + " -a[multiplier] or --aesthetic[multiplier]".rjust(54))
	print("capitalized".upper() + " text" +  " -c or --capitalize".rjust(45))
	print("display this message" +  " -h or --help".rjust(35))
	print("\nIf you use an aesthetic multiplier greater than 9 the program will use the")
	print("last digit of the number as the multiplier rather than the whole number.")
	sys.exit()
else:
	print("Usage: txtman -[option]")
