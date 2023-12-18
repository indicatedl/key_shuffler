[![Telegram channel](https://img.shields.io/endpoint?url=https://runkit.io/damiankrawczyk/telegram-badge/branches/master?url=https://t.me/cryptogovnozavod)](https://t.me/cryptogovnozavod)
[![PyPI version](https://badge.fury.io/py/key_shuffler.svg)](https://badge.fury.io/py/key_shuffler)
[![image](https://img.shields.io/pypi/pyversions/key_shuffler.svg)](https://pypi.org/project/key_shuffler/)
[![Github last commit date](https://img.shields.io/github/last-commit/indicatedl/key_shuffler.svg?label=Updated&logo=github&cacheSeconds=600)](https://github.com/indicatedl/key_shuffler/commits)
[![works badge](https://cdn.jsdelivr.net/gh/nikku/works-on-my-machine@v0.2.0/badge.svg)](https://github.com/nikku/works-on-my-machine)  

# key_shuffler

Simply python library for encrypting private keys using character shuffle method.

Supports any blockchains, but is guaranteed to mask only EVM/Aptos private keys.

It checks the correctly entered password by checking the case of the last 2 characters of the key.

Accepts wallets in the format: _address:key_ or _key_

---

# Installation / Установка
```
pip install key-shuffler
```

# Использование (для нормисов на русском языке)

## В качестве отдельного скрипта для шифровки/расшифровки файла (просто скачайте с гитхаба)

Открыть директорию:
```
cd C:\...\key_shuffler
```
Поместить кошели в \examples\wallets.txt в формате _private_key_ или _address:private_key_

Запустить скрипт командой:
```
python examples\file_encryptor.py
```
---

## Внедрение библиотеки в существующий софт

В общем случае: найти в .py файлах софта (чаще всего в config.py/settings.py/main.py) получение КОШЕЛЬКОВ из .txt файла путем поиска по коду по ключевой фразе "with open" (синхронный код) либо "with aiofiles.open" (асинхронный код)

---
_Для синхронного кода:_

Найти:
```python
with open(*файл с кошельками*, 'r') as file:
    ........
```
Добавить выше строкой "from key_shuffler import openEncrypted" и заменить "open" на "openEncrypted"
```python
from key_shuffler import openEncrypted
with openEncrypted(*файл с кошельками*, 'r') as file:
    ........
```
При этом необходимо не накосячить с отступами текста, оставить такими же как были.

Пример. Было:
```python
with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]
```
Стало:
```python
from key_shuffler import openEncrypted
with openEncrypted("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]
```
---
_Для асинхронного кода:_

Найти:
```python
async with aiofiles.open(*файл с кошельками*, 'r') as file:
    ........
```
Добавить выше строкой "from key_shuffler import aiofilesOpenEncrypted" и заменить "aiofiles.open" на "aiofilesOpenEncrypted"
```python
from key_shuffler import aiofilesOpenEncrypted
async with aiofilesOpenEncrypted(*файл с кошельками*, 'r') as file:
    ........
```
При этом необходимо не накосячить с отступами текста, оставить такими же как были.

Пример. Было:
```python
async with aiofiles.open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]
```
Стало:
```python
from key_shuffler import aiofilesOpenEncrypted
async with aiofilesOpenEncrypted("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]
```
# Usage

## Encrypt/decrypt key
```python
from key_shuffler import KeyShuffler
```
_a) The password is already set in the variable:_
```python
private_key = "........"
passphrase = "Hello world" 

shuffler = KeyShuffler(passphrase)
encrypted_key = shuffler.encrypt_private_key(private_key)
decrypted_key = shuffler.decrypt_private_key(encrypted_key)
```

_b) The password will be specified by the user via the terminal:_
```python
private_key = "......."

shuffler = KeyShuffler()
encrypted_key = shuffler.encrypt_private_key(private_key)
decrypted_key = shuffler.decrypt_private_key(encrypted_key)
```

## Encrypt/decrypt file
_Fast sync/async encrypt: using the context manager:_
```python
from key_shuffler import openEncrypted

with openEncrypted(".....", 'r') as file:
    ...
```

```python
from key_shuffler import aiofilesOpenEncrypted

async with aiofilesOpenEncrypted(".....", 'r') as file:
    ...
```

_Default:_
```python
shuffler = KeyShuffler()

wallets = shuffler.encrypt_from_file(file_wallets)
wallets = shuffler.decrypt_from_file(file_wallets)

shuffler.encrypt_file_to_file(file_wallets, file_encrypted_wallets)
shuffler.decrypt_file_to_file(file_encrypted_wallets, file_wallets)

```

## Handling an input error
If the password is incorrect, there will be an error and you will be asked to enter it again:

---


# DONATE (EVM CHAINS) - 0xd8dcc73675a36f618fe780049429ec66f8402199
