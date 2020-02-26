from PyDictionary import PyDictionary
import sys
import serial

port = '/dev/cu.usbserial-1410'
ard = serial.Serial(port,9600,timeout=5)

dict = PyDictionary()
print("Welcome! Type a word, check your spelling, and ignore the initial warning message! :)")
for line in sys.stdin:
    input = line
    if dict.meaning(input):
        pass
    else:
        print("Incorrect spelling! Please try again.")
        scent = 1
        str(scent)
        ard.write(scent)
    scent = 0


