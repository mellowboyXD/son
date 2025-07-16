import speech_recognition as sr

local = False

r = sr.Recognizer()
r.dynamic_energy_threshold = True

print("Listening...")
while True:
    try:
        with sr.Microphone() as mic:
            r.adjust_for_ambient_noise(mic)
            audio = r.listen(mic)
            try:
                txt = r.recognize_sphinx(audio) if local else r.recognize_google(audio) # type: ignore
                print(txt)
            except sr.UnknownValueError:
                print("Did not understand what you were saying")
            except sr.RequestError as err:
                print(f"Google Error: {err}")
    except KeyboardInterrupt:
        break