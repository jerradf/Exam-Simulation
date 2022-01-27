# file.py
# Jerrad Flores


import os
from datetime import datetime


def text_files():
  files = []
  os.chdir('Test Prompts')
  for f in os.listdir():
    if f.endswith(".txt"):
      files.append(f)
  os.chdir('..')
  return files


def retrieve_prompt(file_name):
  os.chdir('Test Prompts')
  f = open(file_name, "r")
  contents = f.read()
  f.close()
  os.chdir('..')
  return contents


def write_submission(s):
  f = open("submission.txt", 'w')
  f.write("\nTime of submission: {}\n\nSubmission Transcript (Essay):\n\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
  f.write(s)
  f.write("\n\n\n")
  f.close()


def write_movements(detector, l):
  file_name = "{}.txt".format(detector)
  f = open(file_name, "w")
  f.write("--------------------------------------\n\n\nFor Developers Only - Mouse Coordinates Continuously Tracked\n")
  f.write("Time of submission: {}\n\n\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
  if detector == "mouse":
    for movement in l:
      f.write("{}\n".format(str(movement)))
  elif detector == "sound":
    f.write("Time remained silent: {}".format(str(l)))
  f.close()