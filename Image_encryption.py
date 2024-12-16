from PIL import Image
import numpy as np

def encrypt_image(image_path, operation):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to a numpy array
    image_data = np.array(image)
    
    # Perform the selected operation on each pixel
    if operation == 'swap':
        # Swap the first and last pixels of each row
        image_data[:, 0, :] = image_data[:, -1, :]
        image_data[:, -1, :] = image_data[:, 0, :]
    elif operation == 'add':
        # Add a constant value to each pixel
        image_data = image_data + 100
    elif operation == 'subtract':
        # Subtract a constant value from each pixel
        image_data = image_data - 100
    elif operation == 'multiply':
        # Multiply each pixel by a constant value
        image_data = image_data * 2
    elif operation == 'divide':
        # Divide each pixel by a constant value
        image_data = image_data / 2
    
    # Convert the modified image data back to an image
    encrypted_image = Image.fromarray(image_data.astype(np.uint8))
    
    return encrypted_image

# Example usage
image_path = r"C:\Users\suhas\OneDrive\Desktop\OIP.jpeg"
encrypted_image = encrypt_image(image_path, 'swap')
encrypted_image.save(r"C:\Users\suhas\OneDrive\Desktop\IMAGE RES\enc.jpg")