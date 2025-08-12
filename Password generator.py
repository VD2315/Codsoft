import string
import secrets

def generate_password(length, use_digits, use_special):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

while True:
    try:
        length = int(input("Enter desired password length: ").strip())
        if length <= 0:
            print("Please enter a positive number.")
            continue
        break
    except ValueError:
        print("Please enter a valid integer.")

use_digits = input("Include digits? (y/n): ").strip().lower().startswith('y')
use_special = input("Include special characters? (y/n): ").strip().lower().startswith('y')

if not (use_digits or use_special):
    confirm = input("No digits or special characters selected. Continue with letters only? (y/n): ").strip().lower()
    if not confirm.startswith('y'):
        use_digits = input("Include digits? (y/n): ").strip().lower().startswith('y')
        use_special = input("Include special characters? (y/n): ").strip().lower().startswith('y')

password = generate_password(length, use_digits, use_special)
print("Generated Password:", password)
