while True:
    choice = int(input("---MENU---\n 1. Encrypt Text\n 2. Decrypt Text\n 3. Exit\nEnter your choice: "))
    
    if choice == 1:
        message = input("Enter text to encrypt: ")
        shift_value = int(input("Enter encryption key (shift value): "))
        encrypted_message = ""
        
        for char in message:
            ascii_value = ord(char)
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                ascii_value += shift_value
                
            if 'A' <= char <= 'Z' and ascii_value > 90:
                ascii_value -= 26
            elif 'a' <= char <= 'z' and ascii_value > 122:
                ascii_value -= 26
                
            encrypted_message += chr(ascii_value)
    
        print(f"Encrypted Text: {encrypted_message}\n")
    
    elif choice == 2:
        message = input("Enter text to decrypt: ")
        shift_value = int(input("Enter decryption key (shift value): "))
        decrypted_message = ""
        
        for char in message:
            ascii_value = ord(char)
            if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
                ascii_value -= shift_value
                
            if 'A' <= char <= 'Z' and ascii_value < 65:
                ascii_value += 26
            elif 'a' <= char <= 'z' and ascii_value < 97:
                ascii_value += 26
        
            decrypted_message += chr(ascii_value)
        
        print(f"Decrypted Text: {decrypted_message}")
    
    elif choice == 3:
        break
