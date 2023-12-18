import os
import random
import locale


class KeyShuffler:
    def __init__(self, 
                 seed: str =False) -> None:
        self.seed = seed
        self.language = 'ru' if any(locale.getdefaultlocale()[0].startswith(lang) for lang in ['ru', 'be', 'kk', 'uk']) else 'en'

    def get_passphrase(self, 
                       new=False) -> None:
        if new:
            if self.language == 'ru':
                print('Придумайте секретную фразу/пароль (используйте больше 13 символов): ', end='')
            else:
                print('Create and input your passphrase/password (use more than 13 characters): ', end='')
        else:
            if self.language == 'ru':
                print('Введите вашу секретную фразу/пароль от приватников: ', end='')
            else:
                print('Input your passphrase/password for private keys: ', end='')
        self.seed = input('').strip()
        print('\033[F'+' '*(len(self.seed)+75))

    def create_sequence(self, 
                        num: int) -> list:
        index_order = list(range(num))
        random.seed(self.seed)
        random.shuffle(index_order)
        return index_order
        
    def encrypt_private_key(self, 
                            private_key: str) -> str:
        if not self.seed:
            self.get_passphrase(new=True)
        prefix = "0x" if private_key.startswith("0x") else ""
        last_two_indices = [i for i, char in enumerate(private_key) if char.isalpha()][-2:]
        private_key = ''.join(char.upper() if i in last_two_indices else char for i, char in enumerate(private_key.lower()))
        index_order = self.create_sequence(len(private_key[len(prefix):]))
        encrypted_key = [private_key[i + len(prefix)] for i in index_order]
        return prefix + ''.join(encrypted_key)

    def decrypt_private_key(self, 
                            encrypted_key: str) -> str:
        if not self.seed:
            self.get_passphrase(new=False)

        prefix = "0x" if encrypted_key.startswith("0x") else ""
        while True:
            index_order = self.create_sequence(len(encrypted_key[len(prefix):]))
            decrypted_key = [''] * len(index_order)
            for i, char in zip(index_order, encrypted_key[len(prefix):]):
                decrypted_key[i] = char
            decrypted_key_str = prefix + ''.join(decrypted_key)
            last_two_alpha = ''.join(filter(str.isalpha, decrypted_key_str))[-2:]
            if last_two_alpha.isupper():
                return decrypted_key_str.lower()
            else:
                if self.language == 'ru':
                    print("\nНеверный пароль! Попробуй снова\n")
                else:
                    print("\nIncorrect password! Please try again\n")
                self.get_passphrase(new=False)

    def get_wallets_from_file(self, 
                              file_wallets: str) -> list:
        try:
            with open(file_wallets, 'r') as file:
                wallets = [row.strip().split(':') for row in file]
            return wallets
        except FileNotFoundError:
            print(f"Error: File '{file_wallets}' not found.")
            return []

    def save_wallets_to_file(self, 
                             wallets: list, 
                             file_wallets: str) -> None:
        if not os.path.isfile(file_wallets):
            open(file_wallets, 'w').close()
        with open(file_wallets, 'w') as file:
            for wallet in wallets:
                if len(wallet) > 1:
                    file.write(f"{wallet[0]}:{wallet[1]}\n")
                else:
                    file.write(f"{wallet[0]}\n")

    def encrypt_file(self, 
                     file_wallets: str) -> list:
        if not self.seed:
            self.get_passphrase(new=True)
        wallets = self.get_wallets_from_file(file_wallets)
        for wallet in wallets:
            if len(wallet) > 1:
                wallet[1] = self.encrypt_private_key(wallet[1])
            else:
                wallet[0] = self.encrypt_private_key(wallet[0])
        return wallets

    def decrypt_file(self, 
                     file_wallets: str) -> list:
        if not self.seed:
            self.get_passphrase(new=False)
        wallets = self.get_wallets_from_file(file_wallets)
        for wallet in wallets:
            if len(wallet) > 1:
                wallet[1] = self.decrypt_private_key(wallet[1])
            else:
                wallet[0] = self.decrypt_private_key(wallet[0])
        return wallets

    def encrypt_file_to_file(self, 
                             from_file: str, 
                             to_file: str) -> None:
        wallets = self.encrypt_file(from_file)
        self.save_wallets_to_file(wallets, to_file)

    def decrypt_file_to_file(self, 
                             from_file: str, 
                             to_file: str) -> None:
        wallets = self.decrypt_file(from_file)
        self.save_wallets_to_file(wallets, to_file)

