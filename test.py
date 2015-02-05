import speech_recognition as speech_recognition
r = sr.Recognizer

with sr.WavFile("test.wav") as source:
	audio = r.record(source)
	try:
		print "Transcription" + r.recognize(audio)
	except LookupError:
		print "nope, didn't understand"