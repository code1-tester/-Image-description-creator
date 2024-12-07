from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import newthing

def reset_ui():
    image_label.config(image="")
    image_label.image = None
    caption_label.config(text="")
    back_button.pack_forget()
    title_label.pack()
    upload_button.pack(pady=200)

def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")]
    )
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((400, 400))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk

        caption, translated_caption = newthing.generate_caption(file_path)
        caption_label.config(text=f"Caption: {caption}\nTranslated: {translated_caption}")

        upload_button.pack_forget()
        title_label.pack_forget()
        back_button.pack(pady=20)

Window = Tk()
Window.attributes('-fullscreen', True)
screen_width = Window.winfo_screenwidth()
screen_height = Window.winfo_screenheight()

title_label = Label(Window, text='Image Description Creator', font=('Yu Gothic UI Semibold', 50))
upload_button = Button(Window, text='Upload Image', font=('Yu Gothic UI Semibold', 30), command=upload_image)
back_button = Button(Window, text='Back', font=('Yu Gothic UI Semibold', 30), command=reset_ui)

image_label = Label(Window)
caption_label = Label(Window, font=('Yu Gothic UI', 30), wraplength=800, justify="center")

title_label.pack(pady=200)
upload_button.pack(pady=200)
image_label.pack(pady=50)
caption_label.pack(pady=50)

Quit_Button = Button(Window, text='X', font=('Yu Gothic UI Semibold', 15), fg='white', bg='red', command=Window.destroy)
Quit_Button.place(x=screen_width - 50, y=0, width=50, height=40)

Window.mainloop()