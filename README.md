[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/cryptogovnozavod)](https://t.me/cryptogovnozavod)
[![PyPI version](https://badge.fury.io/py/key_shuffler.svg)](https://badge.fury.io/py/key_shuffler)
[![image](https://img.shields.io/pypi/pyversions/key_shuffler.svg)](https://pypi.org/project/key_shuffler/)
[![Github last commit date](https://img.shields.io/github/last-commit/indicatedl/key_shuffler.svg?label=Updated&logo=github&cacheSeconds=600)](https://github.com/indicatedl/key_shuffler/commits)
[![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)  

# key_shuffler

Simply python library for encrypting private keys using character shuffle method.
Supports any blockchains, but is guaranteed to mask only EVM/Aptos private keys.
It checks the correctly entered password by checking the case of the last 2 characters of the key.

---

# Installation / Установка
```
pip install key-shuffler
```

# Usage / Использование

## В качестве отдельного скрипта для шифровки/расшифровки файла (просто скачайте с гитхаба)

Открыть директорию:
```
cd C:\...\key_shuffler
```
Поместить копию приватных ключей в \examples\wallets.txt в формате _private_key_ или _address:private_key_

Запустить скрипт командой:
```
python examples\file_encryptor.py
```

## Внедрение библиотеки в существующий софт

В общем случае: найти в .py файлах софта (чаще всего в config.py/settings.py/main.py) получение кошельков из .txt файла путем поиска по ключевой фразе "with open" либо "with aiofiles.open"
```python
with open(WALLETS_FILE, 'r') as file:
    ........
    WALLETS = ....
```
Заменить весь блок with open...., включая все что находится с отступом под ним на
```python
from key_shuffler import KeyShuffler
WALLETS = KeyShuffler().decrypt_file(WALLETS_FILE)
```
При этом необходимо сохранить имя файла с кошельками WALLETS_FILE и имя переменной с кошельками WALLETS.

Пример:
```python
with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]
```
Стало:
```python
from key_shuffler import KeyShuffler
ACCOUNTS = KeyShuffler().decrypt_file("accounts.txt")
```

# EXAMPLES

```python
from key_shuffler import KeyShuffler
```
a) The password is already set in the variable:
```python
private_key = "........"
passphrase = "Hello world" 

shuffler = KeyShuffler(passphrase)
encrypted_key = shuffler.encrypt_private_key(private_key)
decrypted_key = shuffler.decrypt_private_key(encrypted_key)
```

b) The password will be specified by the user via the terminal:
```python
private_key = "......."

shuffler = KeyShuffler()
encrypted_key = shuffler.encrypt_private_key(private_key)
decrypted_key = shuffler.decrypt_private_key(encrypted_key)
```

If the password is incorrect, there will be an error and you will be asked to enter it again:
```python
new_passphrase = "Hello world hello world hello world" 
shuffler = KeyShuffler(new_passphrase)
decrypted_key = shuffler.decrypt_private_key(encrypted_key) # Error
```


# DONATE (EVM CHAINS) - 0xd8dcc73675a36f618fe780049429ec66f8402199
