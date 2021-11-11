from pynput import keyboard

x = 0


def execute_keypress():
  keyboard.press('e')


def on_press(key):
    global x
    try:
        if key.char == 'e':
          x += 1
    except:
        pass
            

def on_release(key):
    if key == keyboard.Key.esc:
        return False


listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()

