# Introduction to Computation and Programming Using Python (2021)
# Chapter 5, Finger Exercise 5
"""(Re book ciphers)
If a character occurs in the plain text but not in the book,
something bad happens. The code_keys dictionary will map each
such character to -1, and decode_keys will map -1 to whatever the
last character in the book happens to be.

Finger Exercise: Remedy the problem described in the previous
paragraph. Hint: a simple way to do this is to create a new book by
appending something to the original book."""

message = "noze is noze"
secret_book = "Once upon a time, in a house in a land far away,"
UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LC_letters = 'abcdefghijklmnopqrstuvwxyz'
letters = UC_letters + LC_letters
secret_book += letters
# Could also append punctuation if needed

gen_code_keys = (lambda book, plain_text:({c: str
(book.find(c)) for c in plain_text}))
encoder = (lambda code_keys, plain_text:''.join(['*' + code_keys[c] for c in plain_text])[1:])
encrpyt = (lambda book, plain_text:encoder(gen_code_keys(book, plain_text), plain_text))

secret_message = encrpyt(secret_book, message)

gen_decode_keys = (lambda book, cipher_text:{s: book[int(s)] for s in cipher_text.split('*')})

# code above here, other than secret_message and second secret_book definition, given in text
print(message)
print(secret_message)
print(gen_decode_keys(secret_book, secret_message))
decoder = (lambda code_keys, cipher_text:''.join(code_keys[c] for c in cipher_text))
decrypt = (lambda book, cipher_text:decoder(gen_decode_keys(book, cipher_text), cipher_text.split('*')))
decrypted_text = decrypt(secret_book, secret_message)

print(decrypted_text)