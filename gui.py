# gui.py
# Jerrad Flores

# Runs the window for the exam,
# along with all other pop-ups for warnings and info.

# Swiftly installs dependencies in the background

import tkinter
import tkinter.messagebox
from tkinter import font
import time
import file
import md
import sd
import email_sender
import random


def display_warnings():
  tkinter.messagebox.showinfo(title = "Warning", message = "Cheating Detected. Exam Window Closed.")
  quit()


def display_success():
  tkinter.messagebox.showinfo(title = "Success", message = "Successfully submitted exam.\n")
  quit()


class GUI:
  def __init__(self):
    # Display the necessary infomation before the exam begins!
    # Window (initialize it, set the title, change the dimension)
    self.te = email_sender.send_email()
    self.mouse_detector = md.MouseDetector()
    self.sound_detector = sd.SoundDetector()
    self.window = tkinter.Tk()
    self.window.title("Exam")
    self.window.geometry("450x415")

    # Create a font (that we can use)
    self.myFont = tkinter.font.Font(family="Times New Roman", size=15, weight="bold")
    self.examFont = tkinter.font.Font(family="Times New Roman", size=10, weight="bold")

    # Create our submit button for the exam
    self.submit_button= tkinter.Button(self.window, height=1, width=10, bg="white", command= self.submission,text=("Submit Exam"))
    self.submit_button["font"] = self.myFont
    self.submit_button.pack()

    # Create our textbox for the user to type.
    self.textbox = tkinter.Text(master= self.window)
    self.textbox["font"] = self.examFont
    self.textbox.pack()
  
  
  def write_files(self):
    s = self.textbox.get("1.0", "end")
    file.write_submission(s)
    file.write_movements("mouse", self.mouse_detector.mouse_movements)


  def submission(self):
    self.write_files()
    email_sender.send_message(self.te, "SUCCESS")
    self.window.destroy()
    display_success()


  def choose_test(self):
    test_files = file.text_files()
    test_chosen = random.randint(0, len(test_files)-1)
    test_string = file.retrieve_prompt(test_files[test_chosen])
    return test_string


  def show_test_info(self):
    prompt = self.choose_test()
    tkinter.messagebox.showinfo(title = "Test Information", message = prompt+"\nPlease keep your mouse in the screen and please keep your face in the test area.")


  def cheating_actions(self, *args):
    self.write_files()
    email_sender.send_message(self.te, "FAILURE - CHEATING DETECTED\n")
    self.window.destroy()
    display_warnings()


  def run_mouse_detector(self, event):
    detection = self.mouse_detector.detector(event)
    if detection == True: #Cheating detected
      self.cheating_actions()


  def run_sound_detector(self, *args):
    detection = self.sound_detector.detector()
    if detection == True: #Cheating detected
      self.cheating_actions()
    else:
      self.window.after(10, self.run_sound_detector)


  def run(self):
    self.choose_test()
    self.show_test_info()
    self.window.after(10, self.run_sound_detector)
    self.window.bind("<Motion>", self.run_mouse_detector)
    self.window.mainloop()
