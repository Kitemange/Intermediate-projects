import secrets
import string

def generate_password(length):
    """Generate a cryptographically secure password of a given length."""
    # Generate a random password of the given length
    password = ''.join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

def main():
    length = int(input("Length of your password?: "))
    
    #generateandprint assword
    password = generate_password(length)
    print("Generated password:", password)
    
if __name__=="__main__":
    main()

