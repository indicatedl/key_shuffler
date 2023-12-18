from key_shuffler import KeyShuffler

shuffler = KeyShuffler()
shuffler.decrypt_file_to_file("tests/encrypted_wallets.txt", "tests/wallets.txt")