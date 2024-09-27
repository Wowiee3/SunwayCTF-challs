# Visit https://www.lddgo.net/en/string/pyc-compile-decompile for more information
# Version : Python 3.8

import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def steal_browser_history():
    print('[*] Stealing browser history...')
    time.sleep(2)
    browser_files = [
        'C:/Users/XXX/AppData/Local/Google/Chrome/User Data/Default/History',
        'C:/Users/XXX/AppData/Local/Mozilla/Firefox/Profiles/xyz.default-release/places.sqlite']
    for file in browser_files:
        print(f'''Accessing {file}''')
        time.sleep(1)


def access_system_files():
    print('[*] Searching for sensitive system files...')
    time.sleep(2)
    system_files = [
        'C:/Windows/System32/config/SAM',
        'C:/Windows/System32/drivers/etc/hosts',
        'C:/Windows/Logs/DPX/setupact.log']
    for file in system_files:
        print(f'''Accessing {file}''')
        time.sleep(1)

LADDERS = '8cbb8acce9e5a6ffd9e858891a57876dfa3a4e49b71309b928d134ae40ad8f79'
DICE = '536e616b6548617465734c616464657273496e4d79496e666f537465616c6572'

def decrypt_flag(LADDERS, DICE):
    DICE = bytes.fromhex(DICE)
    LADDERS = bytes.fromhex(LADDERS)
    cipher = Cipher(algorithms.AES(DICE), modes.ECB())
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(LADDERS) + decryptor.finalize()
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
    return decrypted_data.decode()


def main():
    print('[*] The SmurfyStealer is running...')
    time.sleep(1)
    steal_browser_history()
    access_system_files()
    print(f'''[*] Flag stolen: {LADDERS}''')
    input('[*] Press Enter to exit...')

if __name__ == '__main__':
    main()
