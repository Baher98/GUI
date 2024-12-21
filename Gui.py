import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

def play_audio():
    user_text = input_box.get("1.0", "end").strip()
    if user_text:
        try:
            tts_object = gTTS(text=user_text, lang='en')
            tts_object.save("speech.mp3")
            os.system("start speech.mp3")
        except Exception as err:
            messagebox.showerror("Error", f"An error occurred:\n{err}")
    else:
        messagebox.showwarning("Input Error", "Please enter some text.")

def clear_text():
    input_box.delete("1.0", "end")

def close_window():
    window.destroy()

window = tk.Tk()
window.title("Text to Speech App")
window.geometry("400x300")

title_label = tk.Label(window, text="Enter your text here:", font=("Arial", 14))
title_label.pack(pady=10)

input_box = tk.Text(window, height=5, width=40, font=("Arial", 12))
input_box.pack(pady=10)

button_container = tk.Frame(window)
button_container.pack(pady=20)

play_btn = tk.Button(button_container, text="Play", command=play_audio, font=("Arial", 12), fg="white", bg="blue", width=10)
play_btn.grid(row=0, column=0, padx=5)

close_btn = tk.Button(button_container, text="Exit", command=close_window, font=("Arial", 12), fg="white", bg="red", width=10)
close_btn.grid(row=0, column=1, padx=5)

clear_btn = tk.Button(button_container, text="Clear", command=clear_text, font=("Arial", 12), fg="white", bg="orange", width=10)
clear_btn.grid(row=0, column=2, padx=5)

window.mainloop()
