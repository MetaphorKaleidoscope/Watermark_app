# Image Watermarking Desktop App
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk, ImageFont, ImageDraw
import os


filetypes = (
    ('image files', '*.jpg'), ('image files', '*.png'), ('image files', '*.bmp'), ('image files', '*.ico'),
    ('All files', '*.*')
)


global image, filepath, width, height

# Computer user
n3 = os.environ["COMPUTERNAME"]
user_name = n3.replace('-PC', '')


def add_logo_image(e_lg):
    global image, filepath, width, height, user_name
    logoname = fd.askopenfilename(filetypes=filetypes)
    logopath = os.path.abspath(logoname)
    logo = Image.open(logopath)
    w, h = logo.width, logo.height
    logo = logo.resize((w, h), Image.Resampling.LANCZOS)
    # paste logo
    image.paste(logo, (width - w - 5, height - h - 5))
    # save image
    image.save(f"C:/Users/{user_name}/Desktop/save_image.png")
    # wait a milliseconds to update image
    window.after(2000)
    show_image()
    e_lg.destroy()


def edit_lg():
    e_lg = Toplevel()
    e_lg.title("Add watermark logo")
    e_lg.minsize(width=150, height=150)
    e_lg.config(padx=80, pady=80)
    # Button select logo
    add_text = Button(e_lg, text="select logo", command=lambda: add_logo_image(e_lg))
    add_text.pack(padx=5, pady=5)


def add_text_image(text_watermark, e_text):
    global image, filepath, width, height, user_name
    # edit section
    text_font = ImageFont.truetype("arial.ttf", size=50)
    # Get text to add to image
    text_add = text_watermark.get()
    size = text_font.getsize(text_add)
    # edit image
    edit_image = ImageDraw.Draw(image)
    edit_image.text((width-size[0]-5, height-size[1]-5), text_add, "white", font=text_font)
    # save image
    image.save(f"C:/Users/{user_name}/Desktop/save_image.png")
    # clear input box
    text_watermark.delete(0, END)
    # wait a milliseconds to update image
    window.after(2000)
    show_image()
    e_text.destroy()


def show_image():
    global filepath, user_name
    new_pic = Image.open(f"C:/Users/{user_name}/Desktop/save_image.png")
    resized = new_pic.resize((800, 600), Image.Resampling.LANCZOS)  #
    new_pic = ImageTk.PhotoImage(resized)
    display.configure(bg='black')
    display.config(image=new_pic)
    display.image = new_pic


def edit_txt():
    e_text = Toplevel()
    e_text.title("Add watermark text")
    e_text.minsize(width=150, height=150)
    e_text.config(padx=80, pady=80)  # padding
    # entry text
    text_watermark = Entry(e_text, width=10, font=("Helvetica", 15))
    text_watermark.pack(padx=5, pady=5)
    # Button
    add_text = Button(e_text, text="add text to image", command=lambda: add_text_image(text_watermark, e_text))
    add_text.pack(padx=5, pady=5)


def edit_w():
    edit_window = Toplevel()
    edit_window.title("Edit watermark")
    edit_window.minsize(width=150, height=150)
    edit_window.config(padx=80, pady=80)
    # edit section
    edit_text = Button(edit_window, text='add text', command=edit_txt)
    edit_logo = Button(edit_window, text='add logo', command=edit_lg)
    edit_text.pack(padx=10, pady=10)
    edit_logo.pack(padx=10, pady=10)


def select_img():
    global image, filepath, width, height
    filename = fd.askopenfilename(filetypes=filetypes)
    filepath = os.path.abspath(filename)
    image = Image.open(filepath)
    width, height = image.width, image.height
    resized = image.resize((800, 600), Image.Resampling.LANCZOS)  #
    new_pic = ImageTk.PhotoImage(resized)
    display.config(image=new_pic)
    display.image = new_pic
    edit_w()


# creating a window
window = Tk()
window.title("Watermarkly")
window.minsize(width=1000, height=600)
window.configure(bg='black')

# frame
left_frame = Frame(window, width=200, height=600, bg='black')
left_frame.pack(side='left', fill='y')
# # canvas
canvas = Canvas(window, width=800, height=600)
canvas.configure(bg='black')
canvas.pack()

# select image
select_image = Button(left_frame, text='select image', command=select_img)
select_image.pack(padx=5,  pady=5, ipadx=5,  ipady=5)
close_window = Button(left_frame, text='close', command=window.destroy)
close_window.pack(padx=5,  pady=5, ipadx=5,  ipady=5)


display = tkinter.Label(canvas)  # create label once
display.pack(expand=1)
display.configure(bg='black')


window.mainloop()
