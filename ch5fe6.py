# Introduction to Computation and Programming Using Python (2021)
# Chapter 5, Finger Exercise 6
"""Finger exercise: Using encoder and encrypt as models, implement
the functions decoder and decrypt. Use them to decrypt the message below
which was encrypted using the opening of Don Quixote."""

secret_message = "22*13*33*137*59*11*23*11*1*57*6*13*1*2*6*57*2*6*1*22*13*33*137*59*11*23*11*1*57*6*173*7*11"
secret_book = "In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound for coursing."
gen_decode_keys = (lambda book, cipher_text:{s: book[int(s)] for s in cipher_text.split('*')})

print(secret_message)
print(gen_decode_keys(secret_book, secret_message))
decoder = (lambda code_keys, cipher_text:''.join(code_keys[c] for c in cipher_text))
decrypt = (lambda book, cipher_text:decoder(gen_decode_keys(book, cipher_text), cipher_text.split('*')))
decrypted_text = decrypt(secret_book, secret_message)

print(decrypted_text)