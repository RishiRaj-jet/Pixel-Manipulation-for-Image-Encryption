from PIL import Image
import numpy as np
import os

def encrypt_image(input_path, output_path, key):
    try:
        # Print the current working directory
        print("Current Working Directory: ", os.getcwd())
        print("Directory Listing: ", os.listdir(os.getcwd()))
        
        # Open the input image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Encrypt by swapping pixels
        np.random.seed(key)
        flat_pixels = pixels.flatten()
        indices = np.arange(len(flat_pixels))
        np.random.shuffle(indices)
        encrypted_pixels = flat_pixels[indices].reshape(pixels.shape)
        
        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_pixels.astype('uint8'))
        encrypted_img.save(output_path)
        print(f"Image encrypted and saved to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(input_path, output_path, key):
    try:
        # Open the encrypted image
        img = Image.open(input_path)
        pixels = np.array(img)
        
        # Decrypt by reversing the pixel swap
        np.random.seed(key)
        flat_pixels = pixels.flatten()
        indices = np.arange(len(flat_pixels))
        np.random.shuffle(indices)
        
        decrypted_pixels = np.empty_like(flat_pixels)
        decrypted_pixels[indices] = flat_pixels
        decrypted_pixels = decrypted_pixels.reshape(pixels.shape)
        
        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_pixels.astype('uint8'))
        decrypted_img.save(output_path)
        print(f"Image decrypted and saved to {output_path}")
    except FileNotFoundError:
        print(f"File not found: {input_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
key = 12345
input_image_path = 'C:\\Users\\RISHI\\Desktop\\prodigyintern\\task-2\\input.jpg'
encrypted_image_path = 'C:\\Users\\RISHI\\Desktop\\prodigyintern\\task-2\\encrypted_image.png'
decrypted_image_path = 'C:\\Users\\RISHI\\Desktop\\prodigyintern\\task-2\\decrypted_image.png'

encrypt_image(input_image_path, encrypted_image_path, key)
decrypt_image(encrypted_image_path, decrypted_image_path, key)
