import tkinter as tk
from file_downloader import download_file

root = tk.Tk()
root.title("File Downloader")
root.geometry("500x200")

def buttonCall():
    pass

# label enter url
urlLabel = tk.Label(root, text="URL")
# urlLabel.pack(padx=10,pady=10)
urlLabel.grid(row=0,column=0)

# url entry
urlInput = tk.Entry(root)
# urlInput.pack(padx=10,pady=10)
urlInput.grid(row=0,column=1)

# label enter filename
filenameLabel = tk.Label(root,text="FileName")
filenameLabel.grid(row=1, column=0)

# filename entry
filenameInput = tk.Entry(root)
filenameInput.grid(row=1, column=1)

# button
downloadButton = tk.Button(root, text="Download", command=buttonCall)
downloadButton.grid(row=2, column=1)


root.mainloop()