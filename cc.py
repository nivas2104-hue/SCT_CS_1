# Caesar Cipher - Encrypt & Decrypt

def caesar_cipher(text, shift, mode="encrypt"):
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters
            base = ord('A') if char.isupper() else ord('a')
            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:  # decrypt
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep spaces/punctuation as is
    return result


wanna_end = False
while not wanna_end:

    # Take user input
    what_to_do = input("encrypt or decrypt :\n").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if what_to_do == "encrypt":
        encrypted = caesar_cipher(message, shift, "encrypt")
        print("Encrypted message:", encrypted)

    elif what_to_do == "decrypt":
        decrypted = caesar_cipher(message, shift, "decrypt")
        print("Decrypted message:", decrypted)

    # Ask if user wants to continue
    play = input("Do you want to continue? (yes/no): ").lower()
    if play == "no":
        wanna_end = True
        print("BYE!")
