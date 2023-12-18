from key_shuffler import openEncrypted


with openEncrypted("tests/encrypted_wallets.txt", 'r') as file:
    print("OpenEncrypted:")
    for line in file:
        print(line)

