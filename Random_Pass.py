import random
import string

# Налаштування параметрів
USE_COMPLEX_PASSWORD = True  # True для складного пароля, False для простого
SHORT_PASSWORD_LENGTH = 6  # Довжина простого пароля
COMPLEX_PASSWORD_LENGTH = 9  # Довжина складного пароля

# Символи для генерації
SIMPLE_CHARS = string.ascii_letters + string.digits  # Літери та цифри
COMPLEX_CHARS = (
    string.ascii_letters + string.digits +
    "!@#$%&*()-=+?"  # Спеціальні символи без :;"'
)

# Вибір параметрів залежно від складності
if USE_COMPLEX_PASSWORD:
    length = COMPLEX_PASSWORD_LENGTH
    characters = COMPLEX_CHARS
else:
    length = SHORT_PASSWORD_LENGTH
    characters = SIMPLE_CHARS

# Генерація пароля
password = ''.join(random.choice(characters) for _ in range(length))

# Вивід результату
print(password)
