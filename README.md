# Bencode Parser 🚀

A simple and efficient Bencode encoder/decoder. 🛠️

## 📖 Overview

Bencode is the encoding format used by the BitTorrent protocol for storing and transmitting data. This repository provides a lightweight implementation for encoding and decoding Bencoded data. 🔄

## ✨ Features

- ✅ Encode Python data structures (dict, list, int, bytes) into Bencode format.
- ✅ Decode Bencoded data back into Python objects.
- ✅ Simple and efficient implementation. ⚡

## 📦 Installation

Clone the repository:

```sh
$ git clone https://github.com/yourusername/bencode-parser.git
$ cd bencode-parser
```

## 🚀 Usage

### 📝 Encoding

```python
from bencode import Encoder

data = {"key": "value", "number": 42, "list": [1, 2, 3]}
Encoder(data).encode()
```

### 🔍 Decoding

```python
from bencode import Decoder

data = b"d3:key5:value6:numberi42e4:listli1ei2ei3ee"
Decoder(data).decode()
```

## 📜 License

This project is licensed under the MIT License. See `LICENSE` for details. 📝

## 👤 Author

[0youcef](https://github.com/0youcef) ✨
