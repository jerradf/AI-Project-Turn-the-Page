# Waits to detect the given sentence and returns a boolean value.

import speech_recognition as sr


def listen():
  r = sr.Recognizer()

  with sr.Microphone() as source:
    audio = r.listen(source)

    try:
      text = r.recognize_google(audio)
      return text
    except:
      print("could not hear.")


def determine_phrase(s, text):
  # s is the last sentence; text is the speech spoken
  if text in s:
    return True
  return False
