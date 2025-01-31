import keyboard

def data():
    keyboard.write("{{ _(")

def data_2():
    keyboard.write(") }}")

keyboard.add_hotkey("F8", lambda: data())
keyboard.add_hotkey("F9", lambda: data_2())

keyboard.wait()