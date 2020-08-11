from tkinter import *
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk
from pytube import YouTube
from threading import *
from tkinter.messagebox import askyesno

file_size = 0


def downThread():
    thread = Thread(target=downloader)
    thread.start()


def progress(chunk, file_handle, remaining):
    global download_status
    file_downloaded = file_size - remaining
    per = (file_downloaded/file_size)*100
    MB = float(1024 ** 2)
    status = "{0:.0f} MB".format(file_downloaded/MB), " of ", "{0:.0f} MB".format(file_size/MB)
    download_status.config(text='{:00.0f} % downloaded'.format(per))
    size_status = Label(root, text=status, font=('Verdana', 15), bg='white')
    size_status.place(x=260, y=275)


def downloader():
    global file_size, download_status
    download_button.config(state=DISABLED)
    download_status.place(x=270, y=250)
    try:
        url1 = url.get()
        path = askdirectory()
        yt = YouTube(url1, on_progress_callback=progress)
        video = yt.streams.filter(progressive=True, file_extension='mp4').first()
        file_size = video.filesize
        video.download(path)
        download_status.config(text='Download completed...')
        res = askyesno("Youtube Video Downloader", "Do you want to download another video?")
        if res == 1:
            url.delete(0, END)
            download_button.config(state=NORMAL)
            download_status.config(' ')
        else:
            root.destroy()
    except Exception as err:
        download_status.config(text='Error !, Some Error Encountered...')


root = Tk()
root.geometry('740x400')
# root.iconbitmap('icon.ico')
root.title('Youtube Video Downloader')
root['bg'] = 'white'
root.resizable(0, 0)
img = Image.open('youtube.jpg')
img = img.resize((300, 80), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
head = Label(root, image=img)
head.config(anchor=CENTER)
head.pack()

enter_url = Label(root, text='Enter URL: ', bg='white')
enter_url.config(font=('Verdana', 14))
enter_url.place(x=7, y=123)
tagline = Label(root, text='HackersBrain', bg='white')
tagline.config(font=('Verdana', 14))
tagline.place(x=602, y=123)
url = Entry(root, width=35, border=1, relief=SUNKEN, font=('Verdana', 15))
url.place(x=125, y=123)

download_button = Button(root, text='Download', bg='white', relief=FLAT, command=downThread)
download_button.place(x=320, y=170)
download_status = Label(root, text='Please wait...', font=('Verdana', 15), bg='white')
root.mainloop()
