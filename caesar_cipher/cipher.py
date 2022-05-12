import re
from caesar_cipher.corpus_loader import word_list, name_list

lowercase_alphabet = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key): # Thank you stackoverflow.com :)
    # Will only take in alphabet characters only upper/lower
    # Handling both upper and lower case string.
    string = lowercase_alphabet + uppercase_alphabet

    # Performs shift of lower and upper case string with the given key.
    # The [key] tells the individual string value how many index to shift over to.
    shifted_lowercase_alphabet = lowercase_alphabet[key:] + lowercase_alphabet[:key]
    shifted_uppercase_alphabet = uppercase_alphabet[key:] + uppercase_alphabet[:key]
    shifted_alphabet = shifted_lowercase_alphabet + shifted_uppercase_alphabet

    # Maketrans(), maps out the shifted string and returns string in numerical value.
    map_cipher = str.maketrans(string, shifted_alphabet)
    # Translate() takes the returned values from maketrans() and converts it back to alphabet characture.
    cipher = text.translate(map_cipher)
    # Returns the ciphered text
    return cipher


def decrypt(cipher, key): # Decryption with the encrypted cipher and the key value to shift back.
    return encrypt(cipher, -key)

def count_words(cipher): # Thankyou JB for the fallowing code.
    words = 0
    cipher_text = cipher.split()
    # iterating through the cipher text to see if any matches the imported word_list or name_list.
    for text in cipher_text:
        word = re.sub(r'[^A-Za-z]+','', text)
        if word.lower() in word_list or word in name_list:
            words += 1

    return words

def crack(cipher): # Thank you JB for the fallowing code.
    for key in range(26): # Iterate through for possible keys in the range of 26 letters in the alphabet.
        crack_cipher = decrypt(cipher, key)
        word_count = count_words(crack_cipher)
        percent = int(word_count / len(cipher.split()) * 100)
        if percent > 50:
            return crack_cipher

    return ''

