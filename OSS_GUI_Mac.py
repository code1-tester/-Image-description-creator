from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk, ExifTags
import newthing

def reset_ui():
    image_label.config(image="")
    image_label.image = None
    caption_label.config(text="")
    back_button.pack_forget()
    title_label.pack()
    upload_button.pack()

def upload_image():
    try:
        print("File dialog opened.")
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg"), ("Image files", "*.jpeg"), ("Image files", "*.png"), 
                      ("Image files", "*.bmp"), ("Image files", "*.gif")]
        )
        print(f"Selected file: {file_path}")
        
        if not file_path:  # 파일이 선택되지 않았을 때의 처리
            print("No file selected.")
            caption_label.config(text="No file selected.")
            return

        img = Image.open(file_path)
        img.thumbnail((500, 500))
        print("Image loaded and resized.")

        try:
            exif = img._getexif()
            if exif is not None:
                print("EXIF data found.")
                for tag, value in exif.items():
                    if ExifTags.TAGS.get(tag) == 'Orientation':
                        if value == 3:
                            img = img.rotate(180, expand=True)
                        elif value == 6:
                            img = img.rotate(270, expand=True)
                        elif value == 8:
                            img = img.rotate(90, expand=True)
                print("EXIF data processed.")
        except (AttributeError, KeyError, IndexError) as e:
            print(f"EXIF error: {e}")

        img_tk = ImageTk.PhotoImage(img)

        image_label.config(image=img_tk)
        image_label.image = img_tk

        try:
            print("Generating caption...")
            caption, translated_caption = newthing.generate_caption(file_path)
            caption_label.config(text=f"Caption: {caption}\nTranslated: {translated_caption}")
            print("Caption generated.")
        except Exception as e:
            print(f"Caption generation error: {e}")
            caption_label.config(text="Error generating caption.")
        
        upload_button.pack_forget()
        title_label.pack_forget()
        back_button.pack(pady=20)
        
    except Exception as e:
        print(f"Error: {e}")
        caption_label.config(text="Error loading image.")

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
upload_button.pack(pady=20)
image_label.pack(pady=20)
caption_label.pack(pady=20)

Quit_Button = Button(Window, text='X', font=('Yu Gothic UI Semibold', 15), fg='white', bg='red', command=Window.destroy)
Quit_Button.place(x=screen_width - 50, y=0, width=50, height=40)

Window.mainloop()
