import string
import secrets

def generate_strong_password(length=12):
    """
    Generates a strong, random password of a specified length.
    The password will contain a mix of uppercase and lowercase letters,
    digits, and punctuation.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    # Define the possible characters using string constants
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one of each character type for strength
    password_list = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]
    
    # Fill the remainder of the password length with random choices from all characters
    for _ in range(length - 4):
        password_list.append(secrets.choice(characters))
        
    # Shuffle the list to ensure randomness of character positions
    secrets.SystemRandom().shuffle(password_list)
    
    # Join the characters to form the final password string
    return "".join(password_list)

# Example Usage:
new_password = generate_strong_password(16)
print(f"Generated Password: {new_password}")
