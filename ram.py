def caesar_cipher(text, shift, mode="encrypt"):
    shift = shift % 26
    if mode == "decrypt":
        shift = -shift

    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            idx = ord(ch) - base
            new_idx = (idx + shift) % 26
            result.append(chr(new_idx + base))
        else:
            result.append(ch)
    return ''.join(result)


def main():
    print("=== Caesar Cipher Program ===")
    while True:
        print("\nMain Options:")
        print("1. Encrypt only")
        print("2. Decrypt only")
        print("3. Both (Encrypt + Decrypt)")
        choice = input("Choose option: ")

        if choice == "1":
            msg = input("Enter your message: ")
            shift = int(input("Enter shift value: "))
            print("Encrypted:", caesar_cipher(msg, shift, "encrypt"))

        elif choice == "2":
            msg = input("Enter your encrypted message: ")
            shift = int(input("Enter shift value: "))
            print("Decrypted:", caesar_cipher(msg, shift, "decrypt"))

        elif choice == "3":
            msg = input("Enter your message: ")
            shift = int(input("Enter shift value: "))
            encrypted = caesar_cipher(msg, shift, "encrypt")
            decrypted = caesar_cipher(encrypted, shift, "decrypt")
            print("Encrypted:", encrypted)
            print("Decrypted:", decrypted)

        else:
            print("Invalid choice, try again.")
            continue  # skip asking continue if invalid input

        # ask user if they want to continue
        cont = input("\nDo you want to continue? (y/n): ").lower()
        if cont != "y":
            print("Exiting... Goodbye!")
            break


if __name__ == "__main__":
    main()
