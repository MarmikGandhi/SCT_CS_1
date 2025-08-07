def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(cipher, shift):
    return encrypt(cipher, -shift)

# --- User Interface ---
print("=== Caesar Cipher Encryption / Decryption ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value (number): "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"\n🔒 Encrypted: {encrypted}")
print(f"🔓 Decrypted: {decrypted}")
