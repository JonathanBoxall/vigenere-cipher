text = 'super secret message' #Message to encrypt
custom_key = 'highlysecurekey' # Key to use to encrypt/decrypt

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            encrypted += char
        else:        
            # Find the character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            encrypted += alphabet[new_index]
    
    return encrypted
# Function to encrypt with the cipher
def encrypt(message, key):
    return vigenere(message, key)
# Function to decrypt with the cipher    
def decrypt(message, key):
    return vigenere(message, key, -1)

print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
