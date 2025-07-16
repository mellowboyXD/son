import speech_recognition as sr

word = "son"
count = 0
local = False

r = sr.Recognizer()
r.dynamic_energy_threshold = True


if __name__ == "__main__":
    while True:
        try:
            print("Listening...")
            txt = ""
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic)
                audio_data = r.listen(mic)
                try:
                    txt = r.recognize_sphinx(audio_data) if local else r.recognize_google(audio_data)    # type: ignore
                except sr.UnknownValueError:
                    print("Sorry, could not get that!")
                except sr.RequestError as err:
                    print(f"Request could not be made: {err}")

                if word in txt:
                    print("There you go! He said it.")
                    count += txt.count(word)
        except KeyboardInterrupt:
            print(f"He said it {count} times. Jeez louise!")
            break