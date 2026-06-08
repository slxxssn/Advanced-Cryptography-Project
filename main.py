from classical import (
    caesar_encrypt,
    caesar_decrypt,
    vigenere_encrypt,
    vigenere_decrypt
)

from stream_cipher import lfsr, rc4_simulation
import time

print("=== Secure File Encryption System ===")

text = input("Enter text: ").upper()

if text == "":
    print("Error: input cannot be empty")

else:
    print("Valid input")

    # =========================
    # WEEK 2 OUTPUT (CLASSICAL)
    # =========================
    print("\n===== Encryption and Decryption Output =====")

    caesar_encrypted = caesar_encrypt(text, 5)
    caesar_decrypted = caesar_decrypt(caesar_encrypted, 5)

    print("\nOriginal Text:", text)
    print("Caesar Encrypted:", caesar_encrypted)
    print("Caesar Decrypted:", caesar_decrypted)

    vigenere_encrypted = vigenere_encrypt(text, "SAFE")
    vigenere_decrypted = vigenere_decrypt(vigenere_encrypted, "SAFE")

    print("\nVigenere Encrypted:", vigenere_encrypted)
    print("Vigenere Decrypted:", vigenere_decrypted)

    # =========================
    # WEEK 2 TESTING RESULTS
    # =========================
    print("\n===== Cipher Testing Results =====")

    test_cases = ["HELLO", "SECURITY", "CRYPTO"]

    for item in test_cases:
        print("\nTesting:", item)
        print("Caesar:", caesar_encrypt(item, 5))
        print("Vigenere:", vigenere_encrypt(item, "SAFE"))

    # =========================
    # WEEK 3 - LFSR
    # =========================
    print("\n===== LFSR Generator =====")

    seed = [1, 0, 1, 1]
    taps = [0, 1]

    sequence = lfsr(seed, taps, 20)

    print("Pseudorandom Sequence:")
    print(sequence)

    ones = sequence.count(1)
    zeros = sequence.count(0)

    print("\nRandomness Test")
    print("Ones:", ones)
    print("Zeros:", zeros)

    # =========================
    # WEEK 3 - RC4 SIMULATION
    # =========================
    print("\n===== RC4 Simulation =====")

    encrypted = rc4_simulation("HELLO", "KEY")
    print("Encrypted Output:", encrypted)

    # =========================
    # PERFORMANCE TEST
    # =========================
    print("\n===== Performance Test =====")

    start = time.time()

    for _ in range(1000):
        rc4_simulation("HELLOCRYPTO", "KEY")

    end = time.time()

    print("Execution Time:", end - start)




    from aes_cipher import generate_key, load_key, encrypt_file, decrypt_file

print("\n===== AES FILE ENCRYPTION (WEEK 4) =====")

key = generate_key()
print("Key generated and saved as secret.key")

# Create a sample file (for demo)
with open("sample.txt", "w") as f:
    f.write("This is a secure file encryption test.")

# Encrypt file
encrypt_file("sample.txt", key)
print("File encrypted → sample.txt.enc")

# Decrypt file
decrypted = decrypt_file("sample.txt.enc", key)
print("File decrypted successfully")




import time

start = time.time()

for _ in range(100):
    encrypt_file("sample.txt", key)

end = time.time()

print("\nAES Performance Test")
print("Time:", end - start)