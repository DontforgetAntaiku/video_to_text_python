import speech_recognition as sr
import os
from moviepy.editor import VideoFileClip
import clipboard
def mp4_to_text(path, lang):
	lang = "ru-RU" if lang == "Ru" else "uk-UK" if lang == "Uk" else "en-US" if lang == "En" else lang
	if path.split('\\')[-1].split(".")[-1] in ['mkv', 'mp4', 'webm', 'avi', 'mov']:  
		mp4_path = path
		audio = VideoFileClip(mp4_path)
		audio = audio.audio.write_audiofile(path + ".wav")
		r = sr.Recognizer()
		with sr.AudioFile(path + ".wav") as source:
			audio = r.record(source)
		text = r.recognize_google(audio, language=lang)
		clipboard.copy(text)
		print(text)
		os.remove(path + ".wav")
	elif path.split('\\')[-1].split(".")[-1] in ['wav', 'mp3', 'aax', 'au', 'm4p', 'wma', 'webm']:
		r = sr.Recognizer()
		with sr.AudioFile(path) as source:
			audio = r.record(source)
		text = r.recognize_google(audio, language=lang)
		clipboard.copy(text)
		print(text)
mp4_to_text(input("Absolute path to video/audio\n"), input("Ru/Uk/En\n"))