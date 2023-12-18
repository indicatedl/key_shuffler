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

# Installation 
```
pip install key-shuffler
```

# Usage

## В качестве отдельного скрипта для шифровки/расшифровки файла (скачайте с гитхаба)

Открыть директорию:
```
cd C:\...\key_shuffler
```
Поместить копию приватных ключей в \examples\wallets.txt в формате _private_key_ или _address:private_key_

Запустить скрипт командой:
```
python examples\file_encryptor.py
```

## Внедрение в существующий софт

В общем случае:
Найти в .py файлах софта (чаще всего в config.py/settings.py/main.py) получение кошельков из .txt файла путем поиска по ключевой фразе "with open" либо "with aiofiles.open"
```python
with open(WALLETS_FILE, 'r') as file:
    ........
    wallets = ....
```
Заменить весь блок with open...., включая все что находится с отступом под ним на
```python
from key_shuffler import KeyShuffler
wallets = KeyShuffler.decrypt_file('your_file.txt')
```

Пример: было
```python
with open("accounts.txt", "r") as file:
    ACCOUNTS = [row.strip() for row in file]
```
Стало:
```python
from key_shuffler import KeyShuffler
ACCOUNTS = KeyShuffler.decrypt_file("accounts.txt")
```


# DONATE (EVM CHAINS) - 0xd8dcc73675a36f618fe780049429ec66f8402199
