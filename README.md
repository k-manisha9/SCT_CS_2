# Image Encryption & Decryption Tool

This project provides a simple tool for encrypting and decrypting images using various pixel manipulation techniques. It is implemented in Python using OpenCV and NumPy and supports multiple encryption methods, including pixel swapping, XOR encryption, and key addition.

## Features

- **Encryption Methods**:
  - **Pixel Swapping**: Swaps pixels in pairs to create an encrypted image.
  - **XOR Encryption**: Applies a bitwise XOR operation on pixel values using a specified key.
  - **Key Addition**: Adds a specified value to each pixel to encrypt the image.
  
- **Decryption Methods**:
  - **Pixel Swapping Decryption**: Re-swapping the pixels restores the original image.
  - **XOR Decryption**: Reapplying the XOR operation with the same key decrypts the image.
  - **Key Subtraction**: Subtracts the same value from each pixel to recover the original image.

## How It Works

1. **Load the Image**: The image is loaded using OpenCV's `cv2.imread()` method.
2. **Choose Encryption Method**:
   - The user selects an encryption method: `swap`, `xor`, or `add_key`.
   - Optionally, a key is provided for XOR and key addition methods.
3. **Encrypt the Image**: 
   - Depending on the selected method, the image is encrypted using pixel manipulation techniques.
   - The encrypted image is saved to the file `encrypted_image.png`.
4. **Decrypt the Image**: 
   - The user can decrypt the image by selecting the corresponding decryption method and providing the same key used for encryption.
   - The decrypted image is saved to the file `decrypted_image.png`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/image-encryption-tool.git
   ```

2. Navigate to the project directory:
   ```bash
   cd image-encryption-tool
   ```

3. Install the required dependencies:
   ```bash
   pip install opencv-python numpy
   ```

## Usage

1. Place the image you want to encrypt in the project directory (e.g., `butterfly.jpg`).

2. Run the Python script:
   ```bash
   python image_encryption.py
   ```

3. When prompted, enter the encryption method (`swap`, `xor`, `add_key`).

4. The encrypted image will be saved as `encrypted_image.png`.

5. To decrypt the image, use the same method and key that were used for encryption. The decrypted image will be saved as `decrypted_image.png`.

## Example

```bash
Enter the method name: xor
Encrypted image saved at encrypted_image.png
Decrypted image saved at decrypted_image.png
```

## Supported Encryption Methods

- **swap**: Swaps adjacent pixels in the image to obfuscate the original pixel values.
- **xor**: Applies a bitwise XOR operation to each pixel using a user-defined key.
- **add_key**: Adds a user-defined value to each pixel in the image.

## Contributing

Feel free to fork this repository and contribute by adding more encryption methods or improving the code. Pull requests are welcome!

