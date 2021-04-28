import random, string

class SignUpData:
    new_username = ''.join(random.choice(string.ascii_lowercase) for _ in range(8))
    phone_number = ''.join(random.choices(string.digits, k=10))
    email = new_username + "@gmail.com"
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    confirm_password = password
    invitation_code = "1234"