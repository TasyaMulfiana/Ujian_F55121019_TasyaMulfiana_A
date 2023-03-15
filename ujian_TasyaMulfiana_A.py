import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.image = None

    def create_widgets(self):
        # Create label for original image
        self.original_label = tk.Label(self)
        self.original_label.pack(side="left")

        # Create label for processed image
        self.processed_label = tk.Label(self)
        self.processed_label.pack(side="right")

        # Create button to select image
        self.select_button = tk.Button(self, text="Select Image", command=self.select_image)
        self.select_button.pack()

        # Create button to process image with contrast method
        self.contrast_button = tk.Button(self, text="Contrast", command=self.contrast_image)
        self.contrast_button.pack()

        # Create button to process image with brightness method
        self.brightness_button = tk.Button(self, text="Brightness", command=self.brightness_image)
        self.brightness_button.pack()

    def select_image(self):
        # Open file dialog to select image
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])

        # Load selected image and display in original label
        self.image = Image.open(file_path)
        self.original_image = ImageTk.PhotoImage(self.image)
        self.original_label.config(image=self.original_image)

    def contrast_image(self):
        # Check if image is loaded
        if self.image:
            # Process image with contrast method
            processed_image = self.image.point(lambda p: p * 1.5)

            # Display processed image in processed label
            processed_image = ImageTk.PhotoImage(processed_image)
            self.processed_label.config(image=processed_image)
            self.processed_image = processed_image

    def brightness_image(self):
        # Check if image is loaded
        if self.image:
            # Process image with brightness method
            processed_image = self.image.point(lambda p: p + 50)

            # Display processed image in processed label
            processed_image = ImageTk.PhotoImage(processed_image)
            self.processed_label.config(image=processed_image)
            self.processed_image = processed_image


# Create main window and start application
root = tk.Tk()
app = Application(master=root)
app.mainloop()
