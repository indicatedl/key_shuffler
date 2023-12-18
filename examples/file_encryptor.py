import os

from key_shuffler import KeyShuffler


file_wallets = 'examples/wallets.txt'
file_encrypted_wallets = 'examples/encrypted_wallets.txt'


def get_action_id(lang):
    if lang == 'ru':
        action_id = input('''
1. Зашифровать файл wallets.txt -> encrypted_wallets.txt
2. Расшифровать файл encrypted_wallets.txt -> wallets.txt
3. Выход
                      
Выберите действие: ''')
    else:
        action_id = input('''
1. Encrypt the file wallets.txt -> encrypted_wallets.txt
2. Decrypt the file encrypted_wallets.txt -> wallets.txt
3. Exit
                      
Choose an action: ''')

    return int(action_id)

def main():
    shuffler = KeyShuffler()
    action = get_action_id(shuffler.language)
    match action:
        case 1:
            shuffler.encrypt_file_to_file(file_wallets, file_encrypted_wallets)
            if shuffler.language == 'ru':
                print(f'Кошельки успешно зашифрованы в файл {file_encrypted_wallets}\n')
            else:
                print(f'Wallets successfull encrypted to file {file_encrypted_wallets}\n')
        case 2:
            shuffler.decrypt_file_to_file(file_encrypted_wallets, file_wallets)
            if shuffler.language == 'ru':
                print(f'Кошельки успешно расшифрованы в файл {file_wallets}\n')
            else:
                print(f'Wallets successfull decrypted to file {file_wallets}\n')
        case 3:
            return

if (__name__ == '__main__'):
    if not os.path.isfile(file_wallets):
       open(file_wallets, 'w').close()
    main()

