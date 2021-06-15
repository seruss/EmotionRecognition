import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

class App:

 #function displaying selected image
    def showImage(self, filename):
        imageFile = Image.open(filename)
        image = ImageTk.PhotoImage(imageFile)
        imgW, imgH = imageFile.size
        self.label1 = tk.Label(image=image)
        self.label1.image = self.image
        print(filename)

    # Function for opening the
    # file explorer window
    def browseFiles(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                              title = "Select a File",
                                              filetypes = (("JPG files",
                                                            "*.jpg*"),
                                                           ("Png files",
                                                            "*.png*")))
        self.showImage(filename)

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x400")

        self.imageFile = Image.open("pic.png")
        self.imgW, self.imgH = self.imageFile.size

        self.image = ImageTk.PhotoImage(self.imageFile)

        self.label1 = tk.Label(image=self.image)
        self.label1.image = self.image

        # Position image
        self.label1.place(x=200 - self.imgW / 2, y= 200 - self.imgH /2)


        self.showImgButton = tk.Button(self.root, text="Show image", command=self.browseFiles).pack(side = tk.BOTTOM, pady = 15)

        self.label1.pack()

        

        self.root.mainloop()


App = App()



#root = tk.Tk()

#root.geometry("400x400")

#imageFile = Image.open("pic.png")
#imgW, imgH = imageFile.size

#image = ImageTk.PhotoImage(imageFile)

#label1 = tk.Label(image=image)
#label1.image = image

## Position image
#label1.place(x=200 - imgW / 2, y= 200 - imgH /2)

#showImgButton = tk.Button(root, text="Show image", command=browseFiles).pack(side = tk.BOTTOM, pady = 15)

#tk.mainloop()

