import speech_recognition as sr
import argparse

r = sr.Recognizer()
r.dynamic_energy_threshold = True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="clison", 
                                     description="Speech recognition CLI wrapper. Uses Google API by default")
    groups = parser.add_mutually_exclusive_group()
    groups.add_argument("-l", "--local",
                        action="store_true",
                        help="Performs speech recognition offline using Sphinx API")
    groups.add_argument("-w", "--whisper",
                        action="store_true",
                        help="Uses OpenAi Whisper API")
    args = parser.parse_args()._get_kwargs()

    print("Listening...")
    while True:
        try:
            with sr.Microphone() as mic:
                r.adjust_for_ambient_noise(mic)
                audio = r.listen(mic)
                try:
                    # txt = r.recognize_sphinx(audio) if args.local else r.recognize_google(audio) # type: ignore
                    match args:
                        case [("local", True), ("whisper", False)]:
                            txt = r.recognize_sphinx(audio) # type: ignore
                        case [("local", False), ("whisper", True)]:
                            txt = r.recognize_whisper(audio, model="turbo", language="english") # type: ignore
                        case _:
                            txt = r.recognize_google(audio) # type: ignore
                    print(txt)
                except sr.UnknownValueError:
                    print("--- Could not understand ---")
                except sr.RequestError as err:
                    print(f"--- Google Error: {err} ---")
        except KeyboardInterrupt:
            break