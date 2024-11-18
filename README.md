# imasteg

🖼️ IMASTEG - Image Steganography Tool
IMASTEG is a simple GUI-based Python tool for embedding hidden payloads (text) into images using steganography techniques. 
This project demonstrates how to manipulate image pixels at a binary level to hide data within an image file.

🚀 Features
Payload Embedding:

Input a secret payload (text).
Embed the payload into an image by modifying the least significant bit (LSB) of the red channel of each pixel.
Automatically terminates the payload with a delimiter (00000000 in binary).
Multiple Image Formats:

Supports PNG, JPG, JPEG, BMP, GIF, and TIFF image formats for embedding.
User-Friendly GUI:

Built with Tkinter for ease of use.
File dialog for selecting the image and real-time error handling.

Automated File Saving:
Saves the modified image as modified_image.png in the same directory as the script.

💡 What I Learned
Programming Concepts
Graphical User Interfaces (GUIs):
Designed a simple GUI using Tkinter.
Learned to handle user input, buttons, and dialogs for a seamless user experience.
File Handling:

Used filedialog to browse and select files.
Automatically saved the modified image in a specified location.
Image Manipulation:

Worked with Pillow (PIL) to open, edit, and save images.
Converted payload text into binary and embedded it into image pixels.
Binary Data Handling:

Converted text to binary for LSB manipulation.
Appended a delimiter (00000000) to signify the end of the payload.
Error Handling:

Implemented try-except blocks to gracefully handle errors.
Displayed meaningful error messages with messagebox.
Bitwise Operations:

Used bitwise AND (&) and OR (|) to manipulate the least significant bit of the red channel in RGB values.
🛠️ How to Use
Pillow (PIL) library installed:
pip install pillow

Enter the secret payload in the text box.
Select an image file.
The modified image will be saved as modified_image.png in the current directory.
🌟 Highlights of the Journey
1. Understanding Steganography
Explored how to hide data within image files using the LSB technique.
Learned the importance of a binary delimiter to mark the end of embedded data.
2. Building a GUI
Designed an intuitive interface for non-technical users.
Mastered Tkinter basics, including buttons, labels, and dialogs.
3. Image Processing with Pillow
Manipulated image pixels efficiently.
Ensured compatibility with multiple image formats by converting to RGB.
4. Bit Manipulation
Used bitwise operations to control specific bits of image data without affecting the overall quality.
5. Error Handling and User Experience
Anticipated user errors (e.g., invalid payload, no file selected) and provided clear feedback.

Simplified file saving to ensure ease of access.
📈 What's Next?
Payload Extraction:

Explore embedding payloads in image metadata instead of pixel data.
Batch Processing:

Enable embedding across multiple images in one go.
