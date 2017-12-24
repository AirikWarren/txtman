#!/usr/bin/python3
import pyperclip
import sys

if len(sys.argv) < 2 or len(sys.argv) > 2:
	print("Usage: txtman -[option]")
	sys.exit()

str = pyperclip.paste()
mode = sys.argv[1]

if (mode == '-a' or mode == '--aesthetic'):
	pyperclip.copy(' '.join(str))
	print(' '.join("aestheticized") + " text copied to clipboard")
elif (mode == '-c' or mode == '--capitalize'):
	pyperclip.copy(str.upper())
	print("capitalized text copied to clipboard".upper())
elif (mode == '-h' or mode == '--help'):
	print(' '.join("aestheticized") + " text" + " -a or --aesthetic".rjust(30))
	print("capitalized".upper() + " text" +  " -c or --capitalize".rjust(45))
	print("display this message" +  " -h or --help".rjust(35))
	sys.exit()
else:
	print("Usage: txtman -[option]")
