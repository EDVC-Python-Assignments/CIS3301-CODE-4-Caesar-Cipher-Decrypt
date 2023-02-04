import os,sys
from mock_input_tests import *
from code_4 import main
import random

def check_if_file_exists():
    try:
        exists = os.path.exists("code_4.py")
        assert exists == True
    except:
        sys.exit()

def get_caesar_encryption(word,key):
    encrypted_word = [chr(ord(x)+key) for x in word]
    return "".join(encrypted_word)

def test_encryption():
    check_if_file_exists()
    words = ["apple", "orange", "kiwi", "pear", "grape"]
    secret = random.choice(words)
    key = random.randint(1,4)
    encrypted_message = get_caesar_encryption(secret,key)

    set_keyboard_input([encrypted_message,key])

    main()
    output = get_display_output()

    assert output == [
        "\nCaesar Cipher - Program",
        "\nEnter the secret to decrypt: ",
        "Enter your key: ",
        f"\nThe secret is {secret}\n"
    ]