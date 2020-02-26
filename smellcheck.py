from PyDictionary import PyDictionary
import sys
import serial

port = '/dev/cu.usbserial-1410'
ard = serial.Serial(port,9600,timeout=5)

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")

dict = PyDictionary()

print("Welcome! Type a word and check your spelling! :)")
for line in sys.stdin:
    input = line
    if dict.meaning(input):
        print("Your spelling is correct! Go again!")
    else:
        print("Incorrect spelling! Please try again.")
        scent = 1
        str(scent)
        ard.write(scent)
    scent = 0


