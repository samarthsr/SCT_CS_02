
🔒 Image Encryption Tool

A Python program to encrypt and decrypt images using pixel manipulation techniques. This tool demonstrates how to use basic image processing operations for lightweight security, offering a fun and educational introduction to image encryption.

🚀 Features

Pixel Swapping: Swap the first and last pixels of each row to obscure the image.

Mathematical Transformations: Apply arithmetic operations (e.g., addition, subtraction, multiplication, division) to alter pixel values.

Encryption and Decryption: Easily encrypt images and restore them to their original form by reversing the applied transformations.

Multi-Format Support: Compatible with common formats like PNG and JPEG.

📋 How It Works
The tool manipulates pixel values to encrypt images. It uses the following workflow:

Encryption Process:

Load the image using the Pillow library.

Convert the image into a numpy array for pixel-level operations.

Perform a selected operation on each pixel, such as:

Swap: Swap the first and last pixels in each row.

Add/Subtract: Add or subtract a constant value to/from each pixel.

Multiply/Divide: Multiply or divide each pixel by a constant value.

Convert the modified array back to an image.

Save the encrypted image.

Decryption Process:

Load the encrypted image.

Reverse the applied transformations using the same operation and parameters (e.g., subtracting the added value, swapping pixels back).

Save the decrypted image to verify restoration.

🛠️ Installation & Usage

Prerequisites

Python 3.7 or later

Install required libraries:

pip install pillow numpy

Steps

Clone the repository:

git clone https://github.com/samarthsr/SCT_CS_02.git
cd Image_encryption.py


# Example usage
image_path = r"<Enter the path to your input image here>"
encrypted_image = encrypt_image(image_path, 'swap')
encrypted_image.save(r"<Enter the path to save your encrypted image here>")

Customize operations by editing the Python script as needed.

📚 Concepts Covered

Image Processing Basics: Understand how to work with image matrices.

Python Libraries: Gain hands-on experience with Pillow and numpy.

Basic Security Principles: Learn how transformations can obscure visual data.

🤝 Contributing
Contributions are welcome! Feel free to fork the repository, submit pull requests, or open issues for feature suggestions.

🛡️ License
This project is licensed under the MIT License. See the LICENSE file for details.

🌟 Acknowledgments

Python Documentation: https://docs.python.org

Open Source Contributions: Community insights and examples.

📧 Contact
For questions or feedback, please reach out to samarthsr333@gmail.com.
