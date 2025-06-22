from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    # Open and convert image to RGB
    image = Image.open(input_path).convert("RGB")
    data = np.array(image)

    # Encrypt: apply XOR and reverse rows
    encrypted_data = data ^ key
    encrypted_data = encrypted_data[::-1]

    encrypted_image = Image.fromarray(encrypted_data.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"[+] Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open and convert image to RGB
    image = Image.open(input_path).convert("RGB")
    data = np.array(image)

    # Decrypt: reverse rows back and apply XOR
    decrypted_data = data[::-1]
    decrypted_data = decrypted_data ^ key

    decrypted_image = Image.fromarray(decrypted_data.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"[+] Image decrypted and saved as {output_path}")

if __name__ == "__main__":
    # Change the filenames as needed
    key = 123  # You can change the key (must be between 0 and 255)
    encrypt_image("original_image.png", "encrypted_image.png", key)
    decrypt_image("encrypted_image.png", "decrypted_image.jpg", key)
