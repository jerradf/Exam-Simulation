# file.py
# Jerrad Flores


import os


def text_files():
  files = []
  for f in os.listdir():
    if f.endswith(".txt"):
      files.append(f)
  return files


def retrieve_prompt(file_name):
  # 1.) Open a file
  # "r" -> read
  # "w" -> write (overwrite entire file)
  # "a" -> write (append to the back of file)
  f = open(file_name, "r")

  # 2.) Read the contents
  contents = f.read()

  # 3.) Close the file
  f.close()

  return contents