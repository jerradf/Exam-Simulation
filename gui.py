# gui.py
# Jerrad Flores

# Runs the window for the exam,
# along with all other pop-ups for warnings and info.

import tkinter
import tkinter.messagebox
from tkinter import font
import time
import file
import mouse_detector
import random


def display_warnings():
  tkinter.messagebox.showinfo(title = "Warning", message = "We detected 3 cheating movements")



class GUI:
  def __init__(self):
    # Display the necessary infomation before the exam begins!

    # Window (initialize it, set the title, change the dimension)
    self.mouse_detector = mouse_detector.MouseDetector()
    self.window = tkinter.Tk()
    self.window.title("Exam")
    self.window.geometry("450x415")

    # Create a font (that we can use)
    self.myFont = tkinter.font.Font(family="Times New Roman", size=15, weight="bold")
    self.examFont = tkinter.font.Font(family="Times New Roman", size=10, weight="bold")

    # Create a button (initialize it, change the font {optional}, pack the button)
    # where the master is located, and the text you want the beginning of the textbox to say
    # update the font
    # pack the button

    self.textbox = tkinter.Text(master= self.window)
    self.textbox["font"] = self.examFont
    self.textbox.pack()
  
  
  def action(self):
    print("Violation")


  def choose_test(self):
    test_files = file.text_files()
    test_chosen = random.randint(0, len(test_files)-1)
    test_string = file.retrieve_prompt(test_files[test_chosen])
    return test_string

      

  def show_test_info(self):
    prompt = self.choose_test()
    tkinter.messagebox.showinfo(title = "Test Information", message = prompt+"\nPlease keep your mouse in the screen and please keep your face in the test area.")


  def run_mouse_detector(self, event):
    detection = self.mouse_detector.detector(event)
    print(detection)
    if detection == True:
      print("Oh no!")
      self.window.destroy()
      display_warnings()
      return False


  def run(self):
    self.choose_test()
    self.show_test_info()

    self.window.bind("<Motion>", self.run_mouse_detector)
    self.window.mainloop()