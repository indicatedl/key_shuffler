from key_shuffler import KeyShuffler


private_key = "0xDEADDEADDEAD083C8AE336aDaF7A82Fd292E13B246245EAB3452DEADDEADDEAD"
passphrase = "Hello world" 


print(f"Original Private Key: {private_key.lower()}")
print(f"Passphrase: {passphrase}")

shuffler = KeyShuffler(passphrase)
encrypted_key = shuffler.encrypt_private_key(private_key)
print(f"Encrypted Private Key: {encrypted_key}")

# passphrase = "Hello world hello world hello world" 
# print(f"Using incorrect passphrase: {passphrase}")
# shuffler = KeyShuffler(passphrase)

decrypted_key = shuffler.decrypt_private_key(encrypted_key)
print(f"Decrypted Private Key: {decrypted_key}")

if private_key.lower() == decrypted_key:
    print(f"Private key successful decrypt!")

