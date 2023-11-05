def encrypt(plain_text, key):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift = ord('a') if char.islower() else ord('A')
            encrypted_char = chr((ord(char) - shift + key) % 26 + shift)
            cipher_text += encrypted_char
        else:
            cipher_text += char
    return cipher_text

def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)

def main():
    while True:
        action = input("Do you want to encrypt or decrypt? ").strip().lower()
        
        if action == "encrypt":
            plain_text = input("What is the plain text? ").strip()
            key = int(input("What is the key? "))
            cipher_text = encrypt(plain_text, key)
            print("Cipher text: " + cipher_text)
        elif action == "decrypt":
            cipher_text = input("What is the cipher text? ").strip()
            key = int(input("What is the key? "))
            plain_text = decrypt(cipher_text, key)
            print("Plain text: " + plain_text)
        else:
            print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
            continue
        
        more = input("Do you want to encrypt or decrypt more? (yes/no) ").strip().lower()
        if more != "yes":
            break

if __name__ == "__main__":
    main()
