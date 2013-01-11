#MorseCode.py
import sys, time, winsound, pyaudio, wave

CODE_DIC = {'A' : '.-', 	'B' : '-...', 	'C' : '-.-.',
		    'D' : '-..', 	'E' : '.', 		'F' : '..-.',
		    'G' : '--.',	'H' : '....',	'I' : '..',
		    'J' : '.---',	'K' : '-.-',	'L' : '.-..',
		    'M' : '--',		'N' : '-.',		'O' : '---',
		    'P' : '.--.',	'Q' : '--.-',	'R' : '.-.',
		    'S' : '...',	'T' : '-',		'U' : '..-',
		    'V' : '...-',	'W' : '.--',	'X' : '-..-',
		    'Y' : '-.--',	'Z' : '--..',

		    '0' : '-----',	'1' : '.----',	'2' : '..---',
		    '3' : '...--',	'4' : '....-',	'5' : '.....',
		    '6' : '-....',	'7' : '--...',	'8' : '---..',
		    '9' : '----.'}

DIC_CODE = {'.-'   : 'A', 	'-...' : 'B', 	'-.-.' : 'C',
		    '-..'  : 'D', 	'.'    : 'E', 	'..-.' : 'F',
		    '--.'  : 'G',	'....' : 'H',	'..'   : 'I',
		    '.---' : 'J',	'-.-'  : 'K',	'.-..' : 'L',
		    '--'   : 'M',	'-.'   : 'N',	'---'  : 'O',
		    '.--.' : 'P',	'--.-' : 'Q',	'.-.'  : 'R',
		    '...'  : 'S',	'-'    : 'T',	'..--' : 'U',
		    '...-' : 'V',	'.--'  : 'W',	'-..-' : 'X',
		    '-.--' : 'Y',	'--..' : 'Z',

		    '-----' : '0',	'.----' : '1',	'..---' : '2',
		    '...--' : '3',	'....-' : '4',	'.....' : '5',
		    '-....' : '6',	'--...' : '7',	'---..' : '8',
		    '----.' : '9'}

def init():
	INIT_REQ = raw_input("Enter 'E' to input English. \nEnter 'M' to input Morse: ")
	INIT_REQ.upper()
	if(INIT_REQ == 'E'):
		main_eng()
	if(INIT_REQ == 'M'):
		main_mor()
	else:
		print "Please enter 'E' or 'M'"
		init()

def verify_eng(MESSAGE):
	codes = CODE_DIC.keys()
	for char in MESSAGE:
		if char.upper() not in codes and char != ' ' and char != ',':
			print 'Error the charcter ' + char + ' cannot be translated to Morse Code. \nEnter \',\' to quit or use alphanumeric characters only.'
			main_eng()

def main_eng():
	MESSAGE = raw_input('MESSAGE: ')

	verify_eng(MESSAGE)

	if MESSAGE == ",":
		sys.exit(0),
	else:
		for char in MESSAGE:
			if char == ' ':
				print
				time.sleep(3)
			else:
				print CODE_DIC[char.upper()] + " ",
				for char in CODE_DIC[char.upper()]:
					if(char == '.'):
						winsound.Beep(700, 300)
					else:
						winsound.Beep(700, 700)
				time.sleep(0.5)

		print "\n"		
		main_eng()

def verify_mor(MESSAGE):
	for char in MESSAGE:
		if(char != "-" and char != "." and char != ' '):
			print "This is not valid."
			main_mor()

def main_mor():
	TS_REQ = raw_input("Enter 'T' to input TEXT or 'S' to input SOUND, or ',' to QUIT: ")
	if(TS_REQ == 'T'):
		MESSAGE = raw_input('MESSAGE: ')

		verify_mor(MESSAGE)
		letter = ""

		for char in MESSAGE:
			if(char == ' '):
				print DIC_CODE[letter]
				letter = ""
			if(char == '.'):
				letter = letter + '.'
			if(char == '-'):
				letter = letter + '-'

		print ' '

		main_mor()

	if(TS_REQ == 'S'):
		CHUNK = 1024
		FORMAT = pyaudio.paInt16
		CHANNELS = 2
		RATE = 44100
		RECORD_SECONDS = input("Time to record in seconds: ")
		WAVE_OUTPUT_FILENAME = "output.wav"

		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

		print("* recording")

		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)

		print("* done recording")

		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()

		main_mor()

	if(TS_REQ == ','):
		sys.exit(0)

if __name__ == "__init__":
	init()

init()