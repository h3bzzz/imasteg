import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def embed_payload():
    payload = payload_entry.get()
    if not payload:
        messagebox.showerror("Error", "Please enter a payload")
        return

    # Allow selection of multiple image types
    file_path = filedialog.askopenfilename(filetypes=[
        ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"),
        ("All Files", "*.*")
    ])
    if not file_path:
        messagebox.showerror("Error", "Please select an image")
        return

    try:
        image = Image.open(file_path)
        if image.mode != "RGB":
            image = image.convert("RGB")
        pixels = image.load()

        # Convert payload to binary
        binary_payload = ''.join(format(ord(char), '08b') for char in payload) + '00000000'
        binary_index = 0

        # Embed payload in image
        for y in range(image.height):
            for x in range(image.width):
                if binary_index < len(binary_payload):
                    r, g, b = pixels[x, y]

                    # Modify the least significant bit of the red channel
                    r = (r & ~1) | int(binary_payload[binary_index])
                    binary_index += 1

                    pixels[x, y] = (r, g, b)

        # Automatically save in the current directory
        script_dir = os.getcwd()  # Get the current working directory
        file_name = "modified_image.png"
        save_path = os.path.join(script_dir, file_name)

        image.save(save_path)
        messagebox.showinfo("Success", f"Payload embedded and image saved at: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("IMASTEG")

tk.Label(root, text="Enter Payload: ").pack(pady=5)
payload_entry = tk.Entry(root, width=50)
payload_entry.pack(pady=5)

embed_button = tk.Button(root, text="Embed Payload", command=embed_payload)
embed_button.pack(pady=20)

root.mainloop()

