import tkinter as tk
from tkinter import *
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk

# Create tkinter window
window = tk.Tk()
window.title("Smart CCTV")

# Set window icon
window.iconphoto(False, tk.PhotoImage(file='mn.png'))

window.geometry('1080x760')

# Create frame
frame1 = tk.Frame(window)

# Label for title
label_title = tk.Label(frame1, text="Smart CCTV Camera")
label_font = font.Font(size=35, weight='bold', family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10, 10), column=1, columnspan=2)

# Load and resize icon image
icon = Image.open(r'icons\spy.png')
icon = icon.resize((150, 150), Image.BILINEAR)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5, 10), column=1, columnspan=2)

# Load and resize button images
btn1_image = Image.open(r'icons\rectangle-of-cutted-line-geometrical-shape.png')
btn1_image = btn1_image.resize((50, 50), Image.BILINEAR)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open(r'icons\security-camera.png')
btn2_image = btn2_image.resize((50, 50), Image.BILINEAR)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open(r'icons\incognito.png')
btn3_image = btn3_image.resize((50, 50), Image.BILINEAR)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open(r'icons\recording.png')
btn4_image = btn4_image.resize((50, 50), Image.BILINEAR)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open(r'icons\exit.png')
btn5_image = btn5_image.resize((50, 50), Image.BILINEAR)
btn5_image = ImageTk.PhotoImage(btn5_image)

# Button fonts
btn_font = font.Font(size=25)

# Buttons
btn1 = tk.Button(frame1, text='Rectangle', height=90, width=180, fg='orange', command=rect_noise, compound='left', image=btn1_image)
btn1['font'] = btn_font
btn1.grid(row=3, pady=(20, 10), column=1, padx=(20, 5))

btn2 = tk.Button(frame1, text='Noise', height=90, width=180, fg='green', command=noise, image=btn2_image, compound='left')
btn2['font'] = btn_font
btn2.grid(row=3, pady=(20, 10), column=2, padx=(20, 5))

btn3 = tk.Button(frame1, text='In Out', height=90, width=180, fg='green', command=in_out, image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=4, pady=(20, 10), column=1, padx=(20, 5))

btn4 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=4, pady=(20, 10), column=2, padx=(20, 5))

btn5 = tk.Button(frame1, height=90, width=180, fg='red', command=window.quit, image=btn5_image)
btn5['font'] = btn_font
btn5.grid(row=5, pady=(20, 10), column=1, columnspan=2)

frame1.pack()
window.mainloop()
