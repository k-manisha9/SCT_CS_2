import cv2
import numpy as np

# Load the image
image_path = 'butterfly.jpg'
image = cv2.imread(image_path)

# Ensure the image is loaded
if image is None:
    raise ValueError("Image not found or unable to load.")

# Function to encrypt the image by swapping pixel values
def swap_pixels(image):
    encrypted_image = image.copy()
    height, width, _ = image.shape
    for i in range(0, height, 2):
        for j in range(0, width, 2):
            # Swap pixels (i, j) with (i+1, j+1), ensure within bounds
            if i + 1 < height and j + 1 < width:
                encrypted_image[i, j], encrypted_image[i+1, j+1] = encrypted_image[i+1, j+1], encrypted_image[i, j]
    return encrypted_image

# Function to encrypt the image by applying a basic mathematical operation (XOR)
def apply_xor(image, key=42):
    encrypted_image = image.copy()
    encrypted_image = cv2.bitwise_xor(encrypted_image, key)
    return encrypted_image

# Function to encrypt the image by adding a key to each pixel value
def add_key(image, key=255):
    encrypted_image = image.copy()
    encrypted_image = cv2.add(encrypted_image, key)
    return encrypted_image

# Function to decrypt the image by subtracting the key from each pixel value
def subtract_key(image, key=255):
    decrypted_image = image.copy()
    decrypted_image = cv2.subtract(decrypted_image, key)
    return decrypted_image

# Choose encryption method
def encrypt_image(image, method='swap', key=42):
    if method == 'swap':
        return swap_pixels(image)
    elif method == 'xor':
        return apply_xor(image, key)
    elif method == 'add_key':
        return add_key(image, key)
    else:
        raise ValueError("Invalid encryption method selected.")

# Decryption functions
# For XOR, applying the XOR operation again with the same key decrypts the image
def decrypt_xor(image, key=42):
    return apply_xor(image, key)  # XOR with the same key reverses encryption

# For swap, swapping the same pixels again decrypts the image
def decrypt_swap(image):
    return swap_pixels(image)  # Re-swapping restores the original order

# For add_key, subtracting the key decrypts the image
def decrypt_add_key(image, key=10):
    return subtract_key(image, key)

# Choose decryption method
def decrypt_image(image, method='swap', key=42):
    if method == 'swap':
        return decrypt_swap(image)
    elif method == 'xor':
        return decrypt_xor(image, key)
    elif method == 'add_key':
        return decrypt_add_key(image, key)
    else:
        raise ValueError("Invalid decryption method selected.")


method_name=input("Enter the method name: ")

encrypted_image = encrypt_image(image, method=method_name, key=50)

# Saving the encrypted image
encrypted_output_path = 'encrypted_image.png'
cv2.imwrite(encrypted_output_path, encrypted_image)
print(f"Encrypted image saved at {encrypted_output_path}")

# Example: Decrypt the image
decrypted_image = decrypt_image(encrypted_image, method=method_name, key=50)

# Saving the decrypted image
decrypted_output_path = 'decrypted_image.png'
cv2.imwrite(decrypted_output_path, decrypted_image)
print(f"Decrypted image saved at {decrypted_output_path}")
