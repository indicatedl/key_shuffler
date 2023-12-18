from key_shuffler import KeyShuffler

shuffler = KeyShuffler()
shuffler.encrypt_file_to_file("tests/wallets.txt", "tests/encrypted_wallets.txt")